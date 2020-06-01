from patternScanner import get_candle_funcs
import yfinance as yf
import numpy as np
import utils
import statics
import sys
import talib
import matplotlib.pyplot as plt
import pandas as pd

def fetchData(tickerList, fetchOptions):
    try:
        data = yf.download(  # or pdr.get_data_yahoo(...
            # tickers list or string as well
            tickers = str(' '.join(tickerList)),

            # start="2014-04-01", end="2014-04-10",
            # start="2020-03-01", end="2020-03-04",
            # use "period" instead of start/end
            # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
            # (optional, default is '1mo')
            period = fetchOptions['period'],

            # fetch data by interval (including intraday if period < 60 days)
            # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
            # (optional, default is '1d')
            interval = fetchOptions['interval'],

            # group by ticker (to access via data['SPY'])
            # (optional, default is 'column')
            group_by = fetchOptions['group_by'],

            # adjust all OHLC automatically
            # (optional, default is False)
            auto_adjust = fetchOptions['auto_adjust'],

            # download pre/post regular market hours data
            # (optional, default is False)
            prepost = fetchOptions['prepost'],

            # use threads for mass downloading? (True/False/Integer)
            # (optional, default is True)
            threads = fetchOptions['threads'],

            # proxy URL scheme use use when downloading?
            # (optional, default is None)
            proxy = fetchOptions['proxy'],
        )
        

        results = {
            'alerts': {},
            # 'data': data,
        }
        for ticker in tickerList:
            tickerInvestigationData = investigateTickerDf(data[ticker])
            if tickerInvestigationData:
                results['alerts'][ticker] = tickerInvestigationData


        return results

    except ValueError:
        print("Unexpected error:", sys.exc_info()[0])
        raise


def investigateTickerDf(df):
    cleanDf = utils.cleanDf(df)
    
    tickerResult = {}
   
    # more indicators:
    # http://tutorials.topstockresearch.com/candlestick/Bearish/DarkCloudCover/TutotrialOnDarkCloudCoverChartPattern.html
    # momentum indicator (RSI)
    # momentumIndicatorRes = momentumIndicator(cleanDf)
    # trend = utils.identifyTrend(df.Open, df.High, df.Low, df.Close, df.Volume)

    ta = technicalIndicatorsDf(cleanDf)

    trend = utils.identifyTrend(ta, cleanDf)
    # ta.to_json(r'ta-data.json')
    ##################################
    # set results:
    ##################################
    return {
        'ta': ta,
        # 'momentumIndicator': momentumIndicatorRes,
        'candlestickPatternsIndicator': candlestickPatternsIndicator(cleanDf, trend),       # candlestick patterns indicators
        f'{statics.indicatorsConfigurations["increasedVolumeIndicator"]["timeperiod"]}DaysIncreasedVolumeIndicator': increasedVolumeBarsIndicator(cleanDf, statics.indicatorsConfigurations["increasedVolumeIndicator"]["timeperiod"]),    # 3 days increased volume indicator
    }

def technicalIndicatorsDf(daily_data):
        """
        Assemble a dataframe of technical indicator series for a single stock
        """
        o = daily_data['Open'].values
        c = daily_data['Close'].values
        h = daily_data['High'].values
        l = daily_data['Low'].values
        v = daily_data['Volume'].astype(float).values
        # define the technical analysis matrix

        # Most data series are normalized by their series' mean
        ta = {} #pd.DataFrame()
        # ta = pd.DataFrame()
        ta['MA5'] = talib.MA(c, timeperiod=5)
        ta['MA10'] = talib.MA(c, timeperiod=10)
        ta['MA20'] = talib.MA(c, timeperiod=20)
        ta['MA60'] = talib.MA(c, timeperiod=60)
        ta['MA120'] = talib.MA(c, timeperiod=120)
        ta['MA5Volume'] = talib.MA(v, timeperiod=5)
        ta['MA10Volume'] = talib.MA(v, timeperiod=10)
        ta['MA20Volume'] = talib.MA(v, timeperiod=20)
        ta['ADX'] = talib.ADX(h, l, c, timeperiod=14)
        ta['ADXR'] = talib.ADXR(h, l, c, timeperiod=14)
        ta['MACD'] = talib.MACD(c, fastperiod=12, slowperiod=26, signalperiod=9)[0]
        ta['RSI'] = talib.RSI(c, timeperiod=14)
        ta['BBANDS_U'] = talib.BBANDS(c, timeperiod=20, nbdevup=2, nbdevdn=2, matype=0)[0]
        ta['BBANDS_M'] = talib.BBANDS(c, timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)[1]
        ta['BBANDS_L'] = talib.BBANDS(c, timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)[2]
        ta['BBP'] = bbp(c)
        ta['AD'] = talib.AD(h, l, c, v)        
        ta['ATR'] = talib.ATR(h, l, c, timeperiod=14)        
        ta['HT_DC'] = talib.HT_DCPERIOD(c)        
        ta["High/Open"] = h / o
        ta["Low/Open"] = l / o
        ta["Close/Open"] = c / o
        ta['Open'] = o
        ta['Close'] = c
        ta['High'] = h
        ta['Low'] = l
        ta['Volume'] = v

        # Normalized values
        ta['MA5-normalized'] = talib.MA(c, timeperiod=5) / np.nanmean(talib.MA(c, timeperiod=5))
        ta['MA10-normalized'] = talib.MA(c, timeperiod=10) / np.nanmean(talib.MA(c, timeperiod=10))
        ta['MA20-normalized'] = talib.MA(c, timeperiod=20) / np.nanmean(talib.MA(c, timeperiod=20))
        ta['MA60-normalized'] = talib.MA(c, timeperiod=60) / np.nanmean(talib.MA(c, timeperiod=60))
        ta['MA120-normalized'] = talib.MA(c, timeperiod=120) / np.nanmean(talib.MA(c, timeperiod=120))
        ta['MA5-normalized'] = talib.MA(v, timeperiod=5) / np.nanmean(talib.MA(v, timeperiod=5))
        ta['MA10-normalized'] = talib.MA(v, timeperiod=10) / np.nanmean(talib.MA(v, timeperiod=10))
        ta['MA20-normalized'] = talib.MA(v, timeperiod=20) / np.nanmean(talib.MA(v, timeperiod=20))
        ta['ADX-normalized'] = talib.ADX(h, l, c, timeperiod=14) / np.nanmean(talib.ADX(h, l, c, timeperiod=14))
        ta['ADXR-normalized'] = talib.ADXR(h, l, c, timeperiod=14) / np.nanmean(talib.ADXR(h, l, c, timeperiod=14))
        ta['MACD-normalized'] = talib.MACD(c, fastperiod=12, slowperiod=26, signalperiod=9)[0] / \
                     np.nanmean(talib.MACD(c, fastperiod=12, slowperiod=26, signalperiod=9)[0])
        ta['RSI-normalized'] = talib.RSI(c, timeperiod=14) / np.nanmean(talib.RSI(c, timeperiod=14))
        ta['BBANDS_U-normalized'] = talib.BBANDS(c, timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)[0] / \
                         np.nanmean(talib.BBANDS(c, timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)[0])
        ta['BBANDS_M-normalized'] = talib.BBANDS(c, timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)[1] / \
                         np.nanmean(talib.BBANDS(c, timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)[1])
        ta['BBANDS_L-normalized'] = talib.BBANDS(c, timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)[2] / \
                         np.nanmean(talib.BBANDS(c, timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)[2])
        ta['AD-normalized'] = talib.AD(h, l, c, v) / np.nanmean(talib.AD(h, l, c, v))
        ta['ATR-normalized'] = talib.ATR(h, l, c, timeperiod=14) / np.nanmean(talib.ATR(h, l, c, timeperiod=14))
        ta['HT_DC-normalized'] = talib.HT_DCPERIOD(c) / np.nanmean(talib.HT_DCPERIOD(c))

        # # Plot
        # ta[['Close','MA5','MA10']].plot(figsize=(10,5))
        # plt.show()
        return ta

def bbp(c):
    up, mid, low = talib.BBANDS(c, timeperiod=20, nbdevup=2, nbdevdn=2, matype=0)
    bbp = (c - low) / (up - low)
    return bbp

def candlestickPatternsIndicator(df, trend):
    patternNameList = get_candle_funcs()
    tickerDetectionResult = {}
    
    for patternName in patternNameList:
        patternNameResult = patternNameList[patternName](df.Open, df.High, df.Low, df.Close)

        # Remove all undetected rows (equal to 0)
        filteredPatternNameResultList = patternNameResult[patternNameResult != 0]

        for i in range(len(filteredPatternNameResultList)):
            
            patternInformation = utils.getPatternInformation(patternName, filteredPatternNameResultList[i], trend)
            if (patternInformation):
                # Datetime readable string
                datetimeReadable = utils.getReadableTimestamp(filteredPatternNameResultList.index[i])
                if not datetimeReadable in tickerDetectionResult:
                    tickerDetectionResult[datetimeReadable] = []
                tickerDetectionResult[datetimeReadable].append(patternInformation)

    return tickerDetectionResult

def increasedVolumeBarsIndicator(df, incVolumeBars):
    # n days
    """Dataframe oldest to newest"""
    results = {}
    counter = 0
    # Iterate all rows
    for i in range(len(df)):
        if i+1 < len(df) and df.Volume[i] < df.Volume[i+1]:
            counter += 1
            if counter >= incVolumeBars:
                # save date
                datetimeReadable = utils.getReadableTimestamp(df.index[i+1])
                results[datetimeReadable] = True
        else: counter = 0
    return results