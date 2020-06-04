from statics import candleStickSwitcher, fetchDefaultOptions, shortTermOptions, mediumTermOptions, longTermOptions
import numpy as np
import pandas as pd
import talib
import statics

def getPatternInformation(patternName, value, currentTrend):
  detectedFunction = candleStickSwitcher.get(patternName, lambda _value,_currentTrend: {'error': f'missing pattern={patternName} with value={_value} in currentTrend={_currentTrend}'})
  patternInformation = detectedFunction(value, currentTrend)

  # confirmation
  # there are more reasons this pattern can be confirm like trend
  # trend
  # if (value > 100 or value < -100):
  #     patternInformation['hasConfirmedBar'] = True
  # result = {}

  for criteria in patternInformation['acceptableValues']:
    # and criteria['currentTrend'] == currentTrend
    if (criteria['low'] <= value and value <= criteria['high'] ) \
      or criteria['predictedTrend'] == statics.PatternSignal.Indecision:
        # or criteria['predictedTrend'] == statics.PatternSignal.Bullish:
      # Build result object
      criteria['value'] = value
      if not 'reliability' in criteria or not criteria['reliability']:
        criteria['reliability'] = patternInformation['reliability']
      if not 'description' in criteria or not criteria['description']:
        criteria['description'] = patternInformation['description']

      output = {**patternInformation, **criteria, **{
        'patternName': patternName,
        'value': value
      }}

      # clean output
      output.pop('acceptableValues', None)
      output.pop('high', None)
      output.pop('low', None)
      if ('img' in output and not output['img']):
        output.pop('img', None)
      if ('reliability' in output and output['reliability'] == 'N'):
        output.pop('reliability', None)
      # del output['acceptableValues']
      return output

      # result['patternType']: statics.PatternType(criteria.patternType).name # criteria.patternType
      # criteria['sourceCode'] = f'https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_${patternName}.c#l239'
      # return criteria
      # break
      # patternInformation[]
  # else:
    # print(f'{criteria} missing')

  # return {}
  # return {**patternInformation, **{
  #   'patternName': patternName,
  #   'value': value
  # }}

def getShortTermOptions():
  return dict(fetchDefaultOptions, **shortTermOptions)

def getMediumTermOptions():
  return dict(fetchDefaultOptions, **mediumTermOptions)

def getLongTermOptions():
  return dict(fetchDefaultOptions, **longTermOptions)

def convert(o):
    if isinstance(o, np.generic): return np.asscalar(o)
    elif isinstance(o, np.ndarray): return o.tolist()
    elif isinstance(o, statics.Enum): return o.name
    elif isinstance(o, statics.PatternType): return o
    return o
    # raise TypeError

def cleanDf(df):
    # Remove 'Adj Close' column
    if 'Adj Close' in df.columns:
        df = df.drop('Adj Close', axis=1)  # axis=1 for columns

    return df.dropna()  # clean df rows from nan values

# def calculateRSI(df, array=False):
#   rsiList = talib.RSI(df.Close.values, statics.indicatorsConfigurations['rsi']['timeperiod'])
#   rsiResult = {}
#   if array:
#     for i in range(len(df)):
#       rsiResult[getReadableTimestamp(df.index[i])] = getRsiTranslationObj(rsiList[i])

#   else:
#     rsiResult[getReadableTimestamp(df.index[-1])] = getRsiTranslationObj(rsiList[-1])

#   return rsiResult

# def getRsiTranslationObj(value):
#   trend = statics.TrendType.Indecision.name
#   if value <= 30 and value >= 0: trend = statics.TrendType.Uptrend.name
#   elif value <= 100 and value >= 70: trend = statics.TrendType.Downtrend.name
#   else: trend = statics.TrendType.Indecision.name

#   return {
#     'trend': trend,
#     'value': value,
#   }

# def identifyTrend(open, high, low, close, volume):
def identifyTrend(ta, df):
  # print("RSI (first 10 elements)\n", ta['RSI'][14:24])
  # holdings = pd.DataFrame(index=df.index, data={'Holdings': np.array([np.nan] * df.shape[0])})
  # df.loc[((ta['RSI'] < 30) & (ta['BBP'] < 0)), 'Holdings'] = 100
  # df.loc[((ta['RSI'] > 70) & (ta['BBP'] > 1)), 'Holdings'] = 0
  #Simple Moving Average
  # df['SMA'] = talib.SMA(df.Close, timeperiod = 20)
  # # Exponential Moving Average
  # df['EMA'] = talib.EMA(df.Close, timeperiod = 20)
  # # Plot
  # df[['Close','SMA','EMA']].plot(figsize=(10,5))
  # plt.show()

  if(ta['RSI'][-1] >= 70 and ta['BBP'][-1] > 1):
    print(statics.TrendType.Downtrend)
    return statics.TrendType.Downtrend
  elif(ta['RSI'][-1] <= 30 and ta['BBP'][-1] < 0):
    print(statics.TrendType.Uptrend)
    return statics.TrendType.Uptrend
  else: 
    return statics.TrendType.Indecision
  

  # holdings.ffill(inplace=True)
  # holdings.fillna(0, inplace=True)
  # holdings['Order'] = holdings.diff()
  # holdings.dropna(inplace=True)

  # if (True): statics.TrendType.Downtrend
  # else: currentTrend = statics.TrendType.Uptrend

def getReadableTimestamp(ts):
  return ts.strftime('%Y-%m-%d')
  
# def calculateRSI(closeValuesList, timeperiod=14, array=False):
#   rsiList = talib.RSI(df.Close.values, statics.indicatorsConfigurations['RSI']['timeperiod'])
#   rsiResult = {}
#   for i in range(len(df)):
#       rsiResult[utils.getReadableTimestamp(df.index[i])] = {
#           'trend': statics.TrendType.Uptrend.name if rsiList[i] <= 30 and rsiList[i] >= 0 else (statics.TrendType.Downtrend.name if rsiList[i] >= 70 and rsiList[i] <=0 else statics.TrendType.Indecision.name),
#           'value': rsiList[i],
#       }
#   return rsiResult
  
#     resultList = talib.RSI(closeValuesList, timeperiod)
#     if array:
#         return resultList

#     return resultList[-1]

# def singleton(class_):
#     instances = {}
#     def getinstance(*args, **kwargs):
#         if class_ not in instances:
#             instances[class_] = class_(*args, **kwargs)
#         return instances[class_]
#     return getinstance


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
        return ta

def bbp(c):
    up, mid, low = talib.BBANDS(c, timeperiod=20, nbdevup=2, nbdevdn=2, matype=0)
    bbp = (c - low) / (up - low)
    return bbp






















