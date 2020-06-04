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
            # showPlot(tickerInvestigationData['ta'])
            if tickerInvestigationData:
                results['alerts'][ticker] = tickerInvestigationData


        return results

    except ValueError:
        print("Unexpected error:", sys.exc_info()[0])
        raise

def showPlot(tickerInvestigationData):
    # Plot
    plot = pd.DataFrame()
    plot['Close'] = tickerInvestigationData['Close']
    plot['MA5'] = tickerInvestigationData['MA5']
    plot['MA10'] = tickerInvestigationData['MA10']
    plot[['Close','MA5','MA10']].plot(figsize=(10,5))
    plt.show()

def investigateTickerDf(df):
    cleanDf = utils.cleanDf(df)
    
    tickerResult = {}
   
    # more indicators:
    # momentum indicator (RSI)
    # momentumIndicatorRes = momentumIndicator(cleanDf)
    ta = utils.technicalIndicatorsDf(cleanDf)

    # trend = utils.identifyTrend(df.Open, df.High, df.Low, df.Close, df.Volume)
    trend = utils.identifyTrend(ta, cleanDf)
    # ta.to_json(r'ta-data.json')
    ##################################
    # set results:
    ##################################
    return {
        'ta': ta,
        # 'momentumIndicator': momentumIndicatorRes,
        'candlestickPatternsIndicator': candlestickPatternsIndicator(cleanDf, trend),       # candlestick patterns indicators
        # 'customIndicators': customIndicators(cleanDf, trend, ta)
        # f'{statics.indicatorsConfigurations["increasedVolumeIndicator"]["timeperiod"]}DaysIncreasedVolumeIndicator': increasedVolumeBarsIndicator(cleanDf, statics.indicatorsConfigurations["increasedVolumeIndicator"]["timeperiod"]),    # 3 days increased volume indicator
    }

def customIndicators(df, trend, ta):
    # n days
    """Dataframe oldest to newest"""
    results = {}
    # Iterate all rows
    for i in range(len(df)):
        pass
        # results['increasedVolume'] = increasedVolumeBarsIndicator(df[i], statics.indicatorsConfigurations["increasedVolumeIndicator"]["timeperiod"], results['increasedVolume'])

    return results

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

def increasedVolumeBarsIndicator(df, incVolumeBars, pastResults):
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