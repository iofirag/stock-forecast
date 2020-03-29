from statics import candleStickSwitcher, fetchDefaultOptions, shortTermOptions, mediumTermOptions, longTermOptions
import numpy as np

def getPatternInformation(patternName):
  return candleStickSwitcher.get(patternName, lambda: {'direction': 'Invalid pattern', 'reliability': 'Invalid pattern'})()

def getShortTermOptions():
  return dict(fetchDefaultOptions, **shortTermOptions)

def getMediumTermOptions():
  return dict(fetchDefaultOptions, **mediumTermOptions)

def getLongTermOptions():
  return dict(fetchDefaultOptions, **longTermOptions)

def convert(o):
    if isinstance(o, np.int32): return int(o)
    if isinstance(o, np.bool_): return bool(o)
    raise TypeError



















































