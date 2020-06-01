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
    if (criteria['low'] <= value and value <= criteria['high'] and criteria['currentTrend'] == currentTrend) \
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

  if(ta['RSI'][-1] > 70 and ta['BBP'][-1] > 1):
    print(statics.TrendType.Downtrend)
    return statics.TrendType.Downtrend
  elif(ta['RSI'][-1] < 30 and ta['BBP'][-1] < 0):
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

























