def getPatternInformation(patternName):
  switcher = {    
    'CDL2CROWS': lambda: {'direction': 'Bullish', 'reliability': 'medium'},
    'CDL3BLACKCROWS': lambda: {'direction': 'Bullish', 'reliability': 'medium'},
    'CDL3INSIDE': lambda: {'direction': 'Bullish', 'reliability': 'medium'},
    'CDL3LINESTRIKE': lambda: {'direction': 'Bullish', 'reliability': 'medium'},
    'CDL3OUTSIDE': lambda: {'direction': 'Bullish', 'reliability': 'medium'},
    'CDL3STARSINSOUTH': lambda: {'direction': 'Bullish', 'reliability': 'medium'},
    'CDL3WHITESOLDIERS': lambda: {'direction': 'Bullish', 'reliability': 'medium'},
    'CDLABANDONEDBABY': lambda: {'direction': 'Bullish', 'reliability': 'medium'},
    'CDLADVANCEBLOCK': lambda: {'direction': 'Bullish', 'reliability': 'medium'},
    'CDLBELTHOLD': lambda: {'direction': 'Bullish', 'reliability': 'medium'},
    'CDLBREAKAWAY': lambda: {'direction': 'Bullish', 'reliability': 'medium'},
    'CDLCLOSINGMARUBOZU': lambda: {'direction': 'Bullish', 'reliability': 'medium'},
    'CDLCONCEALBABYSWALL': lambda: {'direction': 'Bullish', 'reliability': 'medium'},
    'CDLCOUNTERATTACK': lambda: {'direction': 'Bullish', 'reliability': 'medium'},
    'CDLDARKCLOUDCOVER': lambda: {'direction': 'Bullish', 'reliability': 'medium'},
    'CDLDOJI': lambda: {'direction': 'Bullish', 'reliability': 'medium'},
    'CDLDOJISTAR': lambda: {'direction': 'Bullish', 'reliability': 'medium'},
    'CDLDRAGONFLYDOJI': lambda: {'direction': 'Bullish', 'reliability': 'medium'},
    'CDLENGULFING': lambda: {'direction': 'Bullish', 'reliability': 'medium'},
    'CDLEVENINGDOJISTAR': lambda: {'direction': 'Bullish', 'reliability': 'medium'},
    'CDLEVENINGSTAR': lambda: {'direction': 'Bullish', 'reliability': 'medium'},
    'CDLGAPSIDESIDEWHITE': lambda: {'direction': 'Bullish', 'reliability': 'medium'},
    'CDLGRAVESTONEDOJI': lambda: {'direction': 'Bullish', 'reliability': 'medium'},
    'CDLHAMMER': lambda: {'direction': 'Bullish', 'reliability': 'medium'},
    'CDLHANGINGMAN': lambda: {'direction': 'Bullish', 'reliability': 'medium'},
    'CDLHARAMI': lambda: {'direction': 'Bullish', 'reliability': 'medium'},
    'CDLHARAMICROSS': lambda: {'direction': 'Bullish', 'reliability': 'medium'},
    'CDLHIGHWAVE': lambda: {'direction': 'Bullish', 'reliability': 'medium'},
    'CDLHIKKAKE': lambda: {'direction': 'Bullish', 'reliability': 'medium'},
    'CDLHIKKAKEMOD': lambda: {'direction': 'Bullish', 'reliability': 'medium'},
    'CDLHOMINGPIGEON': lambda: {'direction': 'Bullish', 'reliability': 'medium'},
    'CDLIDENTICAL3CROWS': lambda: {'direction': 'Bullish', 'reliability': 'medium'},
    'CDLINNECK': lambda: {'direction': 'Bullish', 'reliability': 'medium'},
    'CDLINVERTEDHAMMER': lambda: {'direction': 'Bullish', 'reliability': 'medium'},
    'CDLKICKING': lambda: {'direction': 'Bullish', 'reliability': 'medium'},
    'CDLKICKINGBYLENGTH': lambda: {'direction': 'Bullish', 'reliability': 'medium'},
    'CDLLADDERBOTTOM': lambda: {'direction': 'Bullish', 'reliability': 'medium'},
    'CDLLONGLEGGEDDOJI': lambda: {'direction': 'Bullish', 'reliability': 'medium'},
    'CDLLONGLINE': lambda: {'direction': 'Bullish', 'reliability': 'medium'},
    'CDLMARUBOZU': lambda: {'direction': 'Bullish', 'reliability': 'medium'},
    'CDLMATCHINGLOW': lambda: {'direction': 'Bullish', 'reliability': 'medium'},
    'CDLMATHOLD': lambda: {'direction': 'Bullish', 'reliability': 'medium'},
    'CDLMORNINGDOJISTAR': lambda: {'direction': 'Bullish', 'reliability': 'medium'},
    'CDLMORNINGSTAR': lambda: {'direction': 'Bullish', 'reliability': 'medium'},
    'CDLONNECK': lambda: {'direction': 'Bullish', 'reliability': 'medium'},
    'CDLPIERCING': lambda: {'direction': 'Bullish', 'reliability': 'medium'},
    'CDLRICKSHAWMAN': lambda: {'direction': 'Bullish', 'reliability': 'medium'},
    'CDLRISEFALL3METHODS': lambda: {'direction': 'Bullish', 'reliability': 'medium'},
    'CDLSEPARATINGLINES': lambda: {'direction': 'Bullish', 'reliability': 'medium'},
    'CDLSHOOTINGSTAR': lambda: {'direction': 'Bullish', 'reliability': 'medium'},
    'CDLSHORTLINE': lambda: {'direction': 'Bullish', 'reliability': 'medium'},
    'CDLSPINNINGTOP': lambda: {'direction': 'Bullish', 'reliability': 'medium'},
    'CDLSTALLEDPATTERN': lambda: {'direction': 'Bullish', 'reliability': 'medium'},
    'CDLSTICKSANDWICH': lambda: {'direction': 'Bullish', 'reliability': 'medium'},
    'CDLTAKURI': lambda: {'direction': 'Bullish', 'reliability': 'medium'},
    'CDLTASUKIGAP': lambda: {'direction': 'Bullish', 'reliability': 'medium'},
    'CDLTHRUSTING': lambda: {'direction': 'Bullish', 'reliability': 'medium'},
    'CDLTRISTAR': lambda: {'direction': 'Bullish', 'reliability': 'medium'},
    'CDLUNIQUE3RIVER': lambda: {'direction': 'Bullish', 'reliability': 'medium'},
    'CDLUPSIDEGAP2CROWS': lambda: {'direction': 'Bullish', 'reliability': 'medium'},
    'CDLXSIDEGAP3METHODS': lambda: {'direction': 'Bullish', 'reliability': 'medium'},
  }
  return switcher.get(patternName, lambda: {'direction': 'Invalid pattern', 'reliability': 'Invalid pattern'})()
























































