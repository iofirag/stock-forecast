from statics import candleStickSwitcher, fetchDefaultOptions, shortTermOptions, mediumTermOptions, longTermOptions
import numpy as np

def getPatternInformation(patternName, value, trend):
  detectedFunction = candleStickSwitcher.get(patternName, lambda _value,_trend: {'error': f'missing pattern={patternName} with value={_value} in trend={_trend}'})
  patternInformation = detectedFunction(value, trend)

  # confirmation
  # there are more reasons this pattern can be confirm like trend
  # trend
  if (value > 100 or value < -100):
      patternInformation['confirmedBar'] = True

  return {**patternInformation, **{
    'patternName': patternName,
    'value': value
  }}

def getShortTermOptions():
  return dict(fetchDefaultOptions, **shortTermOptions)

def getMediumTermOptions():
  return dict(fetchDefaultOptions, **mediumTermOptions)

def getLongTermOptions():
  return dict(fetchDefaultOptions, **longTermOptions)

def convert(o):
    if isinstance(o, np.generic): return np.asscalar(o)
    raise TypeError

def cleanDf(df):
    # Remove 'Adj Close' column
    if 'Adj Close' in df.columns:
        df = df.drop('Adj Close', axis=1)  # axis=1 for columns

    return df.dropna()  # clean df rows from nan values

def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance

def identifyTrend(open, high, low, close, volume):
  pass




































