from statics import candleStickSwitcher, fetchDefaultOptions, shortTermOptions, mediumTermOptions, longTermOptions
import numpy as np
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
  for criteria in patternInformation.acceptableValues():
    if (criteria.low < value and value < criteria.high and criteria.currentTrend == currentTrend) \
      or criteria.predictedTrend == statics.PatternSignal.Indecision:
      # Build result object
      criteria['value'] = value
      if not 'reliability' in criteria or criteria['reliability']:
        criteria['reliability'] = patternInformation.reliability
      if not 'description' in criteria or criteria['description']:
        criteria['description'] = patternInformation.description

      # result['patternType']: statics.PatternType(criteria.patternType).name # criteria.patternType
      # criteria['sourceCode'] = f'https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_${patternName}.c#l239'
      return criteria
      # break
      # patternInformation[]

  return {}
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
    raise TypeError

def cleanDf(df):
    # Remove 'Adj Close' column
    if 'Adj Close' in df.columns:
        df = df.drop('Adj Close', axis=1)  # axis=1 for columns

    return df.dropna()  # clean df rows from nan values

def calculateRSI(df, array=False):
  rsiList = talib.RSI(df.Close.values, statics.indicatorsConfigurations['rsi']['timeperiod'])
  rsiResult = {}
  if array:
    for i in range(len(df)):
      rsiResult[getReadableTimestamp(df.index[i])] = getRsiTranslationObj(rsiList[i])

  else:
    rsiResult[getReadableTimestamp(df.index[-1])] = getRsiTranslationObj(rsiList[-1])

  return rsiResult

def getRsiTranslationObj(value):
  trend = statics.TrendType.Indecision.name
  if value <= 30 and value >= 0: trend = statics.TrendType.Uptrend.name
  elif value <= 100 and value >= 70: trend = statics.TrendType.Downtrend.name
  # else: trend = statics.TrendType.Indecision.name

  return {
    'trend': trend,
    'value': value,
  }

def identifyTrend(open, high, low, close, volume):
  pass

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

























