from fetcher import fetchData
from config import tickerList, fetchOptions

def investigateTickers():
  tickersResult = fetchData(tickerList, '10d', '1d', fetchOptions)
  return tickersResult