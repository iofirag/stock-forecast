from fetcher import fetchData
from statics import tickerList
import utils

def investigateTickers():
  tickersResult = {
    'shortTermResult': fetchData(tickerList, utils.getShortTermOptions()),
    'mediumTermResult': fetchData(tickerList, utils.getMediumTermOptions()),
    'longTermResult': fetchData(tickerList, utils.getLongTermOptions())
  }
  return tickersResult