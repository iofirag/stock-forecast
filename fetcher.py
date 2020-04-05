from patternScanner import get_candle_funcs
import yfinance as yf
import numpy as np
import utils
import statics

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
        
        results = {}
        for ticker in tickerList:
            tickerInvestigationData = investigateTickerDf(data[ticker])
            if tickerInvestigationData:
                results[ticker] = tickerInvestigationData

        return results

    except ValueError:
        print("Unexpected error:", sys.exc_info()[0])
        raise



def investigateTickerDf(df):
    cleanDf = utils.cleanDf(df)
    trend = utils.identifyTrend(df.Open, df.High, df.Low, df.Close, df.Volume)
    
    tickerResult = {}
    # more indicators:
    # http://tutorials.topstockresearch.com/candlestick/Bearish/DarkCloudCover/TutotrialOnDarkCloudCoverChartPattern.html
    candlestickPatternsIndicatorRes = candlestickPatternsIndicator(cleanDf, trend)
    threeDaysincreasedVolumeIndicatorRes = threeDaysincreasedVolumeIndicator(cleanDf)

    if candlestickPatternsIndicatorRes:
        tickerResult['candlestickPatternsIndicator'] = candlestickPatternsIndicatorRes
    
    if threeDaysincreasedVolumeIndicatorRes:
        tickerResult['threeDaysincreasedVolumeIndicator'] = threeDaysincreasedVolumeIndicatorRes
    return tickerResult

def candlestickPatternsIndicator(df, trend):
    patternNameList = get_candle_funcs()
    tickerDetectionResult = {}
    
    for patternName in patternNameList:
        patternNameResult = patternNameList[patternName](df.Open, df.High, df.Low, df.Close)

        # Remove all undetected rows (equal to 0)
        filteredPatternNameResultList = patternNameResult[patternNameResult != 0]

        for i in range(len(filteredPatternNameResultList)):
            # Datetime readable string
            datetimeReadable = filteredPatternNameResultList.index[i].strftime('%Y-%m-%d')
            if not datetimeReadable in tickerDetectionResult:
                tickerDetectionResult[datetimeReadable] = []
            
            patternInformation = utils.getPatternInformation(patternName, filteredPatternNameResultList[i], trend)
            tickerDetectionResult[datetimeReadable].append(patternInformation)

    return tickerDetectionResult

def threeDaysincreasedVolumeIndicator(df):
    length = len(df)
    return df.Volume[length-1] > df.Volume[length-2] > df.Volume[length-3]