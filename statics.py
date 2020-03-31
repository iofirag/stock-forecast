tickerList = ['BEZQ.TA', 'DSCT.TA']
# tickerList = ['SPY','MSFT','GOOGL','TEVA','BEZQ.TA']

# https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/
candleStickSwitcher = {    
  'CDL2CROWS': lambda: {'patternType': '?', 'direction': '<', 'reliability': '>'},
  'CDL3BLACKCROWS': lambda: {'patternType': '?', 'direction': '<', 'reliability': '>'},
  'CDL3INSIDE': lambda: {'patternType': '?', 'direction': '<', 'reliability': '>'},
  'CDL3LINESTRIKE': lambda: {'patternType': '?', 'direction': '<', 'reliability': '>'},
  'CDL3OUTSIDE': lambda: {'patternType': '?', 'direction': '<', 'reliability': '>'},
  'CDL3STARSINSOUTH': lambda: {'patternType': '?', 'direction': '<', 'reliability': '>'},
  'CDL3WHITESOLDIERS': lambda: {'patternType': '?', 'direction': '<', 'reliability': '>'},
  'CDLABANDONEDBABY': lambda: {'patternType': '?', 'direction': '<', 'reliability': '>'},
  'CDLADVANCEBLOCK': lambda: {'patternType': '?', 'direction': '<', 'reliability': '>'},
  'CDLBELTHOLD': lambda: {'patternType': '?', 'direction': '<', 'reliability': '>'},
  'CDLBREAKAWAY': lambda: {'patternType': '?', 'direction': '<', 'reliability': '>'},
  'CDLCLOSINGMARUBOZU': lambda: {'patternType': '?', 'direction': '<', 'reliability': '>'},
  'CDLCONCEALBABYSWALL': lambda: {'patternType': '?', 'direction': '<', 'reliability': '>'},
  'CDLCOUNTERATTACK': lambda: {'patternType': '?', 'direction': '<', 'reliability': '>'},
  'CDLDARKCLOUDCOVER': lambda: {'patternType': '?', 'direction': '<', 'reliability': '>'},
  'CDLDOJI': lambda: {'patternType': '?', 'direction': '<', 'reliability': '>'},
  'CDLDOJISTAR': lambda: {'patternType': 'reversal pattern', 'direction': '<', 'reliability': 'medium'}, # V
  'CDLDRAGONFLYDOJI': lambda: {'patternType': '?', 'direction': '<', 'reliability': '>'}, # not high
  'CDLENGULFING': lambda: {'patternType': '?', 'direction': '<', 'reliability': '>'}, # https://sourceforge.net/p/ta-lib/code/HEAD/tree/trunk/ta-lib/c/src/ta_func/ta_CDLENGULFING.c#l212 * outInteger is positive (1 to 100) when < or negative (-1 to -100) when bearish:
  'CDLEVENINGDOJISTAR': lambda: {'patternType': '?', 'direction': '<', 'reliability': '>'},
  'CDLEVENINGSTAR': lambda: {'patternType': '?', 'direction': '<', 'reliability': '>'},
  'CDLGAPSIDESIDEWHITE': lambda: {'patternType': '?', 'direction': '<', 'reliability': '>'},
  'CDLGRAVESTONEDOJI': lambda: {'patternType': '?', 'direction': '<', 'reliability': '>'},
  'CDLHAMMER': lambda: {'patternType': '?', 'direction': '<', 'reliability': '>'},
  'CDLHANGINGMAN': lambda: {'patternType': '?', 'direction': '<', 'reliability': '>'},
  'CDLHARAMI': lambda: {'patternType': '?', 'direction': '<', 'reliability': '>'},
  'CDLHARAMICROSS': lambda: {'patternType': '?', 'direction': '<', 'reliability': '>'},
  'CDLHIGHWAVE': lambda: {'patternType': '?', 'direction': '<', 'reliability': '>'},
  'CDLHIKKAKE': lambda: {'patternType': '?', 'direction': '<', 'reliability': '>'},
  'CDLHIKKAKEMOD': lambda: {'patternType': '?', 'direction': '<', 'reliability': '>'},
  'CDLHOMINGPIGEON': lambda: {'patternType': '?', 'direction': '<', 'reliability': '>'},
  'CDLIDENTICAL3CROWS': lambda: {'patternType': '?', 'direction': '<', 'reliability': '>'},
  'CDLINNECK': lambda: {'patternType': '?', 'direction': '<', 'reliability': '>'},
  'CDLINVERTEDHAMMER': lambda: {'patternType': '?', 'direction': '<', 'reliability': '>'},
  'CDLKICKING': lambda: {'patternType': '?', 'direction': '<', 'reliability': '>'},
  'CDLKICKINGBYLENGTH': lambda: {'patternType': '?', 'direction': '<', 'reliability': '>'},
  'CDLLADDERBOTTOM': lambda: {'patternType': '?', 'direction': '<', 'reliability': '>'},
  'CDLLONGLEGGEDDOJI': lambda: {'patternType': '?', 'direction': '<', 'reliability': '>'},
  'CDLLONGLINE': lambda: {'patternType': '?', 'direction': '<', 'reliability': '>'},
  'CDLMARUBOZU': lambda: {'patternType': '?', 'direction': '<', 'reliability': '>'},
  'CDLMATCHINGLOW': lambda: {'patternType': 'reversal pattern', 'direction': '<', 'reliability': 'medium'}, # V
  'CDLMATHOLD': lambda: {'patternType': '?', 'direction': '<', 'reliability': '>'},
  'CDLMORNINGDOJISTAR': lambda: {'patternType': '?', 'direction': '<', 'reliability': '>'},
  'CDLMORNINGSTAR': lambda: {'patternType': '?', 'direction': '<', 'reliability': '>'},
  'CDLONNECK': lambda: {'patternType': '?', 'direction': '<', 'reliability': '>'},
  'CDLPIERCING': lambda: {'patternType': '?', 'direction': '<', 'reliability': '>'},
  'CDLRICKSHAWMAN': lambda: {'patternType': '?', 'direction': '<', 'reliability': '>'},
  'CDLRISEFALL3METHODS': lambda: {'patternType': '?', 'direction': '<', 'reliability': '>'},
  'CDLSEPARATINGLINES': lambda: {'patternType': '?', 'direction': '<', 'reliability': '>'},
  'CDLSHOOTINGSTAR': lambda: {'patternType': '?', 'direction': '<', 'reliability': '>'},
  'CDLSHORTLINE': lambda: {'patternType': '?', 'direction': '<', 'reliability': '>'},
  'CDLSPINNINGTOP': lambda: {'patternType': '?', 'direction': '<', 'reliability': '>'},
  'CDLSTALLEDPATTERN': lambda: {'patternType': '?', 'direction': '<', 'reliability': '>'},
  'CDLSTICKSANDWICH': lambda: {'patternType': '?', 'direction': '<', 'reliability': '>'},
  'CDLTAKURI': lambda: {'patternType': '?', 'direction': '<', 'reliability': '>'},
  'CDLTASUKIGAP': lambda: {'patternType': '?', 'direction': '<', 'reliability': '>'},
  'CDLTHRUSTING': lambda: {'patternType': '?', 'direction': '<', 'reliability': '>'},
  'CDLTRISTAR': lambda: {'patternType': '?', 'direction': '<', 'reliability': '>'},
  'CDLUNIQUE3RIVER': lambda: {'patternType': '?', 'direction': '<', 'reliability': '>'},
  'CDLUPSIDEGAP2CROWS': lambda: {'patternType': '?', 'direction': '<', 'reliability': '>'},
  'CDLXSIDEGAP3METHODS': lambda: {'patternType': '?', 'direction': '<', 'reliability': '>'},
}

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