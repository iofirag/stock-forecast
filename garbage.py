
# print(talib.CDLDOJI(o,h,l,c))

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
