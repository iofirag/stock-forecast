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

def cleanDfNanRows(df):
    deleteIndexes = []
    for i in range(len(df)):
        if np.isnan(df.Open[i]):
            deleteIndexes.append(i)

    return df.drop(df.index[deleteIndexes])

def get10dfRowsFromLast(df):
    return df.tail(statics.maxDays)

def investigateTickerDf(df):
    cleanDf = cleanDfNanRows(df)
    last10dfRows = get10dfRowsFromLast(cleanDf)
    tickerResult = {}
    candlestickPatternsIndicatorRes = candlestickPatternsIndicator(last10dfRows)
    threeDaysincreasedVolumeIndicatorRes = threeDaysincreasedVolumeIndicator(last10dfRows)

    if candlestickPatternsIndicatorRes:
        tickerResult['candlestickPatternsIndicator'] = candlestickPatternsIndicatorRes
    
    if threeDaysincreasedVolumeIndicatorRes:
        tickerResult['threeDaysincreasedVolumeIndicator'] = threeDaysincreasedVolumeIndicatorRes
    return tickerResult

def candlestickPatternsIndicator(df):
    patternNameList = get_candle_funcs()
    tickerDetectionResult = {}
    for patternName in patternNameList:
        patternNameResult = patternNameList[patternName](df.Open, df.High, df.Low, df.Close)

        patternInformation = utils.getPatternInformation(patternName)
        filteredPatternNameResultList = patternNameResult[patternNameResult != 0]

        for i in range(len(filteredPatternNameResultList)):
            datetimeReadable = filteredPatternNameResultList.index[i].strftime('%Y-%m-%d')
            if not datetimeReadable in tickerDetectionResult:
                tickerDetectionResult[datetimeReadable] = []
            
            tickerDetectionResult[datetimeReadable].append({
                'patternName': patternName,
                'patternType': patternInformation.get('patternType', ''),
                'direction': patternInformation.get('direction', ''),
                'reliability': patternInformation.get('reliability', ''),
                'value': filteredPatternNameResultList[i],
            })
    return tickerDetectionResult

def threeDaysincreasedVolumeIndicator(df):
    length = len(df)
    return df.Volume[length-1] > df.Volume[length-2] > df.Volume[length-3]