from alpha_vantage.timeseries import TimeSeries
from pprint import pprint

def fetch():
    ts = TimeSeries(key='YOUR_API_KEY') # , output_format='pandas'
    # Get json object with the intraday data and another with  the call's metadata
    data, meta_data = ts.get_daily(symbol='TEVA')
    # pprint(data.head(2))
    # print(isinstance(data, dict)) 
    ctr = 0
    for key, value in data.items():
        ctr +=1
        # if ()
        print(key, value)
        # lastTenDays = 

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