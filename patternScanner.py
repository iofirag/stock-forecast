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

# convert data to columns  
sample_data = numpy.column_stack(sample_data)

# extract the columns we need, making sure to make them 64-bit floats  
o = sample_data[1].astype(float)  
h = sample_data[2].astype(float)  
l = sample_data[3].astype(float)  
c = sample_data[4].astype(float)

funcs = get_candle_funcs()

results = {}  
for f in funcs:  
    res = funcs[f](o, h, l, c)
    if res[-1] > 0:
        results[f] = res

print('')
print('results:',results)