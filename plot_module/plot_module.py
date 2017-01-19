
import mlpux
import json
import numpy as np
import random
"""
A fake module which will be used for unit testing the demo framework.

Here, I'll slowly accumulate a list of possible demo architectures to run through
the demo framework.
"""

@mlpux.Interactive()
@mlpux.Plot2D(title="A Plot Title")
@mlpux.Slider(arg='x_min', min_val=0, max_val=50, ndiv=30)
@mlpux.Slider(arg='x_max', min_val=100, max_val=250, ndiv=30)
@mlpux.Demo()
def make_2D_data(x_min, x_max, num, ret_type='tuple', func=np.sin):
    """
    Make data set conisisting of x and y values for a 2D plot.

    param1: x_min: minimum of domain
    param2: x_max: maximium of domain
    param3: number of points to generate
    param5: default: callback representing the function that maps x-values to y values.
    param4: return type: 'tuple', 'dict', or 'numpy_tensor' (i.e. x-y values zipped together)
    """
    name = make_2D_data.__name__
    x = np.linspace(start=x_min, stop=x_max, num=num)
    y = func(x)

    if ret_type == 'tuple':
        return list(x),list(y)
    if ret_type == 'dict':
        return {'x':list(x), 'y':list(y) }
    else:
        raise ValueError("Return of {} must be an iterable representing 2D data set. Options are 'tuple' or 'dict'".format(name))

