from patternScanner import get_candle_funcs
import yfinance as yf
from config import ticker_list, period_days
import numpy as np
import utils

def fetchData():
    try:
        data = yf.download(  # or pdr.get_data_yahoo(...
            # tickers list or string as well
            tickers = str(' '.join(ticker_list)),

            # start="2020-03-01", end="2020-03-04",
            # use "period" instead of start/end
            # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
            # (optional, default is '1mo')
            period = f"{period_days}d",

            # fetch data by interval (including intraday if period < 60 days)
            # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
            # (optional, default is '1d')
            interval = "1d",

            # group by ticker (to access via data['SPY'])
            # (optional, default is 'column')
            group_by = 'ticker',

            # adjust all OHLC automatically
            # (optional, default is False)
            auto_adjust = True,

            # download pre/post regular market hours data
            # (optional, default is False)
            prepost = False,

            # use threads for mass downloading? (True/False/Integer)
            # (optional, default is True)
            threads = True,

            # proxy URL scheme use use when downloading?
            # (optional, default is None)
            proxy = None
        )
        
        results = {}
        for ticker in ticker_list:
            print('\n' + ticker + ':')
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


def investigateTickerDf(df):
    cleanData = cleanDfNanRows(df)
    tickerResult = {}
    candlestickPatternsIndicatorRes = candlestickPatternsIndicator(df)
    threeDaysincreasedVolumeIndicatorRes = threeDaysincreasedVolumeIndicator(df)

    if candlestickPatternsIndicatorRes:
        tickerResult['candlestickPatternsIndicator'] = candlestickPatternsIndicatorRes
    
    if threeDaysincreasedVolumeIndicatorRes:
        tickerResult['threeDaysincreasedVolumeIndicator'] = threeDaysincreasedVolumeIndicatorRes
    return tickerResult

def candlestickPatternsIndicator(df):
    function_list = get_candle_funcs()
    tickerDetectionList = {}
    for pattern_detection in function_list:
        pattern_detection_result = function_list[pattern_detection](df.Open, df.High, df.Low, df.Close)
        # print(pattern_detection_result)
        if pattern_detection_result[-1] > 0 or True:
            print(pattern_detection)
            patternInformation = utils.getPatternInformation(pattern_detection)
            tickerDetectionList[pattern_detection] = {
                'direction': patternInformation.get('direction', ''),
                'reliability': patternInformation.get('reliability', ''),
            }
    return tickerDetectionList

def threeDaysincreasedVolumeIndicator(df):
    length = len(df)
    return df.Volume[length-1] > df.Volume[length-2] > df.Volume[length-3]