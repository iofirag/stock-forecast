from enum import Enum 

tickerList = ['BEZQ.TA', 'DSCT.TA']
# tickerList = ['SPY','MSFT','GOOGL','TEVA','BEZQ.TA']

# /* Proceed with the calculation for the requested range.
#     * Must have:
#     * - first candle: long white candle
#     * - second candle: black real body
#     * - gap between the first and the second candle's real bodies
#     * - third candle: black candle that opens within the second real body and closes within the first real body
#     * The meaning of "long" is specified with TA_SetCandleSettings
#     * outInteger is negative (-1 to -100): two crows is always bearish; 
#     * the user should consider that two crows is significant when it appears in an uptrend, while this function 
#     * does not consider the trend
#     */
# def CDL2CROWS(value):
#   return { # CDL2CROWS
#     'patternType': PatternType.Reversal.name,
#     'JapaneseName': 'niwa garasu',
#     'patternSignal': (lambda: patternSignal.Bearish.name if value < 0 else patternSignal.Bullish.name)(), 
#     'reliability': '>',
#     'value': value,
#     'link': 'https://www.candlescanner.com/wp-content/uploads/2015/08/two-crows1.png'
#   },

# /* Proceed with the calculation for the requested range.
  #   * Must have:
  #   * - first candle: long white (black) real body
  #   * - second candle: short real body totally engulfed by the first
  #   * - third candle: black (white) candle that closes lower (higher) than the first candle's open
  #   * The meaning of "short" and "long" is specified with TA_SetCandleSettings
  #   * outInteger is positive (1 to 100) for the three inside up or negative (-1 to -100) for the three inside down; 
  #   * the user should consider that a three inside up is significant when it appears in a downtrend and a three inside
  #   * down is significant when it appears in an uptrend, while this function does not consider the trend
  #   */
# def CDL3BLACKCROWS(value):
#   return {
#     'patternType': '?',
#     'patternSignal': '<', 
#     'reliability': '>',
#     'value': value
#   }
# def CDL3INSIDE(value):
#   return {
#     'patternType': '?',
#     'patternSignal': '<', 
#     'reliability': '>',
#     'value': value
#   }
# def CDL3LINESTRIKE(value):
#   return {
#     'patternType': '?',
#     'patternSignal': '<', 
#     'reliability': '>',
#     'value': value
#   }
# def CDL3OUTSIDE(value):
#   return {
#     'patternType': '?',
#     'patternSignal': '<', 
#     'reliability': '>',
#     'value': value
#   }

# https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/
# https://mrjbq7.github.io/ta-lib/func_groups/pattern_recognition.html
candleStickSwitcher = {
  
  # /* Proceed with the calculation for the requested range.
#     * Must have:
#     * - first candle: long white candle
#     * - second candle: black real body
#     * - gap between the first and the second candle's real bodies
#     * - third candle: black candle that opens within the second real body and closes within the first real body
#     * The meaning of "long" is specified with TA_SetCandleSettings
#     * outInteger is negative (-1 to -100): two crows is always bearish; 
#     * the user should consider that two crows is significant when it appears in an uptrend, while this function 
#     * does not consider the trend
#     */
      # (lambda _value: PatternSignal.Bearish.name if _value < 0 else PatternSignal.Bullish.name)(value),
  # 'CDL2CROWS': CDL2CROWS,
  'CDL2CROWS': lambda value,trend: { # CDL2CROWS
    'patternType': PatternType.Reversal.name,
    'JapaneseName': 'niwa garasu',
    'patternSignal': PatternSignal.Bearish.name if value < 0 else PatternSignal.Bullish.name, 
    'reliability': PatternReliability.Medium.name,
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': 'https://www.candlescanner.com/wp-content/uploads/2015/08/two-crows1.png',
    'ta-lib-description': """outInteger is negative (-1 to -100): three black crows is always bearish.
      the user should consider that 3 black crows is significant when it appears after 
      a mature advance or at high levels""",
    'quantshare-description': 'Two Crows, The Two Crows Pattern is a 3-day pattern.',
    'quantshare-info': """Signal: Bearish
      Pattern: Reversal
      Reliability: Medium
      During an uptrend we see the market closing lower after an opening gap. Then we see 
      a black day that fills the gap creating the Bearish Two Crows Pattern. It suggests 
      the erosion of the uptrend, and warns about a possible trend reversal.""",
  },

  # /* Proceed with the calculation for the requested range.
  #   * Must have:
  #   * - three consecutive and declining black candlesticks
  #   * - each candle must have no or very short lower shadow
  #   * - each candle after the first must open within the prior candle's real body
  #   * - the first candle's close should be under the prior white candle's high
  #   * The meaning of "very short" is specified with TA_SetCandleSettings
  #   * outInteger is negative (-1 to -100): three black crows is always bearish; 
  #   * the user should consider that 3 black crows is significant when it appears after a mature advance or at high levels, 
  #   * while this function does not consider it
  #   */
  ## high. reversal. 78% bearish
  # 'CDL3BLACKCROWS': CDL3BLACKCROWS,
  'CDL3BLACKCROWS': lambda value,trend: {
    'patternType': PatternType.Reversal.name,
    'JapaneseName': 'niwa garasu',
    'patternSignal': PatternSignal.Bearish.name if value < 0 else PatternSignal.Bullish.name, 
    'reliability': PatternReliability.High.name,
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': '',
    'ta-lib-description': """outInteger is negative (-1 to -100): three black crows is always bearish; 
      the user should consider that 3 black crows is significant when it appears after a mature advance or at high levels, 
      while this function does not consider it""",
    'quantshare-description': """Three Black Crows, The Three Black Crows got their name 
      from the resemblance of three crows looking down from their perch from a tree.""",
    'quantshare-info': """Signal: Bearish
      Pattern: reversal
      Reliability: high
      Three long black days with each successive open being within the body of the previous day 
      and each successive close being below the previous day's and near the day's low.""",
  },
  
  # /* Proceed with the calculation for the requested range.
  #   * Must have:
  #   * - first candle: long white (black) real body
  #   * - second candle: short real body totally engulfed by the first
  #   * - third candle: black (white) candle that closes lower (higher) than the first candle's open
  #   * The meaning of "short" and "long" is specified with TA_SetCandleSettings
  #   * outInteger is positive (1 to 100) for the three inside up or negative (-1 to -100) for the three inside down; 
  #   * the user should consider that a three inside up is significant when it appears in a downtrend and a three inside
  #   * down is significant when it appears in an uptrend, while this function does not consider the trend
  #   */
  # 'CDL3INSIDE': CDL3INSIDE,
  'CDL3INSIDE': lambda value,trend: {
    'patternType': PatternType.Reversal.name,
    'patternSignal': PatternSignal.Bullish.name if value > 0 else PatternSignal.Bearish.name if value < 0 else PatternSignal.N.name,
    'reliability': PatternReliability.Medium.name,
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': 'https://bpcdn.co/images/2016/05/grade2-three-inside.png',
    'ta-lib-description': """* outInteger is positive (1 to 100) for the three inside up 
      or negative (-1 to -100) for the three inside down;
      the user should consider that a three inside up is significant when it appears in a downtrend and a three inside
      down is significant when it appears in an uptrend, while this function does not consider the trend""",
    'quantshare-description': """Three Inside Up/Down, Note that after the long candle day that is in the 
      same direction of the trend that the Harami pattern occurs.""",
  },

  # /* Proceed with the calculation for the requested range.
  #   * Must have:
  #   * - three white soldiers (three black crows): three white (black) candlesticks with consecutively higher (lower) closes,
  #   * each opening within or near the previous real body
  #   * - fourth candle: black (white) candle that opens above (below) prior candle's close and closes below (above) 
  #   * the first candle's open
  #   * The meaning of "near" is specified with TA_SetCandleSettings;
  #   * outInteger is positive (1 to 100) when bullish or negative (-1 to -100) when bearish;
  #   * the user should consider that 3-line strike is significant when it appears in a trend in the same direction of
  #   * the first three candles, while this function does not consider it
  #   */
  ## high. reversal. 84% bullish. 65% bearish
  # 'CDL3LINESTRIKE': CDL3LINESTRIKE,
  'CDL3LINESTRIKE': lambda value,trend: {
    'patternType': PatternType.Continuation.name,
    'patternSignal': PatternSignal.Bullish.name if value > 0 else PatternSignal.Bearish.name if value < 0 else PatternSignal.N.name,
    'reliability': PatternReliability.Low.name,
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': '',
    'ta-lib-description': """outInteger is positive (1 to 100) when bullish or negative (-1 to -100) when bearish;
      the user should consider that 3-line strike is significant when it appears in a trend in the same direction of
      the first three candles, while this function does not consider it""",
    'quantshare-description': """""",
    'quantshare-info': """""",
  },
  
  # 'CDL3OUTSIDE': CDL3OUTSIDE,
  'CDL3OUTSIDE': lambda value,trend: {
    'patternType': PatternType.N.name,
    'patternSignal': PatternSignal.N.name if True else False,
    'reliability': PatternReliability.N.name,
    'value': value,
    'link': '',
    'ta-lib-description': """""",
    'quantshare-description': """""",
    'quantshare-info': """""",
  },

  'CDL3STARSINSOUTH': lambda value,trend: {
    'patternType': PatternType.N,
    'patternSignal': PatternSignal.N.name if True else False,
    'reliability': PatternReliability.N.name,
    'value': value,
    'link': '',
    'ta-lib-description': """""",
    'quantshare-description': """""",
    'quantshare-info': """""",
  },
  'CDL3WHITESOLDIERS': lambda value,trend: {
    'patternType': PatternType.N,
    'patternSignal': PatternSignal.N.name if True else False,
    'reliability': PatternReliability.N.name,
    'value': value,
    'link': '',
    'ta-lib-description': """""",
    'quantshare-description': """""",
    'quantshare-info': """""",
  },

  ## high. reversal. 70% bullish
  'CDLABANDONEDBABY': lambda value,trend: {'patternType': '?', 'patternSignal': '<', 'reliability': '>'},
  
  'CDLADVANCEBLOCK': lambda  value,trend: {'patternType': '?', 'patternSignal': '<', 'reliability': '>'},
  'CDLBELTHOLD': lambda  value,trend: {'patternType': '?', 'patternSignal': '<', 'reliability': '>'},

  ## high. reversal. 63% bearish
  'CDLBREAKAWAY': lambda  value,trend: {'patternType': '?', 'patternSignal': '<', 'reliability': '>'},
  
  'CDLCLOSINGMARUBOZU': lambda  value,trend: {'patternType': '?', 'patternSignal': '<', 'reliability': '>'},
  'CDLCONCEALBABYSWALL': lambda  value,trend: {'patternType': '?', 'patternSignal': '<', 'reliability': '>'},
  'CDLCOUNTERATTACK': lambda  value,trend: {'patternType': '?', 'patternSignal': '<', 'reliability': '>'},
  'CDLDARKCLOUDCOVER': lambda  value,trend: {'patternType': '?', 'patternSignal': '<', 'reliability': '>'},
  'CDLDOJI': lambda  value,trend: {'patternType': '?', 'patternSignal': '<', 'reliability': '>'},
  'CDLDOJISTAR': lambda  value,trend: {'patternType': 'reversal pattern', 'patternSignal': '<', 'reliability': 'medium'}, # V
  'CDLDRAGONFLYDOJI': lambda  value,trend: {'patternType': '?', 'patternSignal': '<', 'reliability': '>'}, # not high
  'CDLENGULFING': lambda  value,trend: {'patternType': '?', 'patternSignal': '<', 'reliability': '>'}, # https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDLENGULFING.c#l212 * outInteger is positive (1 to 100) when < or negative (-1 to -100) when bearish:
  'CDLEVENINGDOJISTAR': lambda  value,trend: {'patternType': '?', 'patternSignal': '<', 'reliability': '>'},

  ## high. reversal. 72% bearish
  'CDLEVENINGSTAR': lambda  value,trend: {'patternType': '?', 'patternSignal': '<', 'reliability': '>'},

  'CDLGAPSIDESIDEWHITE': lambda  value,trend: {'patternType': '?', 'patternSignal': '<', 'reliability': '>'},
  'CDLGRAVESTONEDOJI': lambda  value,trend: {'patternType': '?', 'patternSignal': '<', 'reliability': '>'},
  'CDLHAMMER': lambda  value,trend: {'patternType': '?', 'patternSignal': '<', 'reliability': '>'},
  'CDLHANGINGMAN': lambda  value,trend: {'patternType': '?', 'patternSignal': '<', 'reliability': '>'},
  'CDLHARAMI': lambda  value,trend: {'patternType': '?', 'patternSignal': '<', 'reliability': '>'},
  'CDLHARAMICROSS': lambda  value,trend: {'patternType': '?', 'patternSignal': '<', 'reliability': '>'},
  'CDLHIGHWAVE': lambda  value,trend: {'patternType': '?', 'patternSignal': '<', 'reliability': '>'},
  'CDLHIKKAKE': lambda  value,trend: {'patternType': '?', 'patternSignal': '<', 'reliability': '>'},
  'CDLHIKKAKEMOD': lambda  value,trend: {'patternType': '?', 'patternSignal': '<', 'reliability': '>'},
  'CDLHOMINGPIGEON': lambda  value,trend: {'patternType': '?', 'patternSignal': '<', 'reliability': '>'},
  'CDLIDENTICAL3CROWS': lambda  value,trend: {'patternType': '?', 'patternSignal': '<', 'reliability': '>'},
  'CDLINNECK': lambda  value,trend: {'patternType': '?', 'patternSignal': '<', 'reliability': '>'},

  ## high. continuation. 65% bearish
  'CDLINVERTEDHAMMER': lambda  value,trend: {'patternType': '?', 'patternSignal': '<', 'reliability': '>'},

  'CDLKICKING': lambda  value,trend: {'patternType': '?', 'patternSignal': '<', 'reliability': '>'},
  'CDLKICKINGBYLENGTH': lambda  value,trend: {'patternType': '?', 'patternSignal': '<', 'reliability': '>'},
  'CDLLADDERBOTTOM': lambda  value,trend: {'patternType': '?', 'patternSignal': '<', 'reliability': '>'},
  'CDLLONGLEGGEDDOJI': lambda  value,trend: {'patternType': '?', 'patternSignal': '<', 'reliability': '>'},
  'CDLLONGLINE': lambda  value,trend: {'patternType': '?', 'patternSignal': '<', 'reliability': '>'},
  'CDLMARUBOZU': lambda  value,trend: {'patternType': '?', 'patternSignal': '<', 'reliability': '>'},

  ## high. continuation. 61% bearish
  'CDLMATCHINGLOW': lambda  value,trend: {'patternType': 'reversal pattern', 'patternSignal': '<', 'reliability': '>'},

  'CDLMATHOLD': lambda  value,trend: {'patternType': '?', 'patternSignal': '<', 'reliability': '>'},
  'CDLMORNINGDOJISTAR': lambda  value,trend: {'patternType': '?', 'patternSignal': '<', 'reliability': '>'},
  'CDLMORNINGSTAR': lambda  value,trend: {'patternType': '?', 'patternSignal': '<', 'reliability': '>'},
  'CDLONNECK': lambda  value,trend: {'patternType': '?', 'patternSignal': '<', 'reliability': '>'},
  'CDLPIERCING': lambda  value,trend: {'patternType': '?', 'patternSignal': '<', 'reliability': '>'},
  'CDLRICKSHAWMAN': lambda  value,trend: {'patternType': '?', 'patternSignal': '<', 'reliability': '>'},
  'CDLRISEFALL3METHODS': lambda  value,trend: {'patternType': '?', 'patternSignal': '<', 'reliability': '>'},
  'CDLSEPARATINGLINES': lambda  value,trend: {'patternType': '?', 'patternSignal': '<', 'reliability': '>'},
  'CDLSHOOTINGSTAR': lambda  value,trend: {'patternType': '?', 'patternSignal': '<', 'reliability': '>'},
  'CDLSHORTLINE': lambda  value,trend: {'patternType': '?', 'patternSignal': '<', 'reliability': '>'},
  'CDLSPINNINGTOP': lambda  value,trend: {'patternType': '?', 'patternSignal': '<', 'reliability': '>'},
  'CDLSTALLEDPATTERN': lambda  value,trend: {'patternType': '?', 'patternSignal': '<', 'reliability': '>'},
  'CDLSTICKSANDWICH': lambda  value,trend: {'patternType': '?', 'patternSignal': '<', 'reliability': '>'},
  'CDLTAKURI': lambda  value,trend: {'patternType': '?', 'patternSignal': '<', 'reliability': '>'},

  ## high. continuation. 57% bullish 
  'CDLTASUKIGAP': lambda  value,trend: {'patternType': '?', 'patternSignal': '<', 'reliability': '>'},
  
  'CDLTHRUSTING': lambda  value,trend: {'patternType': '?', 'patternSignal': '<', 'reliability': '>'},
  'CDLTRISTAR': lambda  value,trend: {'patternType': '?', 'patternSignal': '<', 'reliability': '>'},
  'CDLUNIQUE3RIVER': lambda  value,trend: {'patternType': '?', 'patternSignal': '<', 'reliability': '>'},

  # /* Proceed with the calculation for the requested range.
  #   * Must have:
  #   * - first candle: white candle, usually long
  #   * - second candle: small black real body
  #   * - gap between the first and the second candle's real bodies
  #   * - third candle: black candle with a real body that engulfs the preceding candle 
  #   *   and closes above the white candle's close
  #   * The meaning of "short" and "long" is specified with TA_SetCandleSettings
  #   * outInteger is negative (-1 to -100): upside gap two crows is always bearish; 
  #   * the user should consider that an upside gap two crows is significant when it appears in an uptrend, 
  #   * while this function does not consider the trend
  #   */
  'CDLUPSIDEGAP2CROWS': lambda  value,trend: {'patternType': '?', 'patternSignal': '<', 'reliability': '>'},
  
  'CDLXSIDEGAP3METHODS': lambda  value,trend: {'patternType': '?', 'patternSignal': '<', 'reliability': '>'},
}

# still missing:
# - Two Black Gapping

class PatternType(Enum): 
  Reversal = 0
  Continuation = 1
  N = 2

class PatternSignal(Enum): 
  Bullish = 0 # up
  Bearish = 1 # down
  N = 2

class PatternReliability(Enum):
  High = 0
  Medium = 1
  Low = 3
  N = 4

fetchDefaultOptions = {
  'group_by': 'ticker',
  'auto_adjust': False,
  'prepost': False,
  'threads': True,
  'proxy': None
}

shortTermOptions = {  # short term - 10 days
  'period': '3wk',
  'interval': '1d'
}
mediumTermOptions = {  # medium term > - 3 month
  'period': '7mo',
  'interval': '1wk'
}
longTermOptions = { # long term - 10 month
  'period': '2y',
  'interval': '1mo'
}