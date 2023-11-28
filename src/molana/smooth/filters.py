# author: Roy Kid
# contact: lijichen365@126.com
# date: 2023-11-28
# version: 0.0.1

import numpy as np
import scipy

def savgol(x, window_length, polyorder, derive=0, delta=1.0, axis=-1, model='interp', cval=0.0):
    return scipy.signal.savgol_filter(x, window_length, polyorder, deriv=derive, delta=delta, axis=axis, mode=model, cval=cval)