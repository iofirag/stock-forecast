from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
from itertools import islice
from patternScanner import indentifyCandles
import sys

def fetch():
    try:
        ts = TimeSeries(key='YOUR_API_KEY') # , output_format='pandas'
        # Get json object with the intraday data and another with  the call's metadata
        stock_historical_data, stock_meta_data = ts.get_daily(symbol='TEVA')
        # print(type(stock_historical_data)) 
        last10days = take10First(stock_historical_data.items(), 10)
        # print(last10days)
        indentifyCandles(last10days)
        # pprint(data.head(2))
        # print(isinstance(data, dict)) 
        # for key, value in last10days.items():
        #     print(key, value)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

def take10First(iterable, n):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))

# def get_eod_data2(symbol="AAPL.US", api_token="OeAFFmMliFG5orCUuwAKQ8l4WWFQ67YX", session=None):
#     if session is None:
#         session = requests.Session()
#         url = "https://eodhistoricaldata.com/api/eod/%s" % symbol
#         params = {
#             "api_token": api_token
#         }
#         r = session.get(url, params=params)
#         if r.status_code == requests.codes.ok:
#             df = pd.read_csv(StringIO(r.text), skipfooter=1, parse_dates=[0], index_col=0)
#             return df
#     else:
#         raise Exception(r.status_code, r.reason, url)