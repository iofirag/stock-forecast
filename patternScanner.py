import talib
import numpy

def get_candle_funcs():  
    funcs = {}
    for name in talib.get_functions():  
        if name.startswith('CDL'):  
            funcs[name] = getattr(talib, name)  
    return funcs

# sample_data = [  
#     ['1/22/14', 10, 18,  17, 20],
#     ['1/22/14', 10, 18,  17, 20],
#     ['1/22/14', 10, 18,  17, 20],
#     ['1/22/14', 10, 18,  17, 20],
#     ['1/22/14', 10, 18,  17, 20],
#     ['1/22/14', 10, 18,  17, 20],
#     ['1/22/14', 10, 18,  17, 20],
#     ['1/22/14', 10, 18,  17, 20],
#     ['1/22/14', 10, 18,  17, 20],
#     ['1/22/14', 10, 18,  17, 20],
#     ['2/03/14', 44, 45, 43, 44.09],

#     ['1/22/14', 10, 18,  17, 20],
#     ['1/22/14', 10, 18,  17, 20],
#     ['1/22/14', 10, 18,  17, 20],
#     ['1/22/14', 10, 18,  17, 20],
#     ['1/22/14', 10, 18,  17, 20],
#     ['1/22/14', 10, 18,  17, 20],
#     ['1/22/14', 10, 18,  17, 20],
#     ['1/22/14', 10, 18,  17, 20],
#     ['1/22/14', 10, 18,  17, 20],
#     ['1/22/14', 10, 18,  17, 20],
#     ['2/03/14', 44, 45, 43, 44.09], # today
# ]

# indentifyCandles(sample_data)

# def indentifyCandles(historical_data):
#         # convert data to columns  
#         numpyData = numpy.column_stack(historical_data)

#         # extract the columns we need, making sure to make them 64-bit floats  
#         # print(numpyData)
#         o = numpyData[1].astype(float)  
#         h = numpyData[2].astype(float)  
#         l = numpyData[3].astype(float)  
#         c = numpyData[4].astype(float)

#         function_list = get_candle_funcs()

#         results = {}  
#         for f in function_list:  
#             res = function_list[f](o, h, l, c)
#             if res[-1] > 0:
#                 results[f] = res

#         # print('')
#         # print('results:',results)