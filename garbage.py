# https://github.com/iofirag/bill-duck

# def cleanDfNanRows(df):
#     deleteIndexes = []
#     for i in range(len(df)):
#         if np.isnan(df.Open[i]):
#             deleteIndexes.append(i)

#     return df.drop(df.index[deleteIndexes])

# def get10dfRowsFromLast(df):
#     return df.tail(statics.maxDays)

################################################
# build new list from O|H|C|L where data is not NaN
            # openList = [i for i in data[ticker].Open if not np.isnan(i)]
            # data[ticker].High = [i for i in data[ticker].High if not i == 'NaN']
            # data[ticker].Low = [i for i in data[ticker].Low if not i == 'NaN']
            # data[ticker].Close = [i for i in data[ticker].Close if not i == 'NaN']
            # data[ticker].Volume = [i for i in data[ticker].Volume if not i == 'NaN']
            # print(data[ticker].Open[-1])
            # index = 9
            # dfData = {}
            # while index >= 0:
            #     dfData[ticker] = {

            #     }
            #     dfData[ticker].index
            # print(type(data))
            
            # data[ticker, 'indux'] = list(range(len(data[ticker].index))) # work!

            # tickerDf = data[ticker]
            # tickerDf.drop(tickerData.index[i])
            # print(np.isnan( (data[ticker].loc['2020-03-20', : ].Open) ))

            # print (data[ticker].loc[ np.isnan(data[ticker].Open) ])
            # print (data[ticker].drop(np.isnan(data[ticker].Open)))

            #     # for i in range(period_days):
            #         print(data[ticker])
            #         # print(f'Open - {data[ticker].Open[i]:f}')
            #         # print(f'High - {data[ticker].High[i]:f}')
            #         # print(f'Low - {data[ticker].Low[i]:f}')
            #         # print(f'Close - {data[ticker].Close[i]:f}')
            #         # print(f'Volume - {data[ticker].Volume[i]:.0f}')
            #         # print('--------------------')

                    # data[ticker] = tickerData
                    # data[ticker] = tickerData
                    # data[ticker].drop( data[ticker].index[i], inplace=True)
                
                # print(data[ticker][data[ticker].index[i]])
                # print(data[ticker][data[ticker].index])
                    # dateKey = str(data[ticker].index[i]).split(' ')[0]
                    # print(dateKey)

            #         key = data[ticker].index[i]
            #         # print(data[ticker].loc[key, : ])
            #         # print(data[ticker].iloc[i, : ])
                    
            #         data[ticker].drop(key, inplace=True)
            #         # tickerData = data[ticker]
            #         # print(tickerData)

###################################################
            # print('')
            # print('results:',results)

            # df = data[ticker].Open
            # candle_list = df.values.tolist()
            # print (candle_list)
        # ts = TimeSeries(key='0LYQQSYMZAYEZLJP', indexing_type='integer') # , output_format='pandas'
        # # # Get json object with the intraday data and another with  the call's metadata
        # data, meta_data = ts.get_daily(symbol='TEVA', outputsize='compact')
        # # help(ts.get_daily)
        # print(data) 
        # last10days = take10First(stock_historical_data.items(), 10)
        # # print(last10days)
        # indentifyCandles(last10days)
        # # pprint(data.head(2))
        # # print(isinstance(data, dict)) 
        # # for key, value in last10days.items():
        # #     print(key, value)

# print(talib.CDLDOJI(o,h,l,c))

#######################################################
# def take10First(iterable, n):
#     "Return first n items of the iterable as a list"
#     return list(islice(iterable, n))

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
##############################################################################
# def get_candle_funcs():  
#     funcs = {}  
#     for name in talib.get_functions():  
#         if name.startswith('CDL'):  
#             funcs[name] = getattr(talib, name)  
#     return funcs

# O = np.asarray([30.10])
# H = np.asarray([32.10])
# L = np.asarray([31.10])
# C = np.asarray([31.10])

# funcs = get_candle_funcs()

# results = {}  
# for f in funcs:  
#     res = funcs[f](O, H, L, C)
#     print (res)
#     if res > 0:
#         results[f] = res

# print(results)

# input = {
#   open: [21.65,21.48,21.25],
#   high: [21.82,21.57,21.35],
#   close: [21.32,21.10,20.70],
#   low: [21.25,20.97,20.60]
# }
# print('')

# print(talib.CDLDOJI(o,h,l,c))
########################################################################

#########################################################################
# from random import randint

# inputs = []

# for i in range(3):
#     candleStick = {
#         'open': randint(0, 9),
#         'high': randint(0, 9),
#         'low': randint(0, 9),
#         'close': randint(0, 9),
#         'volume': randint(0, 9)
#     }
#     inputs.append(candleStick)
# else:
#     print('Final x = %d' % (i))

# # print(talib.get_functions())
print(len( talib.get_function_groups()['Pattern Recognition']))

#########################################################################



# Continuation Patterns
# --------------------
# Reversal Patterns
# ----------------
# CDL2CROWS Two Crows
# CDL3BLACKCROWS Three Black Crows
# CDL3INSIDE Three Inside Up/Down
# CDL3LINESTRIKE Three-Line Strike
# CDL3OUTSIDE Three Outside Up/Down
# CDL3STARSINSOUTH Three Stars In The South
# CDL3WHITESOLDIERS Three Advancing White Soldiers
# CDLABANDONEDBABY Abandoned Baby
# CDLADVANCEBLOCK Advance Block
# CDLBELTHOLD Belt-hold
# CDLBREAKAWAY Breakaway
# CDLCLOSINGMARUBOZU Closing Marubozu
# CDLCONCEALBABYSWALL Concealing Baby Swallow
# CDLCOUNTERATTACK Counterattack
# CDLDARKCLOUDCOVER Dark Cloud Cover
# CDLDOJI Doji
# CDLDOJISTAR Doji Star
# CDLDRAGONFLYDOJI Dragonfly Doji
# CDLENGULFING Engulfing Pattern
# CDLEVENINGDOJISTAR Evening Doji Star
# CDLEVENINGSTAR Evening Star
# CDLGAPSIDESIDEWHITE Up/Down-gap side-by-side white lines
# CDLGRAVESTONEDOJI Gravestone Doji
# CDLHAMMER Hammer
# CDLHANGINGMAN Hanging Man
# CDLHARAMI Harami Pattern
# CDLHARAMICROSS Harami Cross Pattern
# CDLHIGHWAVE High-Wave Candle
# CDLHIKKAKE Hikkake Pattern
# CDLHIKKAKEMOD Modified Hikkake Pattern
# CDLHOMINGPIGEON Homing Pigeon
# CDLIDENTICAL3CROWS Identical Three Crows
# CDLINNECK In-Neck Pattern
# CDLINVERTEDHAMMER Inverted Hammer
# CDLKICKING Kicking
# CDLKICKINGBYLENGTH Kicking - bull/bear determined by the longer marubozu
# CDLLADDERBOTTOM Ladder Bottom
# CDLLONGLEGGEDDOJI Long Legged Doji
# CDLLONGLINE Long Line Candle
# CDLMARUBOZU Marubozu
# CDLMATCHINGLOW Matching Low
# CDLMATHOLD Mat Hold
# CDLMORNINGDOJISTAR Morning Doji Star
# CDLMORNINGSTAR Morning Star
# CDLONNECK On-Neck Pattern
# CDLPIERCING Piercing Pattern
# CDLRICKSHAWMAN Rickshaw Man
# CDLRISEFALL3METHODS Rising/Falling Three Methods
# CDLSEPARATINGLINES Separating Lines
# CDLSHOOTINGSTAR Shooting Star
# CDLSHORTLINE Short Line Candle
# CDLSPINNINGTOP Spinning Top
# CDLSTALLEDPATTERN Stalled Pattern
# CDLSTICKSANDWICH Stick Sandwich
# CDLTAKURI Takuri (Dragonfly Doji with very long lower shadow)
# CDLTASUKIGAP Tasuki Gap
# CDLTHRUSTING Thrusting Pattern
# CDLTRISTAR Tristar Pattern
# CDLUNIQUE3RIVER Unique 3 River
# CDLUPSIDEGAP2CROWS Upside Gap Two Crows
# CDLXSIDEGAP3METHODS Upside/Downside Gap Three Method


# if trendExist:
  #                 datetimeReadable = utils.getReadableTimestamp(df.index[targetDayIndex])
#                 if not datetimeReadable in results:
#                     results[datetimeReadable] = []

#                 results[datetimeReadable].append(True)