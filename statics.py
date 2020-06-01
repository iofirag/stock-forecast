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
#     # 'value': value,
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
# https://www.quantshare.com/index.php?option=manual&dir=/QuantShare%20Language/Candlestick%20Pattern/CdlEngulfing%201.html
# https://www.feedroll.com/candlestick-patterns/1309-index-candlestick-patterns/
# http://www.traderencyclopedia.com/wiki/index.php/Engulfing_line
# https://www.google.com/search?
candleStickSwitcher = {
  
  # /* Proceed with the calculation for the requested range.
  #   * Must have:
  #   * - first candle: long white candle
  #   * - second candle: black real body
  #   * - gap between the first and the second candle's real bodies
  #   * - third candle: black candle that opens within the second real body and closes within the first real body
  #   * The meaning of "long" is specified with TA_SetCandleSettings
  #   * outInteger is negative (-1 to -100): two crows is always bearish; 
  #   * the user should consider that two crows is significant when it appears in an uptrend, while this function 
  #   * does not consider the trend
  #   */
  # # "https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDL2CROWS.c#l239"
  'CDL2CROWS': lambda value, trend: {
    'acceptableValues': [
      {'low': -100, 'high': -1, 'currentTrend': TrendType.Uptrend, 'predict': PatternSignal.Bearish, 'patternType': PatternType.Reversal}
    ],
    'reliability': PatternReliability.Moderate.name,
    # 'value': value,
    'img': 'https://www.candlescanner.com/wp-content/uploads/2015/08/two-crows1.png',
    'description': ['https://www.investopedia.com/terms/u/upside-gap-two-crows.asp'],
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
  # # "https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDL3BLACKCROWS.c#l239"
  'CDL3BLACKCROWS': lambda value,trend: {
    'acceptableValues': [
      {'low': -100, 'high': -1, 'currentTrend': TrendType.Uptrend, 'predictedTrend': PatternSignal.Bearish, 'patternType': PatternType.Reversal}
    ],
    'reliability': PatternReliability.High.name,
    # 'value': value,
    'img': '',
    'description': ['https://www.investopedia.com/terms/t/three_black_crows.asp'],
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
  # # "https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDL3INSIDE.c#l239"
  'CDL3INSIDE': lambda value,trend: {
    'acceptableValues': [
      {'low': 1, 'high': 100, 'currentTrend': TrendType.Downtrend, 'predictedTrend': PatternSignal.Bullish, 'patternType': PatternType.Reversal},
      {'low': -100, 'high': -1, 'currentTrend': TrendType.Uptrend, 'predictedTrend': PatternSignal.Bearish, 'patternType': PatternType.Reversal}
    ],
    'reliability': PatternReliability.Moderate.name,
    # 'value': value,
    'img': 'https://bpcdn.co/images/2016/05/grade2-three-inside.png',
    'description': ['https://www.investopedia.com/terms/t/three-inside-updown.asp'],
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
  # # "https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDL3LINESTRIKE.c#l239"
  'CDL3LINESTRIKE': lambda value,trend: {
    'acceptableValues': [
      {'low': 1, 'high': 100, 'currentTrend': TrendType.Uptrend, 'predictedTrend': PatternSignal.Bullish, 'patternType': PatternType.Continuation},
      {'low': -100, 'high': -1, 'currentTrend': TrendType.Downtrend, 'predictedTrend': PatternSignal.Bearish, 'patternType': PatternType.Continuation}
    ],
    'reliability': PatternReliability.Low.name,
    # 'value': value,
    'img': '',
    'description': ['https://www.investopedia.com/articles/active-trading/092315/5-most-powerful-candlestick-patterns.asp#three-line-strike'],
  },
  
  # /* Proceed with the calculation for the requested range.
  #   * Must have:
  #   * - first: black (white) real body
  #   * - second: white (black) real body that engulfs the prior real body
  #   * - third: candle that closes higher (lower) than the second candle
  #   * outInteger is positive (1 to 100) for the three outside up or negative (-1 to -100) for the three outside down;
  #   * the user should consider that a three outside up must appear in a downtrend and three outside down must appear
  #   * in an uptrend, while this function does not consider it
  #   */
  # http://tutorials.topstockresearch.com/candlestick/Bearish/ThreeOutsideDown/TutotrialOnThreeOutsideDownPattern.html
  # # "https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDL3OUTSIDE.c#l239"
  'CDL3OUTSIDE': lambda value,trend: {
    'acceptableValues': [
      {'low': 1, 'high': 100, 'currentTrend': TrendType.Downtrend, 'predictedTrend': PatternSignal.Bullish, 'patternType': PatternType.Reversal},
      {'low': -100, 'high': -1, 'currentTrend': TrendType.Uptrend, 'predictedTrend': PatternSignal.Bearish, 'patternType': PatternType.Reversal}
    ],
    'reliability': PatternReliability.High.name,
    # 'value': value,
    'img': 'http://www.tradingpedia.com/wp-content/uploads/2014/02/1.-Evening-star.jpg',
    'description': ['https://www.investopedia.com/terms/t/three-outside-updown.asp'],
  },

  # /* Proceed with the calculation for the requested range.
  #   * Must have:
  #   * - first candle: long black candle with long lower shadow
  #   * - second candle: smaller black candle that opens higher than prior close but within prior candle's range 
  #   *   and trades lower than prior close but not lower than prior low and closes off of its low (it has a shadow)
  #   * - third candle: small black marubozu (or candle with very short shadows) engulfed by prior candle's range
  #   * The meanings of "long body", "short body", "very short shadow" are specified with TA_SetCandleSettings;
  #   * outInteger is positive (1 to 100): 3 stars in the south is always bullish;
  #   * the user should consider that 3 stars in the south is significant when it appears in downtrend, while this function 
  #   * does not consider it
  #   */
  # # "https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDL3STARSINSOUTH.c#l239"
  'CDL3STARSINSOUTH': lambda value,trend: {
    'acceptableValues': [
      {'low': 1, 'high': 100, 'currentTrend': TrendType.Downtrend, 'predictedTrend': PatternSignal.Bullish, 'patternType': PatternType.Reversal},
    ],
    'reliability': PatternReliability.Moderate.name,
    # 'value': value,
    'img': 'https://hitandruncandlesticks.com/wp-content/uploads/2016/08/bullish_three_stars_in_the_south.jpg',
    'description': ['https://www.investopedia.com/terms/t/three-stars-south.asp'],
  },

  # /* Proceed with the calculation for the requested range.
  #   * Must have:
  #   * - three white candlesticks with consecutively higher closes
  #   * - Greg Morris wants them to be long, Steve Nison doesn't; anyway they should not be short
  #   * - each candle opens within or near the previous white real body 
  #   * - each candle must have no or very short upper shadow
  #   * - to differentiate this pattern from advance block, each candle must not be far shorter than the prior candle
  #   * The meanings of "not short", "very short shadow", "far" and "near" are specified with TA_SetCandleSettings;
  #   * here the 3 candles must be not short, if you want them to be long use TA_SetCandleSettings on BodyShort;
  #   * outInteger is positive (1 to 100): advancing 3 white soldiers is always bullish;
  #   * the user should consider that 3 white soldiers is significant when it appears in downtrend, while this function 
  #   * does not consider it
  #   */
  # # "https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDL3WHITESOLDIERS.c#l239"
  'CDL3WHITESOLDIERS': lambda value,trend: {
    'acceptableValues': [
      {'low': 1, 'high': 100, 'currentTrend': TrendType.Downtrend, 'predictedTrend': PatternSignal.Bullish, 'patternType': PatternType.Reversal},
    ],
    'reliability': PatternReliability.High.name,
    # 'value': value,
    'img': 'https://tutorials.topstockresearch.com/candlestick/Bullish/ThreeWhiteSoldiers/ThreeWhiteSoldiers.png',
    'description': ['https://www.investopedia.com/terms/t/three_white_soldiers.asp'],
  },

  # /* Proceed with the calculation for the requested range.
  #   * Must have:
  #   * - first candle: long white (black) real body
  #   * - second candle: doji
  #   * - third candle: black (white) real body that moves well within the first candle's real body
  #   * - upside (downside) gap between the first candle and the doji (the shadows of the two candles don't touch)
  #   * - downside (upside) gap between the doji and the third candle (the shadows of the two candles don't touch)
  #   * The meaning of "doji" and "long" is specified with TA_SetCandleSettings
  #   * The meaning of "moves well within" is specified with optInPenetration and "moves" should mean the real body should
  #   * not be short ("short" is specified with TA_SetCandleSettings) - Greg Morris wants it to be long, someone else want
  #   * it to be relatively long
  #   * outInteger is positive (1 to 100) when it's an abandoned baby bottom or negative (-1 to -100) when it's 
  #   * an abandoned baby top; the user should consider that an abandoned baby is significant when it appears in 
  #   * an uptrend or downtrend, while this function does not consider the trend
  #   */
  ## high. reversal. 70% bullish
  # # "https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDLABANDONEDBABY.c#l239"
  'CDLABANDONEDBABY': lambda value,trend: {
    'acceptableValues': [
      {'low': 1, 'high': 100, 'currentTrend': TrendType.Downtrend, 'predictedTrend': PatternSignal.Bullish, 'patternType': PatternType.Reversal, 'description': ['https://www.investopedia.com/terms/b/bullish-abandoned-baby.asp']},
      {'low': -100, 'high': -1, 'currentTrend': TrendType.Uptrend, 'predictedTrend': PatternSignal.Bearish, 'patternType': PatternType.Reversal, 'description': ['https://www.investopedia.com/terms/b/bearish-abandoned-baby.asp']}
    ],
    'reliability': PatternReliability.High.name,
    # 'value': value,
    'img': 'https://mr-uploads.s3.amazonaws.com/uploads/2014/12/abandoned-baby2.png',
    # 'description': [''],
  },
  
  # /* Proceed with the calculation for the requested range.
  #   * Must have:
  #   * - three white candlesticks with consecutively higher closes
  #   * - each candle opens within or near the previous white real body 
  #   * - first candle: long white with no or very short upper shadow (a short shadow is accepted too for more flexibility)
  #   * - second and third candles, or only third candle, show signs of weakening: progressively smaller white real bodies 
  #   * and/or relatively long upper shadows; see below for specific conditions
  #   * The meanings of "long body", "short shadow", "far" and "near" are specified with TA_SetCandleSettings;
  #   * outInteger is negative (-1 to -100): advance block is always bearish;
  #   * the user should consider that advance block is significant when it appears in uptrend, while this function 
  #   * does not consider it
  #   */
  # # "https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDLADVANCEBLOCK.c#l239"
  'CDLADVANCEBLOCK': lambda value,trend: {
    'acceptableValues': [
      {'low': -100, 'high': -1, 'currentTrend': TrendType.Uptrend, 'predictedTrend': PatternSignal.Bearish, 'patternType': PatternType.Reversal}
    ],
    'reliability': PatternReliability.Moderate.name,
    # 'value': value,
    'img': 'https://www.investopedia.com/thmb/tdbMb6qVoafr7S-lAQKjKpiTZaI=/1538x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/dotdash_Final_Advance_Block_Feb_2020-2f102ad610704541ad0583c14d4bbd7a.jpg',
    'description': ['https://www.investopedia.com/terms/a/advance-block.asp'],
  },

  # /* Proceed with the calculation for the requested range.
  #   * Must have:
  #   * - long white (black) real body
  #   * - no or very short lower (upper) shadow
  #   * The meaning of "long" and "very short" is specified with TA_SetCandleSettings
  #   * outInteger is positive (1 to 100) when white (bullish), negative (-1 to -100) when black (bearish)
  #   */
  # # "https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDLBELTHOLD.c#l239"
  'CDLBELTHOLD': lambda value,trend: {
    'acceptableValues': [
      {'low': 1, 'high': 100, 'currentTrend': TrendType.Downtrend, 'predictedTrend': PatternSignal.Bullish, 'patternType': PatternType.Reversal, 'description': ['https://www.investopedia.com/terms/b/bullishbelthold.asp']},
      {'low': -100, 'high': -1, 'currentTrend': TrendType.Uptrend, 'predictedTrend': PatternSignal.Bearish, 'patternType': PatternType.Reversal, 'description': ['https://www.investopedia.com/terms/b/bearishbelthold.asp']},
    ],
    'reliability': PatternReliability.Low.name,
    # 'value': value,
    'img': 'https://i.ytimg.com/vi/we62RExJrxM/maxresdefault.jpg',
    # 'description': [''],
  },

  # /* Proceed with the calculation for the requested range.
  #   * Must have:
  #   * - first candle: long black (white)
  #   * - second candle: black (white) day whose body gaps down (up)
  #   * - third candle: black or white day with lower (higher) high and lower (higher) low than prior candle's
  #   * - fourth candle: black (white) day with lower (higher) high and lower (higher) low than prior candle's
  #   * - fifth candle: white (black) day that closes inside the gap, erasing the prior 3 days
  #   * The meaning of "long" is specified with TA_SetCandleSettings
  #   * outInteger is positive (1 to 100) when bullish or negative (-1 to -100) when bearish;
  #   * the user should consider that breakaway is significant in a trend opposite to the last candle, while this 
  #   * function does not consider it
  #   */
  ## high. reversal. 63% bearish
  # # "https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDLBREAKAWAY.c#l239"
  'CDLBREAKAWAY': lambda value,trend: {
    'acceptableValues': [
      {'low': 1, 'high': 100, 'currentTrend': TrendType.Downtrend, 'predictedTrend': PatternSignal.Bullish, 'patternType': PatternType.Reversal, 'description': ['https://www.candlesticker.com/Pattern.aspx?lang=en&Pattern=5101']},
      {'low': -100, 'high': -1, 'currentTrend': TrendType.Uptrend, 'predictedTrend': PatternSignal.Bearish, 'patternType': PatternType.Reversal, 'description': ['https://www.traderslog.com/bearish-breakaway-pattern']},
    ],
    'reliability': PatternReliability.Moderate.name,
    # 'value': value,
    'img': 'https://investorshub.advfn.com/uimage/uploads/2018/1/15/gnshqbreakaway-patterns.png',
    # description': ['',
  },
  
  # /* Proceed with the calculation for the requested range.
  #   * Must have:
  #   * - long white (black) real body
  #   * - no or very short upper (lower) shadow
  #   * The meaning of "long" and "very short" is specified with TA_SetCandleSettings
  #   * outInteger is positive (1 to 100) when white (bullish), negative (-1 to -100) when black (bearish)
  #   */
  # # "https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDLCLOSINGMARUBOZU.c#l239"
  'CDLCLOSINGMARUBOZU': lambda value,trend: {
    'acceptableValues': [
      {'low': 1, 'high': 100, 'currentTrend': TrendType.Uptrend, 'predictedTrend': PatternSignal.Bullish, 'patternType': PatternType.Continuation},
      {'low': -100, 'high': -1, 'currentTrend': TrendType.Downtrend, 'predictedTrend': PatternSignal.Bearish, 'patternType': PatternType.Continuation},
      {'low': 1, 'high': 100, 'currentTrend': TrendType.Downtrend, 'predictedTrend': PatternSignal.Bullish, 'patternType': PatternType.Reversal},
      {'low': -100, 'high': -1, 'currentTrend': TrendType.Uptrend, 'predictedTrend': PatternSignal.Bearish, 'patternType': PatternType.Reversal},
    ],
    'reliability': PatternReliability.Low.name,
    # 'value': value,
    'img': 'https://www.elearnmarkets.com/blog/wp-content/uploads/2016/03/CLOSING-MARUBOZU-CANDLESTICKS.jpg',
    'description': ['https://www.candlescanner.com/candlestick-patterns/closing-black-marubozu/'],
  },

  # /* Proceed with the calculation for the requested range.
  #   * Must have:
  #   * - first candle: black marubozu (very short shadows)
  #   * - second candle: black marubozu (very short shadows)
  #   * - third candle: black candle that opens gapping down but has an upper shadow that extends into the prior body
  #   * - fourth candle: black candle that completely engulfs the third candle, including the shadows
  #   * The meanings of "very short shadow" are specified with TA_SetCandleSettings;
  #   * outInteger is positive (1 to 100): concealing baby swallow is always bullish;
  #   * the user should consider that concealing baby swallow is significant when it appears in downtrend, while 
  #   * this function does not consider it
  #   */
  # # "https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDLCONCEALBABYSWALL.c#l239"
  'CDLCONCEALBABYSWALL': lambda value,trend: {
    'acceptableValues': [
      {'low': 1, 'high': 100, 'currentTrend': TrendType.Downtrend, 'predictedTrend': PatternSignal.Bullish, 'patternType': PatternType.Reversal},
    ],
    'reliability': PatternReliability.High.name,
    # 'value': value,
    'img': 'https://www.candlescanner.com/wp-content/uploads/2015/08/cancealing-baby-swallow.png',
    'description': ['https://www.candlescanner.com/candlestick-patterns/concealing-baby-swallow'],
  },

  # /* Proceed with the calculation for the requested range.
  #   * Must have:
  #   * - first candle: long black (white)
  #   * - second candle: long white (black) with close equal to the prior close
  #   * The meaning of "equal" and "long" is specified with TA_SetCandleSettings
  #   * outInteger is positive (1 to 100) when bullish or negative (-1 to -100) when bearish;
  #   * the user should consider that counterattack is significant in a trend, while this function does not consider it
  #   */
  # # "https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDLCOUNTERATTACK.c#l239"
  'CDLCOUNTERATTACK': lambda value,trend: {
    'acceptableValues': [
      {'low': 1, 'high': 100, 'currentTrend': TrendType.Downtrend, 'predictedTrend': PatternSignal.Bullish, 'patternType': PatternType.Reversal},
      {'low': -100, 'high': -1, 'currentTrend': TrendType.Uptrend, 'predictedTrend': PatternSignal.Bearish, 'patternType': PatternType.Reversal},
    ],
    'reliability': PatternReliability.N.name,
    # 'value': value,
    'img': 'http://www.traderencyclopedia.com/wiki/images/8/8c/Counterattack.jpg',
    'description': ['https://www.investopedia.com/terms/c/counterattack.asp'],
  },

  
  # /* Proceed with the calculation for the requested range.
  #   * Must have:
  #   * - first candle: long white candle
  #   * - second candle: black candle that opens above previous day high and closes within previous day real body; 
  #   * Greg Morris wants the close to be below the midpoint of the previous real body
  #   * The meaning of "long" is specified with TA_SetCandleSettings, the penetration of the first real body is specified
  #   * with optInPenetration
  #   * outInteger is negative (-1 to -100): dark cloud cover is always bearish
  #   * the user should consider that a dark cloud cover is significant when it appears in an uptrend, while 
  #   * this function does not consider it
  #   */
  # http://tutorials.topstockresearch.com/candlestick/Bearish/DarkCloudCover/TutotrialOnDarkCloudCoverChartPattern.html
  # # "https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDLDARKCLOUDCOVER.c#l239"
  'CDLDARKCLOUDCOVER': lambda value,trend: {
    'acceptableValues': [
      {'low': -100, 'high': -1, 'currentTrend': TrendType.Uptrend, 'predictedTrend': PatternSignal.Bearish, 'patternType': PatternType.Reversal},
    ],
    'reliability': PatternReliability.High.name,
    # 'value': value,
    'img': 'https://mr-uploads.s3.amazonaws.com/uploads/2014/12/dark-cloud-cover1.png',
    'description': ['https://www.candlescanner.com/candlestick-patterns/dark-cloud-cover/'],
  },
  
  
  # /* Proceed with the calculation for the requested range.
  #   *
  #   * Must have:
  #   * - open quite equal to close
  #   * How much can be the maximum distance between open and close is specified with TA_SetCandleSettings
  #   * outInteger is always positive (1 to 100) but this does not mean it is bullish: doji shows uncertainty and it is
  #   * neither bullish nor bearish when considered alone
  #   */
  # # "https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDLDOJI.c#l239"
  'CDLDOJI': lambda value,trend: {
    'acceptableValues': [
      {'low': 1, 'high': 100, 'currentTrend': TrendType.Indecision, 'predictedTrend': PatternSignal.Indecision, 'patternType': PatternType.Indecision},
    ],
    'reliability': PatternReliability.Low.name,
    # 'value': value,
    'img': 'https://a.c-dn.net/b/3K4xiq/doji-candlestick-pattern_body_standarddoji.png',
    'description': ['https://www.candlescanner.com/candlestick-patterns/doji-2/'],
  },
  
  
  # /* Proceed with the calculation for the requested range.
  #   * Must have:
  #   * - first candle: long real body
  #   * - second candle: star (open gapping up in an uptrend or down in a downtrend) with a doji
  #   * The meaning of "doji" and "long" is specified with TA_SetCandleSettings
  #   * outInteger is positive (1 to 100) when bullish or negative (-1 to -100) when bearish; 
  #   * it's defined bullish when the long candle is white and the star gaps up, bearish when the long candle 
  #   * is black and the star gaps down; the user should consider that a doji star is bullish when it appears 
  #   * in an uptrend and it's bearish when it appears in a downtrend, so to determine the bullishness or 
  #   * bearishness of the pattern the trend must be analyzed
  #   */
  # reversal
  # # "https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDLDOJISTAR.c#l239"
  'CDLDOJISTAR': lambda value,trend: {
    'acceptableValues': [
      {
        'low': 1, 'high': 100, 'currentTrend': TrendType.Uptrend, 'predictedTrend': PatternSignal.Bullish, 'patternType': PatternType.Reversal, 
        'description': ['https://www.adigitalblogger.com/chart-patterns/doji-star-bullish/']
      },
      {
        'low': -100, 'high': -1, 'currentTrend': TrendType.Downtrend, 'predictedTrend': PatternSignal.Bearish, 'patternType': PatternType.Reversal, 
        'description': ['https://www.adigitalblogger.com/chart-patterns/doji-star-bearish/']
      },
    ],
    'reliability': PatternReliability.Moderate.name,
    # 'value': value,
    'img': 'https://a.c-dn.net/b/3K4xiq/doji-candlestick-pattern_body_standarddoji.png',
  },

  # /* Proceed with the calculation for the requested range.
  #   *
  #   * Must have:
  #   * - doji body
  #   * - open and close at the high of the day = no or very short upper shadow
  #   * - lower shadow (to distinguish from other dojis, here lower shadow should not be very short)
  #   * The meaning of "doji" and "very short" is specified with TA_SetCandleSettings
  #   * outInteger is always positive (1 to 100) but this does not mean it is bullish: dragonfly doji must be considered
  #   * relatively to the trend
  #   */
  # http://tutorials.topstockresearch.com/candlestick/Bullish/DragonflyDoji/TutotrialOnDragonflyDojiChartPattern.html
  # # "https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDLDRAGONFLYDOJI.c#l239"
  'CDLDRAGONFLYDOJI': lambda value,trend: {
    'acceptableValues': [
      {'low': 1, 'high': 100, 'currentTrend': TrendType.Uptrend, 'predictedTrend': PatternSignal.Bullish, 'patternType': PatternType.Reversal},
      {'low': 1, 'high': 100, 'currentTrend': TrendType.Downtrend, 'predictedTrend': PatternSignal.Bearish, 'patternType': PatternType.Reversal},
    ],
    'reliability': f'{PatternReliability.Low.name}/{PatternReliability.Moderate.name}',
    # 'value': value,
    'img': 'https://tradingcryptocourse.com/wp-content/uploads/2018/11/candlestickpattern7.jpg',
    'description': ['https://www.adigitalblogger.com/chart-patterns/dragonfly-doji/'],
  },

  # /* Proceed with the calculation for the requested range.
  #   * Must have:
  #   * - first: black (white) real body
  #   * - second: white (black) real body that engulfs the prior real body
  #   * outInteger is positive (1 to 100) when bullish or negative (-1 to -100) when bearish:
  #   * - 100 is returned when the second candle's real body begins before and ends after the first candle's real body
  #   * - 80 is returned when the two real bodies match on one end (Greg Morris contemplate this case in his book
  #   *   "Candlestick charting explained")
  #   * The user should consider that an engulfing must appear in a downtrend if bullish or in an uptrend if bearish,
  #   * while this function does not consider it
  #   */
  # high
  # http://tutorials.topstockresearch.com/candlestick/Bearish/BearishEngulfing/TutotrialOnBearishEngulfingChartPattern.html
  # # "https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDLENGULFING.c#l239"
  'CDLENGULFING': lambda value,trend: {
    'acceptableValues': [
      {'low': 1, 'high': 100, 'currentTrend': TrendType.Downtrend, 'predictedTrend': PatternSignal.Bullish, 'patternType': PatternType.Reversal,
      'description': ['https://www.adigitalblogger.com/chart-patterns/bullish-engulfing-pattern/']},
      {'low': -100, 'high': -1, 'currentTrend': TrendType.Uptrend, 'predictedTrend': PatternSignal.Bearish, 'patternType': PatternType.Reversal,
      'description': ['https://www.adigitalblogger.com/chart-patterns/bearish-engulfing-pattern/']},
    ],
    'reliability': PatternReliability.Moderate.name,
    # 'value': value,
    'img': 'https://forextraininggroup.com/wp-content/uploads/2016/11/Engulfing-Pattern-Stop-Loss.png',
    # description': [''],
  },
  
  # /* Proceed with the calculation for the requested range.
  #   * Must have:
  #   * - first candle: long white real body
  #   * - second candle: doji gapping up
  #   * - third candle: black real body that moves well within the first candle's real body
  #   * The meaning of "doji" and "long" is specified with TA_SetCandleSettings
  #   * The meaning of "moves well within" is specified with optInPenetration and "moves" should mean the real body should
  #   * not be short ("short" is specified with TA_SetCandleSettings) - Greg Morris wants it to be long, someone else want
  #   * it to be relatively long
  #   * outInteger is negative (-1 to -100): evening star is always bearish; 
  #   * the user should consider that an evening star is significant when it appears in an uptrend, 
  #   * while this function does not consider the trend
  #   */
  # # "https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDLEVENINGDOJISTAR.c#l239"
  'CDLEVENINGDOJISTAR': lambda value,trend: {
    'acceptableValues': [
      {'low': -100, 'high': -1, 'currentTrend': TrendType.Uptrend, 'predictedTrend': PatternSignal.Bearish, 'patternType': PatternType.Reversal},
    ],
    'reliability': PatternReliability.High.name,
    # 'value': value,
    'img': '',
    'description': ['https://wiki.timetotrade.com/Evening_Doji_Star_Candlestick'],
  },

  # /* Proceed with the calculation for the requested range.
  #   * Must have:
  #   * - first candle: long white real body
  #   * - second candle: star (short real body gapping up)
  #   * - third candle: black real body that moves well within the first candle's real body
  #   * The meaning of "short" and "long" is specified with TA_SetCandleSettings
  #   * The meaning of "moves well within" is specified with optInPenetration and "moves" should mean the real body should
  #   * not be short ("short" is specified with TA_SetCandleSettings) - Greg Morris wants it to be long, someone else want
  #   * it to be relatively long
  #   * outInteger is negative (-1 to -100): evening star is always bearish; 
  #   * the user should consider that an evening star is significant when it appears in an uptrend, 
  #   * while this function does not consider the trend
  #   */
  ## high. reversal. 72% bearish
  # http://tutorials.topstockresearch.com/candlestick/Bearish/EveningStar/TutotrialOnEveningStarChartPattern.html
  # https://www.investopedia.com/terms/e/eveningstar.asp
  # # "https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDLEVENINGSTAR.c#l239"
  'CDLEVENINGSTAR': lambda value,trend: {
    'acceptableValues': [
      {'low': -100, 'high': -1, 'currentTrend': TrendType.Uptrend, 'predictedTrend': PatternSignal.Bearish, 'patternType': PatternType.Reversal},
    ],
    'reliability': PatternReliability.High.name,
    # 'value': value,
    'img': '',
    'description': ['https://www.adigitalblogger.com/chart-patterns/evening-star-pattern/'],
  },

  # /* Proceed with the calculation for the requested range.
  #   * Must have:
  #   * - upside or downside gap (between the bodies)
  #   * - first candle after the window: white candlestick
  #   * - second candle after the window: white candlestick with similar size (near the same) and about the same 
  #   *   open (equal) of the previous candle
  #   * - the second candle does not close the window
  #   * The meaning of "near" and "equal" is specified with TA_SetCandleSettings
  #   * outInteger is positive (1 to 100) or negative (-1 to -100): the user should consider that upside 
  #   * or downside gap side-by-side white lines is significant when it appears in a trend, while this function 
  #   * does not consider the trend
  #   */
  # # "https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDLGAPSIDESIDEWHITE.c#l239"
  'CDLGAPSIDESIDEWHITE': lambda value,trend: {
    'name': 'GAP SIDE SIDE WHITE',
    'acceptableValues': [
      {'low': 1, 'high': 100, 'currentTrend': TrendType.Uptrend, 'predictedTrend': PatternSignal.Bullish, 'patternType': PatternType.Continuation},
      {'low': -100, 'high': -1, 'currentTrend': TrendType.Downtrend, 'predictedTrend': PatternSignal.Bearish, 'patternType': PatternType.Continuation},
    ],
    'reliability': PatternReliability.Moderate.name,
    # 'value': value,
    'img': '',
    'description': ['https://www.investopedia.com/terms/u/updown-gap-sidebyside-white-lines.asp'],
  },

  # /* Proceed with the calculation for the requested range.
  #   *
  #   * Must have:
  #   * - doji body
  #   * - open and close at the low of the day = no or very short lower shadow
  #   * - upper shadow (to distinguish from other dojis, here upper shadow should not be very short)
  #   * The meaning of "doji" and "very short" is specified with TA_SetCandleSettings
  #   * outInteger is always positive (1 to 100) but this does not mean it is bullish: gravestone doji must be considered
  #   * relatively to the trend
  #   */
  # http://tutorials.topstockresearch.com/candlestick/Bearish/GravestoneDoji/TutotrialOnGravestoneDojiBearishChartPattern.html
  # # "https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDLGRAVESTONEDOJI.c#l239"
  'CDLGRAVESTONEDOJI': lambda value,trend: {
    'acceptableValues': [
      {'low': 1, 'high': 100, 'currentTrend': TrendType.Uptrend, 'predictedTrend': PatternSignal.Bearish, 'patternType': PatternType.Reversal},
      {'low': 1, 'high': 100, 'currentTrend': TrendType.Downtrend, 'predictedTrend': PatternSignal.Bearish, 'patternType': PatternType.Continuation},
    ],
    'reliability': PatternReliability.N.name,
    # 'value': value,
    'img': '',
    'description': [
      'https://www.investopedia.com/terms/g/gravestone-doji.asp', 
      'https://www.candlescanner.com/candlestick-patterns/gravestone-doji/',
    ],
  },

  # /* Proceed with the calculation for the requested range.
  #   * Must have:
  #   * - small real body
  #   * - long lower shadow
  #   * - no, or very short, upper shadow
  #   * - body below or near the lows of the previous candle
  #   * The meaning of "short", "long" and "near the lows" is specified with TA_SetCandleSettings;
  #   * outInteger is positive (1 to 100): hammer is always bullish;
  #   * the user should consider that a hammer must appear in a downtrend, while this function does not consider it
  #   */
  # # "https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDLHAMMER.c#l239"
  'CDLHAMMER': lambda value,trend: {
    'acceptableValues': [
      {'low': 1, 'high': 100, 'currentTrend': TrendType.Downtrend, 'predictedTrend': PatternSignal.Bullish, 'patternType': PatternType.Reversal},
    ],
    'reliability': PatternReliability.N.name,
    # # 'value': value,
    'img': '',
    'description': ['https://www.investopedia.com/terms/h/hammer.asp'],
  },

  # /* Proceed with the calculation for the requested range.
  #   * Must have:
  #   * - small real body
  #   * - long lower shadow
  #   * - no, or very short, upper shadow
  #   * - body above or near the highs of the previous candle
  #   * The meaning of "short", "long" and "near the highs" is specified with TA_SetCandleSettings;
  #   * outInteger is negative (-1 to -100): hanging man is always bearish;
  #   * the user should consider that a hanging man must appear in an uptrend, while this function does not consider it
  #   */
  # http://tutorials.topstockresearch.com/candlestick/Bearish/HangingMan/TutotrialOnHangingManBearishChartPattern.html
  # # "https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDLHANGINGMAN.c#l239"
  'CDLHANGINGMAN': lambda value,trend: {
    'acceptableValues': [
      {'low': -100, 'high': -1, 'currentTrend': TrendType.Uptrend, 'predictedTrend': PatternSignal.Bearish, 'patternType': PatternType.Reversal},
    ],
    'reliability': PatternReliability.N.name,
    # # 'value': value,
    'img': '',
    'description': ['https://www.investopedia.com/articles/active-trading/040914/understanding-hanging-man-optimistic-candlestick-pattern.asp'],
  },

  # /* Proceed with the calculation for the requested range.
  #   * Must have:
  #   * - first candle: long white (black) real body
  #   * - second candle: short real body totally engulfed by the first 
  #   * The meaning of "short" and "long" is specified with TA_SetCandleSettings
  #   * outInteger is positive (1 to 100) when bullish or negative (-1 to -100) when bearish:
  #   * - 100 is returned when the first candle's real body begins before and ends after the second candle's real body
  #   * - 80 is returned when the two real bodies match on one end (Greg Morris contemplate this case in his book
  #   *   "Candlestick charting explained")
  #   * The user should consider that a harami is significant when it appears in a downtrend if bullish or 
  #   * in an uptrend when bearish, while this function does not consider the trend
  #   */
  # http://tutorials.topstockresearch.com/candlestick/Bearish/BearishHarami/TutotrialOnBearishHaramiChartPattern.html
  # # "https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDLHARAMI.c#l239"
  'CDLHARAMI': lambda value,trend: {
    'acceptableValues': [
      {'low': 1, 'high': 100, 'currentTrend': TrendType.Downtrend, 'predictedTrend': PatternSignal.Bullish, 'patternType': PatternType.Reversal},
      {'low': -100, 'high': -1, 'currentTrend': TrendType.Uptrend, 'predictedTrend': PatternSignal.Bearish, 'patternType': PatternType.Reversal},
    ],
    'reliability': PatternReliability.N.name,
    # # 'value': value,
    'img': '',
    'description': ['https://www.investopedia.com/terms/b/bullishharami.asp', 'https://www.investopedia.com/terms/b/bearishharami.asp'],
  },

  # /* Proceed with the calculation for the requested range.
  #   * Must have:
  #   * - first candle: long white (black) real body
  #   * - second candle: doji totally engulfed by the first
  #   * The meaning of "doji" and "long" is specified with TA_SetCandleSettings
  #   * outInteger is positive (1 to 100) when bullish or negative (-1 to -100) when bearish; 
  #   * the user should consider that a harami cross is significant when it appears in a downtrend if bullish or 
  #   * in an uptrend when bearish, while this function does not consider the trend
  #   */
  # # "https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDLHARAMICROSS.c#l239"
  'CDLHARAMICROSS': lambda value,trend: {
    'acceptableValues': [
      {'low': 1, 'high': 100, 'currentTrend': TrendType.Downtrend, 'predictedTrend': PatternSignal.Bullish, 'patternType': PatternType.Reversal},
      {'low': -100, 'high': -1, 'currentTrend': TrendType.Uptrend, 'predictedTrend': PatternSignal.Bearish, 'patternType': PatternType.Reversal},
    ],
    'reliability': PatternReliability.N.name,
    # 'value': value,
    'img': '',
    'description': ['https://www.investopedia.com/terms/h/haramicross.asp'],
  },

  # /* Proceed with the calculation for the requested range.
  #   * Must have:
  #   * - short real body
  #   * - very long upper and lower shadow
  #   * The meaning of "short" and "very long" is specified with TA_SetCandleSettings
  #   * outInteger is positive (1 to 100) when white or negative (-1 to -100) when black;
  #   * it does not mean bullish or bearish
  #   */
  # "https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDLHIGHWAVE.c#l239"
  'CDLHIGHWAVE': lambda value,trend: {
    'acceptableValues': [
#       {'low': 1, 'high': 100, 'currentTrend': TrendType.Uptrend, 'predictedTrend': PatternSignal.Bullish, 'patternType': PatternType.Continuation},
#       {'low': -100, 'high': -1, 'currentTrend': TrendType.Downtrend, 'predictedTrend': PatternSignal.Bearish, 'patternType': PatternType.Continuation},
#       {'low': 1, 'high': 100, 'currentTrend': TrendType.Downtrend, 'predictedTrend': PatternSignal.Bullish, 'patternType': PatternType.Reversal},
#       {'low': -100, 'high': -1, 'currentTrend': TrendType.Uptrend, 'predictedTrend': PatternSignal.Bearish, 'patternType': PatternType.Reversal},
      {'low': 1, 'high': 100, 'currentTrend': TrendType.Indecision, 'predictedTrend': PatternSignal.Indecision, 'patternType': PatternType.Indecision},
      {'low': -100, 'high': -1, 'currentTrend': TrendType.Indecision, 'predictedTrend': PatternSignal.Indecision, 'patternType': PatternType.Indecision},
    ],
    'reliability': PatternReliability.N.name,
    # 'value': value,
    'img': '',
    'description': ['https://www.candlescanner.com/candlestick-patterns/high-wave/'],
  },

  # /* Proceed with the calculation for the requested range.
  #   * Must have:
  #   * - first and second candle: inside bar (2nd has lower high and higher low than 1st)
  #   * - third candle: lower high and lower low than 2nd (higher high and higher low than 2nd)
  #   * outInteger[hikkakebar] is positive (1 to 100) or negative (-1 to -100) meaning bullish or bearish hikkake
  #   * Confirmation could come in the next 3 days with:
  #   * - a day that closes higher than the high (lower than the low) of the 2nd candle
  #   * outInteger[confirmationbar] is equal to 100 + the bullish hikkake result or -100 - the bearish hikkake result
  #   * Note: if confirmation and a new hikkake come at the same bar, only the new hikkake is reported (the new hikkake
  #   * overwrites the confirmation of the old hikkake)
  #   */
  # # "https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDLHIKKAKE.c#l239"
  'CDLHIKKAKE': lambda value,trend: {
    'acceptableValues': [
      {'low': 101, 'high': 200 , 'currentTrend': TrendType.Downtrend, 'predictedTrend': PatternSignal.Bullish, 'patternType': PatternType.Reversal},
      {'low': 1, 'high': 100 , 'currentTrend': TrendType.Downtrend, 'predictedTrend': PatternSignal.Bullish, 'patternType': PatternType.Reversal},
      {'low': -100, 'high': -1, 'currentTrend': TrendType.Uptrend, 'predictedTrend': PatternSignal.Bearish, 'patternType': PatternType.Reversal},
      {'low': -200, 'high': -101, 'currentTrend': TrendType.Uptrend, 'predictedTrend': PatternSignal.Bearish, 'patternType': PatternType.Reversal},
    ],
    'reliability': PatternReliability.N.name,
    # 'value': value,
    'img': '',
    'description': ['https://www.investopedia.com/terms/m/modified-hikkake-pattern.asp'],
  },

  # /* Proceed with the calculation for the requested range.
  #   * Must have:
  #   * - first candle
  #   * - second candle: candle with range less than first candle and close near the bottom (near the top)
  #   * - third candle: lower high and higher low than 2nd
  #   * - fourth candle: lower high and lower low (higher high and higher low) than 3rd
  #   * outInteger[hikkake bar] is positive (1 to 100) or negative (-1 to -100) meaning bullish or bearish hikkake
  #   * Confirmation could come in the next 3 days with:
  #   * - a day that closes higher than the high (lower than the low) of the 3rd candle
  #   * outInteger[confirmationbar] is equal to 100 + the bullish hikkake result or -100 - the bearish hikkake result
  #   * Note: if confirmation and a new hikkake come at the same bar, only the new hikkake is reported (the new hikkake
  #   * overwrites the confirmation of the old hikkake);
  #   * the user should consider that modified hikkake is a reversal pattern, while hikkake could be both a reversal 
  #   * or a continuation pattern, so bullish (bearish) modified hikkake is significant when appearing in a downtrend 
  #   * (uptrend)
  #   */
  # # "https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDLHIKKAKEMOD.c#l239"
  'CDLHIKKAKEMOD': lambda value,trend: {
    'acceptableValues': [
      {'low': 101, 'high': 200 , 'currentTrend': TrendType.Downtrend, 'predictedTrend': PatternSignal.Bullish, 'patternType': PatternType.Reversal},
      {'low': 1, 'high': 100 , 'currentTrend': TrendType.Downtrend, 'predictedTrend': PatternSignal.Bullish, 'patternType': PatternType.Reversal},
      {'low': -100, 'high': -1, 'currentTrend': TrendType.Uptrend, 'predictedTrend': PatternSignal.Bearish, 'patternType': PatternType.Reversal},
      {'low': -200, 'high': -101, 'currentTrend': TrendType.Uptrend, 'predictedTrend': PatternSignal.Bearish, 'patternType': PatternType.Reversal},
    ],
    'reliability': PatternReliability.N.name,
    # 'value': value,
    'img': '',
    'description': ['https://www.investopedia.com/terms/m/modified-hikkake-pattern.asp'],
  },

  # /* Proceed with the calculation for the requested range.
  #   * Must have:
  #   * - first candle: long black candle
  #   * - second candle: short black real body completely inside the previous day's body
  #   * The meaning of "short" and "long" is specified with TA_SetCandleSettings
  #   * outInteger is positive (1 to 100): homing pigeon is always bullish; 
  #   * the user should consider that homing pigeon is significant when it appears in a downtrend,
  #   * while this function does not consider the trend
  #   */
  # # "https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDLHOMINGPIGEON.c#l239"
  'CDLHOMINGPIGEON': lambda value,trend: {
    'acceptableValues': [
      {'low': 1, 'high': 100, 'currentTrend': TrendType.Downtrend, 'predictedTrend': PatternSignal.Bullish, 'patternType': PatternType.Reversal},
    ],
    'reliability': PatternReliability.N.name,
    # 'value': value,
    'img': '',
    'description': ['https://www.investopedia.com/terms/b/bullishhomingpigeon.asp'],
  },

  # /* Proceed with the calculation for the requested range.
  #   * Must have:
  #   * - three consecutive and declining black candlesticks
  #   * - each candle must have no or very short lower shadow
  #   * - each candle after the first must open at or very close to the prior candle's close
  #   * The meaning of "very short" is specified with TA_SetCandleSettings;
  #   * the meaning of "very close" is specified with TA_SetCandleSettings (Equal);
  #   * outInteger is negative (-1 to -100): identical three crows is always bearish; 
  #   * the user should consider that identical 3 crows is significant when it appears after a mature advance or at high levels, 
  #   * while this function does not consider it
  #   */
  # https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDLIDENTICAL3CROWS.c#l239
  'CDLIDENTICAL3CROWS': lambda value,trend: {
    'acceptableValues': [
      {'low': -100, 'high': -1, 'currentTrend': TrendType.Uptrend, 'predictedTrend': PatternSignal.Bearish, 'patternType': PatternType.Reversal},
    ],
    'reliability': PatternReliability.N.name,
    # 'value': value,
    'img': '',
    'description': ['https://www.candlescanner.com/candlestick-patterns/identical-three-crows/'],
  },

  # /* Proceed with the calculation for the requested range.
  #   * Must have:
  #   * - first candle: long black candle
  #   * - second candle: white candle with open below previous day low and close slightly into previous day body
  #   * The meaning of "equal" is specified with TA_SetCandleSettings
  #   * outInteger is negative (-1 to -100): in-neck is always bearish
  #   * the user should consider that in-neck is significant when it appears in a downtrend, while this function 
  #   * does not consider it
  #   */
  # https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDLINNECK.c#l239
  'CDLINNECK': lambda value,trend: {
    'acceptableValues': [
      {'low': -100, 'high': -1, 'currentTrend': TrendType.Downtrend, 'predictedTrend': PatternSignal.Bearish, 'patternType': PatternType.Continuation},
    ],
    'reliability': PatternReliability.N.name,
    # 'value': value,
    'img': '',
    'description': ['https://www.candlescanner.com/candlestick-patterns/in-neck/'],
  },

  # /* Proceed with the calculation for the requested range.
  #   * Must have:
  #   * - small real body
  #   * - long upper shadow
  #   * - no, or very short, lower shadow
  #   * - gap down
  #   * The meaning of "short", "very short" and "long" is specified with TA_SetCandleSettings;
  #   * outInteger is positive (1 to 100): inverted hammer is always bullish;
  #   * the user should consider that an inverted hammer must appear in a downtrend, while this function does not consider it
  #   */
  # https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDLINVERTEDHAMMER.c#l239
  ## high. continuation. 65% bearish
  'CDLINVERTEDHAMMER': lambda value,trend: {
    'acceptableValues': [
      {'low': 1, 'high': 100, 'currentTrend': TrendType.Downtrend, 'predictedTrend': PatternSignal.Bullish, 'patternType': PatternType.Reversal},
    ],
    'reliability': PatternReliability.N.name,
    # 'value': value,
    'img': '',
    'description': ['https://commodity.com/technical-analysis/inverted-hammer/'],
  },

  # /* Proceed with the calculation for the requested range.
  #   * Must have:
  #   * - first candle: marubozu
  #   * - second candle: opposite color marubozu
  #   * - gap between the two candles: upside gap if black then white, downside gap if white then black
  #   * The meaning of "long body" and "very short shadow" is specified with TA_SetCandleSettings
  #   * outInteger is positive (1 to 100) when bullish or negative (-1 to -100) when bearish
  #   */
  # https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDLKICKING.c#l239
  'CDLKICKING': lambda value,trend: {
    'acceptableValues': [
      {'low': 1, 'high': 100, 'currentTrend': TrendType.Downtrend, 'predictedTrend': PatternSignal.Bullish, 'patternType': PatternType.Reversal},
      {'low': -100, 'high': -1, 'currentTrend': TrendType.Uptrend, 'predictedTrend': PatternSignal.Bearish, 'patternType': PatternType.Reversal},
    ],
    'reliability': PatternReliability.N.name,
    # 'value': value,
    'img': '',
    'description': ['https://www.investopedia.com/terms/k/kickerpattern.asp'],
  },

  # /* Proceed with the calculation for the requested range.
  #   * Must have:
  #   * - first candle: marubozu
  #   * - second candle: opposite color marubozu
  #   * - gap between the two candles: upside gap if black then white, downside gap if white then black
  #   * The meaning of "long body" and "very short shadow" is specified with TA_SetCandleSettings
  #   * outInteger is positive (1 to 100) when bullish or negative (-1 to -100) when bearish; the longer of the two
  #   * marubozu determines the bullishness or bearishness of this pattern
  #   */
  # https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDLKICKINGBYLENGTH.c#l239
  'CDLKICKINGBYLENGTH': lambda value,trend: {
    'acceptableValues': [
      {'low': 1, 'high': 100, 'currentTrend': TrendType.Downtrend, 'predictedTrend': PatternSignal.Bullish, 'patternType': PatternType.Reversal},
      {'low': -100, 'high': -1, 'currentTrend': TrendType.Uptrend, 'predictedTrend': PatternSignal.Bearish, 'patternType': PatternType.Reversal},
    ],
    'reliability': PatternReliability.N.name,
    # 'value': value,
    'img': '',
    'description': ['https://mudrex.com/indicators/102'],
  },

  # /* Proceed with the calculation for the requested range.
  #   * Must have:
  #   * - three black candlesticks with consecutively lower opens and closes
  #   * - fourth candle: black candle with an upper shadow (it's supposed to be not very short)
  #   * - fifth candle: white candle that opens above prior candle's body and closes above prior candle's high
  #   * The meaning of "very short" is specified with TA_SetCandleSettings
  #   * outInteger is positive (1 to 100): ladder bottom is always bullish; 
  #   * the user should consider that ladder bottom is significant when it appears in a downtrend, 
  #   * while this function does not consider it
  #   */
  # https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDLLADDERBOTTOM.c#l239
  'CDLLADDERBOTTOM': lambda value,trend: {
    'acceptableValues': [
      {'low': 1, 'high': 100, 'currentTrend': TrendType.Downtrend, 'predictedTrend': PatternSignal.Bullish, 'patternType': PatternType.Reversal},
      {'low': -100, 'high': -1, 'currentTrend': TrendType.Uptrend, 'predictedTrend': PatternSignal.Bearish, 'patternType': PatternType.Reversal},
    ],
    'reliability': PatternReliability.N.name,
    # 'value': value,
    'img': '',
    'description': ['https://www.investopedia.com/terms/l/ladder-bottom.asp'],
  },

  # /* Proceed with the calculation for the requested range.
  #   *
  #   * Must have:
  #   * - doji body
  #   * - one or two long shadows
  #   * The meaning of "doji" is specified with TA_SetCandleSettings
  #   * outInteger is always positive (1 to 100) but this does not mean it is bullish: long legged doji shows uncertainty
  #   */
  # https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDLLONGLEGGEDDOJI.c#l239
  'CDLLONGLEGGEDDOJI': lambda value,trend: {
    'acceptableValues': [
      {'low': 1, 'high': 100, 'currentTrend': TrendType.Indecision, 'predictedTrend': PatternSignal.Indecision, 'patternType': PatternType.Indecision},
    ],
    'reliability': PatternReliability.N.name,
    # 'value': value,
    'img': '',
    'description': ['https://www.investopedia.com/terms/l/long-legged-doji.asp'],
  },

  # /* Proceed with the calculation for the requested range.
  #   * Must have:
  #   * - long real body
  #   * - short upper and lower shadow
  #   * The meaning of "long" and "short" is specified with TA_SetCandleSettings
  #   * outInteger is positive (1 to 100) when white (bullish), negative (-1 to -100) when black (bearish)
  #   */
  # https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDLLONGLINE.c#l239
  'CDLLONGLINE': lambda value,trend: {
    'acceptableValues': [
      {'low': 1, 'high': 100, 'currentTrend': TrendType.Downtrend, 'predictedTrend': PatternSignal.Bullish, 'patternType': PatternType.Reversal},
      {'low': -100, 'high': -1, 'currentTrend': TrendType.Uptrend, 'predictedTrend': PatternSignal.Bearish, 'patternType': PatternType.Reversal},
    ],
    'reliability': PatternReliability.N.name,
    # 'value': value,
    'img': '',
    'description': ['https://www.feedroll.com/candlestick-patterns/1138-long-line-candle-short-line-candle/'],
  },

  # /* Proceed with the calculation for the requested range.
  #   * Must have:
  #   * - long real body
  #   * - no or very short upper and lower shadow
  #   * The meaning of "long" and "very short" is specified with TA_SetCandleSettings
  #   * outInteger is positive (1 to 100) when white (bullish), negative (-1 to -100) when black (bearish)
  #   */
  # https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDLMARUBOZU.c#l239
  'CDLMARUBOZU': lambda value,trend: {
    'acceptableValues': [
      {'low': 1, 'high': 100, 'currentTrend': TrendType.Downtrend, 'predictedTrend': PatternSignal.Bullish, 'patternType': PatternType.Reversal},
      {'low': -100, 'high': -1, 'currentTrend': TrendType.Uptrend, 'predictedTrend': PatternSignal.Bearish, 'patternType': PatternType.Reversal},
    ],
    'reliability': PatternReliability.N.name,
    # 'value': value,
    'img': '',
    'description': ['https://www.investopedia.com/stock-analysis/cotd/pot20120801.aspx'],
  },

  # /* Proceed with the calculation for the requested range.
  #   * Must have:
  #   * - first candle: black candle
  #   * - second candle: black candle with the close equal to the previous close
  #   * The meaning of "equal" is specified with TA_SetCandleSettings
  #   * outInteger is always positive (1 to 100): matching low is always bullish;
  #   */
  # https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDLMATCHINGLOW.c#l239
  ## high. continuation. 61% bearish
  'CDLMATCHINGLOW': lambda value,trend: {
    'acceptableValues': [
      {'low': 1, 'high': 100, 'currentTrend': TrendType.Downtrend, 'predictedTrend': PatternSignal.Bullish, 'patternType': PatternType.Reversal},
    ],
    'reliability': PatternReliability.N.name,
    # 'value': value,
    'img': '',
    'description': ['https://www.investopedia.com/terms/m/matching-low.asp'],
  },

  # /* Proceed with the calculation for the requested range.
  #   * Must have:
  #   * - first candle: long white candle
  #   * - upside gap between the first and the second bodies
  #   * - second candle: small black candle
  #   * - third and fourth candles: falling small real body candlesticks (commonly black) that hold within the long 
  #   *   white candle's body and are higher than the reaction days of the rising three methods
  #   * - fifth candle: white candle that opens above the previous small candle's close and closes higher than the 
  #   *   high of the highest reaction day
  #   * The meaning of "short" and "long" is specified with TA_SetCandleSettings; 
  #   * "hold within" means "a part of the real body must be within";
  #   * optInPenetration is the maximum percentage of the first white body the reaction days can penetrate (it is 
  #   * to specify how much the reaction days should be "higher than the reaction days of the rising three methods")
  #   * outInteger is positive (1 to 100): mat hold is always bullish
  #   */
  # https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDLMATHOLD.c#l239
  'CDLMATHOLD': lambda value,trend: {
    'acceptableValues': [
      {'low': 1, 'high': 100, 'currentTrend': TrendType.Uptrend, 'predictedTrend': PatternSignal.Bullish, 'patternType': PatternType.Continuation},
    ],
    'reliability': PatternReliability.N.name,
    # 'value': value,
    'img': '',
    'description': ['https://www.feedroll.com/candlestick-patterns/1148-mat-hold-pattern/'],
  },
  
  # /* Proceed with the calculation for the requested range.
  #   * Must have:
  #   * - first candle: long black real body
  #   * - second candle: doji gapping down
  #   * - third candle: white real body that moves well within the first candle's real body
  #   * The meaning of "doji" and "long" is specified with TA_SetCandleSettings
  #   * The meaning of "moves well within" is specified with optInPenetration and "moves" should mean the real body should
  #   * not be short ("short" is specified with TA_SetCandleSettings) - Greg Morris wants it to be long, someone else want
  #   * it to be relatively long
  #   * outInteger is positive (1 to 100): morning doji star is always bullish;
  #   * the user should consider that a morning star is significant when it appears in a downtrend, 
  #   * while this function does not consider the trend
  #   */
  # https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDLMORNINGDOJISTAR.c#l239
  'CDLMORNINGDOJISTAR': lambda value,trend: {
    'acceptableValues': [
      {'low': 1, 'high': 100, 'currentTrend': TrendType.Downtrend, 'predictedTrend': PatternSignal.Bullish, 'patternType': PatternType.Reversal},
    ],
    'reliability': PatternReliability.N.name,
    # 'value': value,
    'img': '',
    'description': ['https://www.candlescanner.com/candlestick-patterns/morning-doji-star/','https://wiki.timetotrade.com/Morning_Doji_Star_Candlestick'],
  },

  # /* Proceed with the calculation for the requested range.
  #   * Must have:
  #   * - first candle: long black real body
  #   * - second candle: star (Short real body gapping down)
  #   * - third candle: white real body that moves well within the first candle's real body
  #   * The meaning of "short" and "long" is specified with TA_SetCandleSettings
  #   * The meaning of "moves well within" is specified with optInPenetration and "moves" should mean the real body should
  #   * not be short ("short" is specified with TA_SetCandleSettings) - Greg Morris wants it to be long, someone else want
  #   * it to be relatively long
  #   * outInteger is positive (1 to 100): morning star is always bullish; 
  #   * the user should consider that a morning star is significant when it appears in a downtrend, 
  #   * while this function does not consider the trend
  #   */
  # https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDLMORNINGSTAR.c#l239
  'CDLMORNINGSTAR': lambda value,trend: {
    'acceptableValues': [
      {'low': 1, 'high': 100, 'currentTrend': TrendType.Downtrend, 'predictedTrend': PatternSignal.Bullish, 'patternType': PatternType.Reversal},
    ],
    'reliability': PatternReliability.N.name,
    # 'value': value,
    'img': '',
    'description': ['https://www.investopedia.com/terms/m/morningstar.asp','https://wiki.timetotrade.com/Morning_Star_Candlestick'],
  },

  # /* Proceed with the calculation for the requested range.
  #   * Must have:
  #   * - first candle: long black candle
  #   * - second candle: white candle with open below previous day low and close equal to previous day low
  #   * The meaning of "equal" is specified with TA_SetCandleSettings
  #   * outInteger is negative (-1 to -100): on-neck is always bearish
  #   * the user should consider that on-neck is significant when it appears in a downtrend, while this function 
  #   * does not consider it
  #   */
  # https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDLONNECK.c#l239
  'CDLONNECK': lambda value,trend: {
    'acceptableValues': [
      {'low': -100, 'high': -1, 'currentTrend': TrendType.Downtrend, 'predictedTrend': PatternSignal.Bearish, 'patternType': PatternType.Continuation},
    ],
    'reliability': PatternReliability.N.name,
    # 'value': value,
    'img': '',
    'description': ['https://www.investopedia.com/terms/n/neck-pattern.asp'],
  },

  # /* Proceed with the calculation for the requested range.
  #   * Must have:
  #   * - first candle: long black candle
  #   * - second candle: long white candle with open below previous day low and close at least at 50% of previous day 
  #   * real body
  #   * The meaning of "long" is specified with TA_SetCandleSettings
  #   * outInteger is positive (1 to 100): piercing pattern is always bullish
  #   * the user should consider that a piercing pattern is significant when it appears in a downtrend, while 
  #   * this function does not consider it
  #   */
  # https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDLPIERCING.c#l239
  'CDLPIERCING': lambda value,trend: {
    'acceptableValues': [
      {'low': 1, 'high': 100, 'currentTrend': TrendType.Downtrend, 'predictedTrend': PatternSignal.Bullish, 'patternType': PatternType.Reversal},
    ],
    'reliability': PatternReliability.N.name,
    # 'value': value,
    'img': '',
    'description': ['https://www.investopedia.com/terms/piercing-pattern.asp'],
  },

  
  # /* Proceed with the calculation for the requested range.
  #   *
  #   * Must have:
  #   * - doji body
  #   * - two long shadows
  #   * - body near the midpoint of the high-low range
  #   * The meaning of "doji" and "near" is specified with TA_SetCandleSettings
  #   * outInteger is always positive (1 to 100) but this does not mean it is bullish: rickshaw man shows uncertainty
  #   */
  # https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDLRICKSHAWMAN.c#l239
  'CDLRICKSHAWMAN': lambda value,trend: {
    'acceptableValues': [
      {'low': 1, 'high': 100, 'currentTrend': TrendType.Indecision, 'predictedTrend': PatternSignal.Indecision, 'patternType': PatternType.Indecision},
    ],
    'reliability': PatternReliability.N.name,
    # 'value': value,
    'img': '',
    'description': ['https://www.investopedia.com/terms/r/rickshaw-man.asp'],
  },
  
  # /* Proceed with the calculation for the requested range.
  #   * Must have:
  #   * - first candle: long white (black) candlestick
  #   * - then: group of falling (rising) small real body candlesticks (commonly black (white)) that hold within 
  #   *   the prior long candle's range: ideally they should be three but two or more than three are ok too
  #   * - final candle: long white (black) candle that opens above (below) the previous small candle's close 
  #   *   and closes above (below) the first long candle's close
  #   * The meaning of "short" and "long" is specified with TA_SetCandleSettings; here only patterns with 3 small candles
  #   * are considered;
  #   * outInteger is positive (1 to 100) or negative (-1 to -100)
  #   */
  # # "https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDLRISEFALL3METHODS.c#l239"
  'CDLRISEFALL3METHODS': lambda value,trend: {
    'acceptableValues': [
      {'low': 1, 'high': 100, 'currentTrend': TrendType.Uptrend, 'predictedTrend': PatternSignal.Bullish, 'patternType': PatternType.Continuation},
      {'low': -100, 'high': -1, 'currentTrend': TrendType.Downtrend, 'predictedTrend': PatternSignal.Bearish, 'patternType': PatternType.Continuation},
    ],
    'reliability': PatternReliability.N.name,
    # 'value': value,
    'img': '',
    'description': ['https://www.investopedia.com/terms/r/rising-three-methods.asp'],
  },

  # /* Proceed with the calculation for the requested range.
  #   * Must have:
  #   * - first candle: black (white) candle
  #   * - second candle: bullish (bearish) belt hold with the same open as the prior candle
  #   * The meaning of "long body" and "very short shadow" of the belt hold is specified with TA_SetCandleSettings
  #   * outInteger is positive (1 to 100) when bullish or negative (-1 to -100) when bearish;
  #   * the user should consider that separating lines is significant when coming in a trend and the belt hold has 
  #   * the same direction of the trend, while this function does not consider it
  #   */
  # # "https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDLSEPARATINGLINES.c#l239"
  'CDLSEPARATINGLINES': lambda value,trend: {
    'acceptableValues': [
      {'low': 1, 'high': 100, 'currentTrend': TrendType.Uptrend, 'predictedTrend': PatternSignal.Bullish, 'patternType': PatternType.Continuation},
      {'low': -100, 'high': -1, 'currentTrend': TrendType.Downtrend, 'predictedTrend': PatternSignal.Bearish, 'patternType': PatternType.Continuation},
    ],
    'reliability': PatternReliability.N.name,
    # 'value': value,
    'img': '',
    'description': ['https://therobusttrader.com/bullish-separating-lines-candlestick-pattern/'],
  },

  # /* Proceed with the calculation for the requested range.
  #   * Must have:
  #   * - small real body
  #   * - long upper shadow
  #   * - no, or very short, lower shadow
  #   * - gap up from prior real body
  #   * The meaning of "short", "very short" and "long" is specified with TA_SetCandleSettings;
  #   * outInteger is negative (-1 to -100): shooting star is always bearish;
  #   * the user should consider that a shooting star must appear in an uptrend, while this function does not consider it
  #   */
  # # http://tutorials.topstockresearch.com/candlestick/Bearish/ShootingStar/TutotrialOnShootingStarBearishChartPattern.html
  # # "https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDLSHOOTINGSTAR.c#l239"
  'CDLSHOOTINGSTAR': lambda value,trend: {
    'acceptableValues': [
      {'low': -100, 'high': -1, 'currentTrend': TrendType.Uptrend, 'predictedTrend': PatternSignal.Bearish, 'patternType': PatternType.Reversal},
    ],
    'reliability': PatternReliability.N.name,
    # 'value': value,
    'img': '',
    'description': ['https://www.investopedia.com/terms/s/shootingstar.asp'],
  },

  # /* Proceed with the calculation for the requested range.
  #   * Must have:
  #   * - short real body
  #   * - short upper and lower shadow
  #   * The meaning of "short" is specified with TA_SetCandleSettings
  #   * outInteger is positive (1 to 100) when white, negative (-1 to -100) when black;
  #   * it does not mean bullish or bearish
  #   */
  # # "https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDLSHORTLINE.c#l239"
  'CDLSHORTLINE': lambda value,trend: {
    'acceptableValues': [
      {'low': 1, 'high': 100, 'currentTrend': TrendType.Uptrend, 'predictedTrend': PatternSignal.Bullish, 'patternType': PatternType.Continuation},
      {'low': -100, 'high': -1, 'currentTrend': TrendType.Downtrend, 'predictedTrend': PatternSignal.Bearish, 'patternType': PatternType.Continuation},
    ],
    'reliability': PatternReliability.N.name,
    # 'value': value,
    'img': '',
    'description': ['https://www.investopedia.com/terms/s/short-line-candle.asp'],
  },

  # /* Proceed with the calculation for the requested range.
  #   * Must have:
  #   * - small real body
  #   * - shadows longer than the real body
  #   * The meaning of "short" is specified with TA_SetCandleSettings
  #   * outInteger is positive (1 to 100) when white or negative (-1 to -100) when black;
  #   * it does not mean bullish or bearish
  #   */
  # # "https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDLSPINNINGTOP.c#l239"
  'CDLSPINNINGTOP': lambda value,trend: {
    'acceptableValues': [
      {'low': 1, 'high': 100, 'currentTrend': TrendType.Downtrend, 'predictedTrend': PatternSignal.Bullish, 'patternType': PatternType.Reversal},
      {'low': -100, 'high': -1, 'currentTrend': TrendType.Uptrend, 'predictedTrend': PatternSignal.Bearish, 'patternType': PatternType.Reversal},
    ],
    'reliability': PatternReliability.N.name,
    # 'value': value,
    'img': '',
    'description': ['https://www.investopedia.com/terms/s/spinning-top.asp'],
  },

  # /* Proceed with the calculation for the requested range.
  #   * Must have:
  #   * - three white candlesticks with consecutively higher closes
  #   * - first candle: long white
  #   * - second candle: long white with no or very short upper shadow opening within or near the previous white real body
  #   * and closing higher than the prior candle
  #   * - third candle: small white that gaps away or "rides on the shoulder" of the prior long real body (= it's at 
  #   * the upper end of the prior real body)
  #   * The meanings of "long", "very short", "short", "near" are specified with TA_SetCandleSettings;
  #   * outInteger is negative (-1 to -100): stalled pattern is always bearish;
  #   * the user should consider that stalled pattern is significant when it appears in uptrend, while this function 
  #   * does not consider it
  #   */
  # # "https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDLSTALLEDPATTERN.c#l239"
  'CDLSTALLEDPATTERN': lambda value,trend: {
    'acceptableValues': [
      {'low': -100, 'high': -1, 'currentTrend': TrendType.Uptrend, 'predictedTrend': PatternSignal.Bearish, 'patternType': PatternType.Reversal},
    ],
    'reliability': PatternReliability.N.name,
    # 'value': value,
    'img': '',
    'description': ['https://www.investopedia.com/terms/s/stalled-pattern.asp'],
  },
  
  # /* Proceed with the calculation for the requested range.
  #   * Must have:
  #   * - first candle: black candle
  #   * - second candle: white candle that trades only above the prior close (low > prior close)
  #   * - third candle: black candle with the close equal to the first candle's close
  #   * The meaning of "equal" is specified with TA_SetCandleSettings
  #   * outInteger is always positive (1 to 100): stick sandwich is always bullish;
  #   * the user should consider that stick sandwich is significant when coming in a downtrend, 
  #   * while this function does not consider it
  #   */
  # # "https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDLSTICKSANDWICH.c#l239"
  'CDLSTICKSANDWICH': lambda value,trend: {
    'acceptableValues': [
      {'low': 1, 'high': 100, 'currentTrend': TrendType.Downtrend, 'predictedTrend': PatternSignal.Bullish, 'patternType': PatternType.Reversal},
    ],
    'reliability': PatternReliability.N.name,
    # 'value': value,
    'img': '',
    'description': ['https://www.investopedia.com/terms/s/stick-sandwich.asp'],
  },

  # /* Proceed with the calculation for the requested range.
  #   *
  #   * Must have:
  #   * - doji body
  #   * - open and close at the high of the day = no or very short upper shadow
  #   * - very long lower shadow
  #   * The meaning of "doji", "very short" and "very long" is specified with TA_SetCandleSettings
  #   * outInteger is always positive (1 to 100) but this does not mean it is bullish: takuri must be considered
  #   * relatively to the trend
  #   */
  # # "https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDLTAKURI.c#l239"
  'CDLTAKURI': lambda value,trend: {
    'acceptableValues': [
      {'low': 1, 'high': 100, 'currentTrend': TrendType.Downtrend, 'predictedTrend': PatternSignal.Bullish, 'patternType': PatternType.Reversal},
    ],
    'reliability': PatternReliability.N.name,
    # 'value': value,
    'img': '',
    'description': ['https://www.candlescanner.com/candlestick-patterns/takuri-line/'],
  },

  # /* Proceed with the calculation for the requested range.
  #   * Must have:
  #   * - upside (downside) gap
  #   * - first candle after the window: white (black) candlestick
  #   * - second candle: black (white) candlestick that opens within the previous real body and closes under (above)
  #   *   the previous real body inside the gap
  #   * - the size of two real bodies should be near the same
  #   * The meaning of "near" is specified with TA_SetCandleSettings
  #   * outInteger is positive (1 to 100) when bullish or negative (-1 to -100) when bearish;
  #   * the user should consider that tasuki gap is significant when it appears in a trend, while this function does 
  #   * not consider it
  #   */
  # # "https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDLTASUKIGAP.c#l239"
  ## high. continuation. 57% bullish 
  'CDLTASUKIGAP': lambda value,trend: {
    'acceptableValues': [
      {'low': 1, 'high': 100, 'currentTrend': TrendType.Uptrend, 'predictedTrend': PatternSignal.Bullish, 'patternType': PatternType.Continuation},
      {'low': -100, 'high': -1, 'currentTrend': TrendType.Downtrend, 'predictedTrend': PatternSignal.Bearish, 'patternType': PatternType.Continuation},
    ],
    'reliability': PatternReliability.N.name,
    # 'value': value,
    'img': '',
    'description': ['https://www.investopedia.com/terms/u/upside-tasuki-gap.asp'],
  },
  
  # /* Proceed with the calculation for the requested range.
  #   * Must have:
  #   * - first candle: long black candle
  #   * - second candle: white candle with open below previous day low and close into previous day body under the midpoint;
  #   * to differentiate it from in-neck the close should not be equal to the black candle's close
  #   * The meaning of "equal" is specified with TA_SetCandleSettings
  #   * outInteger is negative (-1 to -100): thrusting pattern is always bearish
  #   * the user should consider that the thrusting pattern is significant when it appears in a downtrend and it could be 
  #   * even bullish "when coming in an uptrend or occurring twice within several days" (Steve Nison says), while this 
  #   * function does not consider the trend
  #   */
  # # "https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDLTHRUSTING.c#l239"
  'CDLTHRUSTING': lambda value,trend: {
    'acceptableValues': [
      {'low': -100, 'high': -1, 'currentTrend': TrendType.Downtrend, 'predictedTrend': PatternSignal.Bearish, 'patternType': PatternType.Continuation},
    ],
    'reliability': PatternReliability.N.name,
    # 'value': value,
    'img': '',
    'description': ['https://www.investopedia.com/terms/t/thrusting-pattern.asp'],
  },

  # /* Proceed with the calculation for the requested range.
  #   * Must have:
  #   * - 3 consecutive doji days
  #   * - the second doji is a star
  #   * The meaning of "doji" is specified with TA_SetCandleSettings
  #   * outInteger is positive (1 to 100) when bullish or negative (-1 to -100) when bearish
  #   */
  # # "https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDLTRISTAR.c#l239"
  'CDLTRISTAR': lambda value,trend: {
    'acceptableValues': [
      {'low': 1, 'high': 100, 'currentTrend': TrendType.Downtrend, 'predictedTrend': PatternSignal.Bullish, 'patternType': PatternType.Reversal},
      {'low': -100, 'high': -1, 'currentTrend': TrendType.Uptrend, 'predictedTrend': PatternSignal.Bearish, 'patternType': PatternType.Reversal},
    ],
    'reliability': PatternReliability.N.name,
    # 'value': value,
    'img': '',
    'description': ['https://www.investopedia.com/terms/t/tri-star.asp'],
  },

  # /* Proceed with the calculation for the requested range.
  #   * Must have:
  #   * - first candle: long black candle
  #   * - second candle: black harami candle with a lower low than the first candle's low
  #   * - third candle: small white candle with open not lower than the second candle's low, better if its open and 
  #   *   close are under the second candle's close
  #   * The meaning of "short" and "long" is specified with TA_SetCandleSettings
  #   * outInteger is positive (1 to 100): unique 3 river is always bullish and should appear in a downtrend 
  #   * to be significant, while this function does not consider the trend
  #   */
  # # "https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDLUNIQUE3RIVER.c#l239"
  'CDLUNIQUE3RIVER': lambda value,trend: {
    'acceptableValues': [
      {'low': 1, 'high': 100, 'currentTrend': TrendType.Downtrend, 'predictedTrend': PatternSignal.Bullish, 'patternType': PatternType.Reversal},
    ],
    'reliability': PatternReliability.N.name,
    # 'value': value,
    'img': '',
    'description': ['https://www.investopedia.com/terms/u/unique-three-river.asp'],
  },

#####################################
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
  # # "https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDLUPSIDEGAP2CROWS.c#l239"
  'CDLUPSIDEGAP2CROWS': lambda value,trend: {
    'acceptableValues': [
      {'low': -100, 'high': -1, 'currentTrend': TrendType.Uptrend, 'predictedTrend': PatternSignal.Bearish, 'patternType': PatternType.Reversal},
    ],
    'reliability': PatternReliability.N.name,
    # 'value': value,
    'img': '',
    'description': ['https://www.investopedia.com/terms/u/upside-gap-two-crows.asp'],
  },

  # /* Proceed with the calculation for the requested range.
  #   * Must have:
  #   * - first candle: white (black) candle
  #   * - second candle: white (black) candle
  #   * - upside (downside) gap between the first and the second real bodies
  #   * - third candle: black (white) candle that opens within the second real body and closes within the first real body
  #   * outInteger is positive (1 to 100) when bullish or negative (-1 to -100) when bearish;
  #   * the user should consider that up/downside gap 3 methods is significant when it appears in a trend, while this 
  #   * function does not consider it
  #   */
  # # "https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDLXSIDEGAP3METHODS.c#l239"
  'CDLXSIDEGAP3METHODS': lambda value,trend: {
    'acceptableValues': [
      {'low': 1, 'high': 100, 'currentTrend': TrendType.Uptrend, 'predictedTrend': PatternSignal.Bullish, 'patternType': PatternType.Continuation},
      {'low': -100, 'high': -1, 'currentTrend': TrendType.Downtrend, 'predictedTrend': PatternSignal.Bearish, 'patternType': PatternType.Continuation},
    ],
    'reliability': PatternReliability.N.name,
    # 'value': value,
    'img': '',
    'description': ['https://www.investopedia.com/terms/u/upsidedownside-gap-three-methods.asp'],
  },
}

# still missing:
# - Two Black Gapping
# http://tutorials.topstockresearch.com/candlestick/Bearish/BearishKicker/TutorialOnBearishKickerCandlestickPattern.html

class PatternType(Enum): 
  Reversal = 0
  Continuation = 1
  Indecision = 2
  N = 3

class PatternSignal(Enum): 
  Bullish = 0 # up
  Bearish = 1 # down
  Indecision = 2 # dont know
  N = 3 # none

class PatternReliability(Enum):
  High = 0
  Moderate = 1
  Low = 3
  N = 4

class TrendType(Enum):
  Uptrend = 0
  Downtrend = 1
  Indecision = 2 # dont know

fetchDefaultOptions = {
  'group_by': 'ticker',
  'auto_adjust': False,
  'prepost': False,
  'threads': True,
  'proxy': None
}

shortTermOptions = {  # short term - 10 days
  'period': '1y',
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

indicatorsConfigurations = {
  'rsi': {
    'timeperiod': 14
  },
  'increasedVolumeIndicator': {
    'timeperiod': 3
  }
}

# 'PATTERN': lambda value,trend: {
#   'patternType': PatternType.N.name,
#   'patternSignal': PatternSignal.N.name if value > 0 else PatternSignal.N.name,
#   'reliability': PatternReliability.N.name,
#   # 'confirmedTrend': True if  value > 100 or value < -100 else False,
#   # 'value': value,
#   'link': '',
#   'ta-lib-description': """""",
#   'quantshare-description': """""",
#   'quantshare-info': """""",
# },