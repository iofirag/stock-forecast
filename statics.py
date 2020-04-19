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
# https://www.quantshare.com/index.php?option=manual&dir=/QuantShare%20Language/Candlestick%20Pattern/CdlEngulfing%201.html
# https://www.feedroll.com/candlestick-patterns/1309-index-candlestick-patterns/
# http://www.traderencyclopedia.com/wiki/index.php/Engulfing_line
# https://www.google.com/search?
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
  'CDL2CROWS': lambda value, trend: { # CDL2CROWS
    # 'patternValidation': lambda patternSignal, trend: expression
    'patternType': PatternType.Reversal.name,
    'acceptableValues': {
      PatternSignal.Bearish.name: {'min': -1, 'max': -100}
    },
    'patternSignal': PatternSignal.Bearish.name if value < 0 else PatternSignal.N.name,
    'reliability': PatternReliability.Moderate.name,
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': 'https://www.candlescanner.com/wp-content/uploads/2015/08/two-crows1.png',
    'ta-lib-description': """outInteger is negative (-1 to -100): two crows is always bearish; 
      the user should consider that two crows is significant when it appears in an uptrend, while this function 
      does not consider the trend""",
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
    'reliability': PatternReliability.Moderate.name,
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
  
  # /* Proceed with the calculation for the requested range.
  #   * Must have:
  #   * - first: black (white) real body
  #   * - second: white (black) real body that engulfs the prior real body
  #   * - third: candle that closes higher (lower) than the second candle
  #   * outInteger is positive (1 to 100) for the three outside up or negative (-1 to -100) for the three outside down;
  #   * the user should consider that a three outside up must appear in a downtrend and three outside down must appear
  #   * in an uptrend, while this function does not consider it
  #   */
  # 'CDL3OUTSIDE': CDL3OUTSIDE,
  # http://tutorials.topstockresearch.com/candlestick/Bearish/ThreeOutsideDown/TutotrialOnThreeOutsideDownPattern.html
  'CDL3OUTSIDE': lambda value,trend: {
    'conditions': {
      PatternSignal.Bullish.name: {'from': 1, 'to': 100, 'preTrend': PatternSignal.Bullish.name},
      PatternSignal.Bearish.name: {'from': -1, 'to': -100, 'preTrend': PatternSignal.Bearish.name},
    },
    'patternType': PatternType.Reversal.name,
    # 'patternSignal': PatternSignal.Bullish.name if value > 0 else PatternSignal.Bearish.name if value < 0 else PatternSignal.N.name,
    'reliability': PatternReliability.High.name,
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': 'http://www.tradingpedia.com/wp-content/uploads/2014/02/1.-Evening-star.jpg',
    'ta-lib-description': """outInteger is positive (1 to 100) for the three outside up or negative (-1 to -100) for the three outside down;
      the user should consider that a three outside up must appear in a downtrend and three outside down must appear
      in an uptrend, while this function does not consider it""",
    'quantshare-description': """""",
    'quantshare-info': """""",
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
  'CDL3STARSINSOUTH': lambda value,trend: {
    'patternType': PatternType.Reversal.name,
    'patternSignal': PatternSignal.Bullish.name if value > 0 else PatternSignal.N.name,
    'reliability': PatternReliability.Moderate.name,
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': 'https://hitandruncandlesticks.com/wp-content/uploads/2016/08/bullish_three_stars_in_the_south.jpg',
    'ta-lib-description': """outInteger is positive (1 to 100): 3 stars in the south is always bullish;
      the user should consider that 3 stars in the south is significant when it appears in downtrend, while this function 
      does not consider it""",
    'quantshare-description': """Three Stars In The South, The slow down of the trend is visually obvious.""",
    'quantshare-info': """""",
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
  'CDL3WHITESOLDIERS': lambda value,trend: {
    'patternType': PatternType.Reversal.name,
    'patternSignal': PatternSignal.Bullish.name if value > 0 else PatternSignal.N.name,
    'reliability': PatternReliability.High.name,
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': 'https://tutorials.topstockresearch.com/candlestick/Bullish/ThreeWhiteSoldiers/ThreeWhiteSoldiers.png',
    'ta-lib-description': """here the 3 candles must be not short, if you want them to be long use TA_SetCandleSettings on BodyShort;
      outInteger is positive (1 to 100): advancing 3 white soldiers is always bullish;
      the user should consider that 3 white soldiers is significant when it appears in downtrend, while this function 
      does not consider it""",
    'quantshare-description': """Three Advancing White Soldiers, The Three White Soldiers 
    (also known as The Advancing Three White Soldiers) is a healthy market reversal pattern""",
    'quantshare-info': """""",
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
  'CDLABANDONEDBABY': lambda value,trend: {
    'patternType': PatternType.Reversal.name,
    'patternSignal': PatternSignal.Bullish.name if value > 0 else PatternSignal.Bearish.name if value < 0 else PatternSignal.N.name,
    'reliability': PatternReliability.High.name,
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': 'https://mr-uploads.s3.amazonaws.com/uploads/2014/12/abandoned-baby2.png',
    'ta-lib-description': """outInteger is positive (1 to 100) when it's an abandoned baby bottom or negative (-1 to -100) when it's 
      an abandoned baby top; the user should consider that an abandoned baby is significant when it appears in 
      an uptrend or downtrend, while this function does not consider the trend""",
    'quantshare-description': """""",
    'quantshare-info': """70% in bullish""",
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
  'CDLADVANCEBLOCK': lambda value,trend: {
    'patternType': PatternType.Reversal.name,
    'patternSignal': PatternSignal.Bearish.name if value < 0 else PatternSignal.N.name,
    'reliability': PatternReliability.Moderate.name,
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': 'https://www.investopedia.com/thmb/tdbMb6qVoafr7S-lAQKjKpiTZaI=/1538x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/dotdash_Final_Advance_Block_Feb_2020-2f102ad610704541ad0583c14d4bbd7a.jpg',
    'ta-lib-description': """outInteger is negative (-1 to -100): advance block is always bearish;
      the user should consider that advance block is significant when it appears in uptrend, while this function 
      does not consider it""",
    'quantshare-description': """""",
    'quantshare-info': """""",
  },

  # /* Proceed with the calculation for the requested range.
  #   * Must have:
  #   * - long white (black) real body
  #   * - no or very short lower (upper) shadow
  #   * The meaning of "long" and "very short" is specified with TA_SetCandleSettings
  #   * outInteger is positive (1 to 100) when white (bullish), negative (-1 to -100) when black (bearish)
  #   */
  'CDLBELTHOLD': lambda value,trend: {
    'patternType': PatternType.Reversal.name,
    'patternSignal': PatternSignal.Bullish.name if value > 0 else PatternSignal.Bearish.name if value < 0 else PatternSignal.N.name,
    'reliability': PatternReliability.Low.name,
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': 'https://i.ytimg.com/vi/we62RExJrxM/maxresdefault.jpg',
    'ta-lib-description': """outInteger is positive (1 to 100) when white (bullish), negative (-1 to -100) when black (bearish)""",
    'quantshare-description': """Belt-hold, The Belt Hold lines are formed by single candlesticks.""",
    'quantshare-info': """""",
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
  'CDLBREAKAWAY': lambda value,trend: {
    'patternType': PatternType.Reversal.name,
    'patternSignal': PatternSignal.Bullish.name if value > 0 else PatternSignal.Bearish.name if value < 0 else PatternSignal.N.name,
    'reliability': PatternReliability.Moderate.name,
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': 'https://investorshub.advfn.com/uimage/uploads/2018/1/15/gnshqbreakaway-patterns.png',
    'ta-lib-description': """outInteger is positive (1 to 100) when bullish or negative (-1 to -100) when bearish;
      the user should consider that breakaway is significant in a trend opposite to the last candle, while this 
      function does not consider it""",
    'quantshare-description': """Breakaway, If a trend has been evident, the breakaway pattern, whether bullish or bearish initially indicates the acceleration of that trend.""",
    'quantshare-info': """""",
  },
  
  # /* Proceed with the calculation for the requested range.
  #   * Must have:
  #   * - long white (black) real body
  #   * - no or very short upper (lower) shadow
  #   * The meaning of "long" and "very short" is specified with TA_SetCandleSettings
  #   * outInteger is positive (1 to 100) when white (bullish), negative (-1 to -100) when black (bearish)
  #   */
  'CDLCLOSINGMARUBOZU': lambda value,trend: {
    'patternType': f'{PatternType.Continuation.name} 54% /{PatternType.Reversal.name} 46%',
    'patternSignal': PatternSignal.Bullish.name if value > 0 else PatternSignal.Bearish.name if value < 0 else PatternSignal.N.name,
    'reliability': PatternReliability.Low.name,
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': 'https://www.elearnmarkets.com/blog/wp-content/uploads/2016/03/CLOSING-MARUBOZU-CANDLESTICKS.jpg',
    'ta-lib-description': """outInteger is positive (1 to 100) when white (bullish), negative (-1 to -100) when black (bearish)""",
    'quantshare-description': """Closing Marubozu, a Closing Marubozu has no shadow at it's closing end.""",
    'quantshare-info': """This is an extremely strong candlestick pattern""",
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
  'CDLCONCEALBABYSWALL': lambda value,trend: {
    'patternType': PatternType.Reversal.name,
    'patternSignal': PatternSignal.Bullish.name if value > 0 else PatternSignal.N.name,
    'reliability': PatternReliability.High.name,
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': 'https://www.candlescanner.com/wp-content/uploads/2015/08/cancealing-baby-swallow.png',
    'ta-lib-description': """outInteger is positive (1 to 100): concealing baby swallow is always bullish;
      the user should consider that concealing baby swallow is significant when it appears in downtrend, while 
      this function does not consider it""",
    'quantshare-description': """Concealing Baby Swallow, The first two days of the signal, two Black Marubozus, demonstrate the continuation of the downtrend.""",
    'quantshare-info': """""",
  },

  # /* Proceed with the calculation for the requested range.
  #   * Must have:
  #   * - first candle: long black (white)
  #   * - second candle: long white (black) with close equal to the prior close
  #   * The meaning of "equal" and "long" is specified with TA_SetCandleSettings
  #   * outInteger is positive (1 to 100) when bullish or negative (-1 to -100) when bearish;
  #   * the user should consider that counterattack is significant in a trend, while this function does not consider it
  #   */
  'CDLCOUNTERATTACK': lambda value,trend: {
    'patternType': PatternType.Reversal.name,
    'patternSignal': PatternSignal.Bullish.name if value > 0 else PatternSignal.Bearish.name if value < 0 else PatternSignal.N.name,
    'reliability': PatternReliability.N.name,
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': 'http://www.traderencyclopedia.com/wiki/images/8/8c/Counterattack.jpg',
    'ta-lib-description': """outInteger is positive (1 to 100) when bullish or negative (-1 to -100) when bearish;
      the user should consider that counterattack is significant in a trend, while this function does not consider it""",
    'quantshare-description': """Counterattack, Meeting Lines (or Counterattack Lines) are formed when opposite coloured bodies have the same closing price.""",
    'quantshare-info': """The counter attack pattern warns that the tide is turning.""",
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
  'CDLDARKCLOUDCOVER': lambda value,trend: {
    'patternType': PatternType.Reversal.name,
    'patternSignal': PatternSignal.Bearish.name if value < 0 else PatternSignal.N.name,
    'reliability': PatternReliability.High.name,
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': 'https://mr-uploads.s3.amazonaws.com/uploads/2014/12/dark-cloud-cover1.png',
    'ta-lib-description': """outInteger is negative (-1 to -100): dark cloud cover is always bearish
      the user should consider that a dark cloud cover is significant when it appears in an uptrend, while 
      this function does not consider it""",
    'quantshare-description': """Dark Cloud Cover, The dark Cloud Cover is the bearish counterpart to the Piercing pattern.""",
    'quantshare-info': """Normally it should be a signal of bearish reversal of the current Trend.""",
  },

  # /* Proceed with the calculation for the requested range.
  #   *
  #   * Must have:
  #   * - open quite equal to close
  #   * How much can be the maximum distance between open and close is specified with TA_SetCandleSettings
  #   * outInteger is always positive (1 to 100) but this does not mean it is bullish: doji shows uncertainty and it is
  #   * neither bullish nor bearish when considered alone
  #   */
  'CDLDOJI': lambda value,trend: {
    'patternType': PatternType.Indecision.name,
    'patternSignal': PatternSignal.Indecision.name if value > 0 or value < 0 else PatternSignal.N.name,
    'reliability': PatternReliability.Low.name,
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': 'https://a.c-dn.net/b/3K4xiq/doji-candlestick-pattern_body_standarddoji.png',
    'ta-lib-description': """outInteger is always positive (1 to 100) but this does not mean it is bullish: doji shows uncertainty and it is
      neither bullish nor bearish when considered alone""",
    'quantshare-description': """Doji, taken alone, is a neutral pattern.""",
    'quantshare-info': """""",
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
  'CDLDOJISTAR': lambda value,trend: {
    'patternType': PatternType.Reversal.name,
    'patternSignal': PatternSignal.Bullish.name if value > 0 else PatternSignal.Bearish.name if value < 0 else PatternSignal.N.name,
    'reliability': PatternReliability.Moderate.name,
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': 'https://a.c-dn.net/b/3K4xiq/doji-candlestick-pattern_body_standarddoji.png',
    'ta-lib-description': """outInteger is positive (1 to 100) when bullish or negative (-1 to -100) when bearish; 
      it's defined bullish when the long candle is white and the star gaps up, bearish when the long candle 
      is black and the star gaps down; the user should consider that a doji star is bullish when it appears 
      in an uptrend and it's bearish when it appears in a downtrend, so to determine the bullishness or 
      bearishness of the pattern the trend must be analyzed""",
    'quantshare-description': """Doji Star, Upon seeing a Doji in an overbought or oversold condition, 
      an extremely high probability reversal situation becomes evident.""",
    'quantshare-info': """""",
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
  'CDLDRAGONFLYDOJI': lambda value,trend: {
    'patternType': PatternType.Reversal.name,
    'patternSignal': PatternSignal.Bullish.name if value > 0 else PatternSignal.N.name,
    'reliability': f'{PatternReliability.Low.name}/{PatternReliability.Moderate.name}',
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': 'https://tradingcryptocourse.com/wp-content/uploads/2018/11/candlestickpattern7.jpg',
    'ta-lib-description': """The meaning of "doji" and "very short" is specified with TA_SetCandleSettings
      outInteger is always positive (1 to 100) but this does not mean it is bullish: dragonfly doji must be considered
      relatively to the trend""",
    'description': """If it occurs during a Downtrend, especially if near a Low of the Trend, it means a possible bullish reversal.""",
    'quantshare-info': """""",
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
  # https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDLENGULFING.c#l212
  # high
  # http://tutorials.topstockresearch.com/candlestick/Bearish/BearishEngulfing/TutotrialOnBearishEngulfingChartPattern.html
  'CDLENGULFING': lambda value,trend: {
    'patternType': PatternType.Reversal.name,
    'patternSignal': PatternSignal.Bullish.name if value > 0 else PatternSignal.Bearish.name if value < 0 else PatternSignal.N.name,
    'reliability': PatternReliability.Moderate.name,
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': 'https://forextraininggroup.com/wp-content/uploads/2016/11/Engulfing-Pattern-Stop-Loss.png',
    'ta-lib-description': """outInteger is positive (1 to 100) when bullish or negative (-1 to -100) when bearish:
      - 100 is returned when the second candle's real body begins before and ends after the first candle's real body
      - 80 is returned when the two real bodies match on one end (Greg Morris contemplate this case in his book
        "Candlestick charting explained")
      The user should consider that an engulfing must appear in a downtrend if bullish or in an uptrend if bearish,
      while this function does not consider it""",
    'quantshare-description': """Engulfing Pattern, Two of the most compelling candlestick signals are the Bullish 
      Engulfing Pattern and Bearish Engulfing Pattern.""",
    'quantshare-info': """""",
  },
  
  #########################
  
  'CDLEVENINGDOJISTAR': lambda value,trend: {
    'patternType': PatternType.N.name,
    'patternSignal': PatternSignal.N.name if value > 0 else PatternSignal.N.name,
    'reliability': PatternReliability.N.name,
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': '',
    'ta-lib-description': """""",
    'quantshare-description': """""",
    'quantshare-info': """""",
  },

  ## high. reversal. 72% bearish
  # http://tutorials.topstockresearch.com/candlestick/Bearish/EveningStar/TutotrialOnEveningStarChartPattern.html
  'CDLEVENINGSTAR': lambda value,trend: {
    'patternType': PatternType.N.name,
    'patternSignal': PatternSignal.N.name if value > 0 else PatternSignal.N.name,
    'reliability': PatternReliability.N.name,
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': '',
    'ta-lib-description': """""",
    'quantshare-description': """""",
    'quantshare-info': """""",
  },

  'CDLGAPSIDESIDEWHITE': lambda value,trend: {
    'patternType': PatternType.N.name,
    'patternSignal': PatternSignal.N.name if value > 0 else PatternSignal.N.name,
    'reliability': PatternReliability.N.name,
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': '',
    'ta-lib-description': """""",
    'quantshare-description': """""",
    'quantshare-info': """""",
  },

  # http://tutorials.topstockresearch.com/candlestick/Bearish/GravestoneDoji/TutotrialOnGravestoneDojiBearishChartPattern.html
  'CDLGRAVESTONEDOJI': lambda value,trend: {
    'patternType': PatternType.N.name,
    'patternSignal': PatternSignal.N.name if value > 0 else PatternSignal.N.name,
    'reliability': PatternReliability.N.name,
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': '',
    'ta-lib-description': """""",
    'quantshare-description': """""",
    'quantshare-info': """""",
  },
  'CDLHAMMER': lambda value,trend: {
    'patternType': PatternType.N.name,
    'patternSignal': PatternSignal.N.name if value > 0 else PatternSignal.N.name,
    'reliability': PatternReliability.N.name,
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': '',
    'ta-lib-description': """""",
    'quantshare-description': """""",
    'quantshare-info': """""",
  },

  # http://tutorials.topstockresearch.com/candlestick/Bearish/HangingMan/TutotrialOnHangingManBearishChartPattern.html
  'CDLHANGINGMAN': lambda value,trend: {
    'patternType': PatternType.N.name,
    'patternSignal': PatternSignal.N.name if value > 0 else PatternSignal.N.name,
    'reliability': PatternReliability.N.name,
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': '',
    'ta-lib-description': """""",
    'quantshare-description': """""",
    'quantshare-info': """""",
  },

  # http://tutorials.topstockresearch.com/candlestick/Bearish/BearishHarami/TutotrialOnBearishHaramiChartPattern.html
  'CDLHARAMI': lambda value,trend: {
    'patternType': PatternType.N.name,
    'patternSignal': PatternSignal.N.name if value > 0 else PatternSignal.N.name,
    'reliability': PatternReliability.N.name,
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': '',
    'ta-lib-description': """""",
    'quantshare-description': """""",
    'quantshare-info': """""",
  },
  'CDLHARAMICROSS': lambda value,trend: {
    'patternType': PatternType.N.name,
    'patternSignal': PatternSignal.N.name if value > 0 else PatternSignal.N.name,
    'reliability': PatternReliability.N.name,
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': '',
    'ta-lib-description': """""",
    'quantshare-description': """""",
    'quantshare-info': """""",
  },
  'CDLHIGHWAVE': lambda value,trend: {
    'patternType': PatternType.N.name,
    'patternSignal': PatternSignal.N.name if value > 0 else PatternSignal.N.name,
    'reliability': PatternReliability.N.name,
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': '',
    'ta-lib-description': """""",
    'quantshare-description': """""",
    'quantshare-info': """""",
  },
  'CDLHIKKAKE': lambda value,trend: {
    'patternType': PatternType.N.name,
    'patternSignal': PatternSignal.N.name if value > 0 else PatternSignal.N.name,
    'reliability': PatternReliability.N.name,
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': '',
    'ta-lib-description': """""",
    'quantshare-description': """""",
    'quantshare-info': """""",
  },
  'CDLHIKKAKEMOD': lambda value,trend: {
    'patternType': PatternType.N.name,
    'patternSignal': PatternSignal.N.name if value > 0 else PatternSignal.N.name,
    'reliability': PatternReliability.N.name,
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': '',
    'ta-lib-description': """""",
    'quantshare-description': """""",
    'quantshare-info': """""",
  },
  'CDLHOMINGPIGEON': lambda value,trend: {
    'patternType': PatternType.N.name,
    'patternSignal': PatternSignal.N.name if value > 0 else PatternSignal.N.name,
    'reliability': PatternReliability.N.name,
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': '',
    'ta-lib-description': """""",
    'quantshare-description': """""",
    'quantshare-info': """""",
  },
  'CDLIDENTICAL3CROWS': lambda value,trend: {
    'patternType': PatternType.N.name,
    'patternSignal': PatternSignal.N.name if value > 0 else PatternSignal.N.name,
    'reliability': PatternReliability.N.name,
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': '',
    'ta-lib-description': """""",
    'quantshare-description': """""",
    'quantshare-info': """""",
  },
  'CDLINNECK': lambda value,trend: {
    'patternType': PatternType.N.name,
    'patternSignal': PatternSignal.N.name if value > 0 else PatternSignal.N.name,
    'reliability': PatternReliability.N.name,
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': '',
    'ta-lib-description': """""",
    'quantshare-description': """""",
    'quantshare-info': """""",
  },

  ## high. continuation. 65% bearish
  'CDLINVERTEDHAMMER': lambda value,trend: {
    'patternType': PatternType.N.name,
    'patternSignal': PatternSignal.N.name if value > 0 else PatternSignal.N.name,
    'reliability': PatternReliability.N.name,
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': '',
    'ta-lib-description': """""",
    'quantshare-description': """""",
    'quantshare-info': """""",
  },

  'CDLKICKING': lambda value,trend: {
    'patternType': PatternType.N.name,
    'patternSignal': PatternSignal.N.name if value > 0 else PatternSignal.N.name,
    'reliability': PatternReliability.N.name,
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': '',
    'ta-lib-description': """""",
    'quantshare-description': """""",
    'quantshare-info': """""",
  },
  'CDLKICKINGBYLENGTH': lambda value,trend: {
    'patternType': PatternType.N.name,
    'patternSignal': PatternSignal.N.name if value > 0 else PatternSignal.N.name,
    'reliability': PatternReliability.N.name,
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': '',
    'ta-lib-description': """""",
    'quantshare-description': """""",
    'quantshare-info': """""",
  },
  'CDLLADDERBOTTOM': lambda value,trend: {
    'patternType': PatternType.N.name,
    'patternSignal': PatternSignal.N.name if value > 0 else PatternSignal.N.name,
    'reliability': PatternReliability.N.name,
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': '',
    'ta-lib-description': """""",
    'quantshare-description': """""",
    'quantshare-info': """""",
  },
  'CDLLONGLEGGEDDOJI': lambda value,trend: {
    'patternType': PatternType.N.name,
    'patternSignal': PatternSignal.N.name if value > 0 else PatternSignal.N.name,
    'reliability': PatternReliability.N.name,
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': '',
    'ta-lib-description': """""",
    'quantshare-description': """""",
    'quantshare-info': """""",
  },
  'CDLLONGLINE': lambda value,trend: {
    'patternType': PatternType.N.name,
    'patternSignal': PatternSignal.N.name if value > 0 else PatternSignal.N.name,
    'reliability': PatternReliability.N.name,
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': '',
    'ta-lib-description': """""",
    'quantshare-description': """""",
    'quantshare-info': """""",
  },
  'CDLMARUBOZU': lambda value,trend: {
    'patternType': PatternType.N.name,
    'patternSignal': PatternSignal.N.name if value > 0 else PatternSignal.N.name,
    'reliability': PatternReliability.N.name,
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': '',
    'ta-lib-description': """""",
    'quantshare-description': """""",
    'quantshare-info': """""",
  },

  ## high. continuation. 61% bearish
  'CDLMATCHINGLOW': lambda value,trend: {
    'patternType': PatternType.N.name,
    'patternSignal': PatternSignal.N.name if value > 0 else PatternSignal.N.name,
    'reliability': PatternReliability.N.name,
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': '',
    'ta-lib-description': """""",
    'quantshare-description': """""",
    'quantshare-info': """""",
  },

  'CDLMATHOLD': lambda value,trend: {
    'patternType': PatternType.N.name,
    'patternSignal': PatternSignal.N.name if value > 0 else PatternSignal.N.name,
    'reliability': PatternReliability.N.name,
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': '',
    'ta-lib-description': """""",
    'quantshare-description': """""",
    'quantshare-info': """""",
  },
  'CDLMORNINGDOJISTAR': lambda value,trend: {
    'patternType': PatternType.N.name,
    'patternSignal': PatternSignal.N.name if value > 0 else PatternSignal.N.name,
    'reliability': PatternReliability.N.name,
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': '',
    'ta-lib-description': """""",
    'quantshare-description': """""",
    'quantshare-info': """""",
  },
  'CDLMORNINGSTAR': lambda value,trend: {
    'patternType': PatternType.N.name,
    'patternSignal': PatternSignal.N.name if value > 0 else PatternSignal.N.name,
    'reliability': PatternReliability.N.name,
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': '',
    'ta-lib-description': """""",
    'quantshare-description': """""",
    'quantshare-info': """""",
  },
  'CDLONNECK': lambda value,trend: {
    'patternType': PatternType.N.name,
    'patternSignal': PatternSignal.N.name if value > 0 else PatternSignal.N.name,
    'reliability': PatternReliability.N.name,
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': '',
    'ta-lib-description': """""",
    'quantshare-description': """""",
    'quantshare-info': """""",
  },
  'CDLPIERCING': lambda value,trend: {
    'patternType': PatternType.N.name,
    'patternSignal': PatternSignal.N.name if value > 0 else PatternSignal.N.name,
    'reliability': PatternReliability.N.name,
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': '',
    'ta-lib-description': """""",
    'quantshare-description': """""",
    'quantshare-info': """""",
  },
  'CDLRICKSHAWMAN': lambda value,trend: {
    'patternType': PatternType.N.name,
    'patternSignal': PatternSignal.N.name if value > 0 else PatternSignal.N.name,
    'reliability': PatternReliability.N.name,
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': '',
    'ta-lib-description': """""",
    'quantshare-description': """""",
    'quantshare-info': """""",
  },
  'CDLRISEFALL3METHODS': lambda value,trend: {
    'patternType': PatternType.N.name,
    'patternSignal': PatternSignal.N.name if value > 0 else PatternSignal.N.name,
    'reliability': PatternReliability.N.name,
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': '',
    'ta-lib-description': """""",
    'quantshare-description': """""",
    'quantshare-info': """""",
  },
  'CDLSEPARATINGLINES': lambda value,trend: {
    'patternType': PatternType.N.name,
    'patternSignal': PatternSignal.N.name if value > 0 else PatternSignal.N.name,
    'reliability': PatternReliability.N.name,
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': '',
    'ta-lib-description': """""",
    'quantshare-description': """""",
    'quantshare-info': """""",
  },

  # http://tutorials.topstockresearch.com/candlestick/Bearish/ShootingStar/TutotrialOnShootingStarBearishChartPattern.html
  'CDLSHOOTINGSTAR': lambda value,trend: {
    'patternType': PatternType.N.name,
    'patternSignal': PatternSignal.N.name if value > 0 else PatternSignal.N.name,
    'reliability': PatternReliability.N.name,
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': '',
    'ta-lib-description': """""",
    'quantshare-description': """""",
    'quantshare-info': """""",
  },
  'CDLSHORTLINE': lambda value,trend: {
    'patternType': PatternType.N.name,
    'patternSignal': PatternSignal.N.name if value > 0 else PatternSignal.N.name,
    'reliability': PatternReliability.N.name,
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': '',
    'ta-lib-description': """""",
    'quantshare-description': """""",
    'quantshare-info': """""",
  },
  'CDLSPINNINGTOP': lambda value,trend: {
    'patternType': PatternType.N.name,
    'patternSignal': PatternSignal.N.name if value > 0 else PatternSignal.N.name,
    'reliability': PatternReliability.N.name,
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': '',
    'ta-lib-description': """""",
    'quantshare-description': """""",
    'quantshare-info': """""",
  },
  'CDLSTALLEDPATTERN': lambda value,trend: {
    'patternType': PatternType.N.name,
    'patternSignal': PatternSignal.N.name if value > 0 else PatternSignal.N.name,
    'reliability': PatternReliability.N.name,
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': '',
    'ta-lib-description': """""",
    'quantshare-description': """""",
    'quantshare-info': """""",
  },
  'CDLSTICKSANDWICH': lambda value,trend: {
    'patternType': PatternType.N.name,
    'patternSignal': PatternSignal.N.name if value > 0 else PatternSignal.N.name,
    'reliability': PatternReliability.N.name,
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': '',
    'ta-lib-description': """""",
    'quantshare-description': """""",
    'quantshare-info': """""",
  },
  'CDLTAKURI': lambda value,trend: {
    'patternType': PatternType.N.name,
    'patternSignal': PatternSignal.N.name if value > 0 else PatternSignal.N.name,
    'reliability': PatternReliability.N.name,
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': '',
    'ta-lib-description': """""",
    'quantshare-description': """""",
    'quantshare-info': """""",
  },

  ## high. continuation. 57% bullish 
  'CDLTASUKIGAP': lambda value,trend: {
    'patternType': PatternType.N.name,
    'patternSignal': PatternSignal.N.name if value > 0 else PatternSignal.N.name,
    'reliability': PatternReliability.N.name,
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': '',
    'ta-lib-description': """""",
    'quantshare-description': """""",
    'quantshare-info': """""",
  },
  
  'CDLTHRUSTING': lambda value,trend: {
    'patternType': PatternType.N.name,
    'patternSignal': PatternSignal.N.name if value > 0 else PatternSignal.N.name,
    'reliability': PatternReliability.N.name,
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': '',
    'ta-lib-description': """""",
    'quantshare-description': """""",
    'quantshare-info': """""",
  },
  'CDLTRISTAR': lambda value,trend: {
    'patternType': PatternType.N.name,
    'patternSignal': PatternSignal.N.name if value > 0 else PatternSignal.N.name,
    'reliability': PatternReliability.N.name,
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': '',
    'ta-lib-description': """""",
    'quantshare-description': """""",
    'quantshare-info': """""",
  },
  'CDLUNIQUE3RIVER': lambda value,trend: {
    'patternType': PatternType.N.name,
    'patternSignal': PatternSignal.N.name if value > 0 else PatternSignal.N.name,
    'reliability': PatternReliability.N.name,
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': '',
    'ta-lib-description': """""",
    'quantshare-description': """""",
    'quantshare-info': """""",
  },

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
  'CDLUPSIDEGAP2CROWS': lambda value,trend: {
    'patternType': PatternType.N.name,
    'patternSignal': PatternSignal.N.name if value > 0 else PatternSignal.N.name,
    'reliability': PatternReliability.N.name,
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': '',
    'ta-lib-description': """""",
    'quantshare-description': """""",
    'quantshare-info': """""",
  },
  
  'CDLXSIDEGAP3METHODS': lambda value,trend: {
    'patternType': PatternType.N.name,
    'patternSignal': PatternSignal.N.name if value > 0 else PatternSignal.N.name,
    'reliability': PatternReliability.N.name,
    # 'confirmedTrend': True if  value > 100 or value < -100 else False,
    'value': value,
    'link': '',
    'ta-lib-description': """""",
    'quantshare-description': """""",
    'quantshare-info': """""",
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
#   'value': value,
#   'link': '',
#   'ta-lib-description': """""",
#   'quantshare-description': """""",
#   'quantshare-info': """""",
# },