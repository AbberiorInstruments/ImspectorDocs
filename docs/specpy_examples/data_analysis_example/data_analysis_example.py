"""
    Connects to Imspector, opens a recorded measurement, computes statistical measures on this data
    and prints them in a file.
    
    Requirements: Latest Python 2.X or 3.X, specpy (https://pypi.python.org/pypi/specpy/1.0.2)
    which itself requires NumPy >= 1.8.1, Imspector with "Run Server" checked and the file
    "data_analysis_example.msr".
        
    See also: https://im.mpibpc.mpg.de/documentation/specpy_examples.html        
"""

# Python 2/3 compatibility
from __future__ import absolute_import, division, print_function

# import numpy
import numpy as np

# import specpy
import specpy as sp

# connect to local Imspector and open an example file
im = sp.Imspector()
measurement = im.open("data_analysis_example.msr")

# set threshold
threshold = 410

# open output file
file = open('data_analysis_example_output.txt', 'w')

# for each stack in the measurement
for name in measurement.stack_names():
    # get the stack (as our stub object)
    stack = measurement.stack(name)
    # get the data array from the stack
    data = stack.data()
    # compute mean and std
    mean = data.mean()
    standard_deviation = data.std()
    # print mean and std to console and to file
    print('stack {} has mean {} and std {}'.format(name, mean, standard_deviation))
    print('stack {} has mean {} and std {}'.format(name, mean, standard_deviation), file=file)

    # apply mask (all values smaller threshold)
    masked_data = np.ma.masked_less(data, threshold)

    # compute mean and std on masked image
    mean = masked_data.mean()
    standard_deviation = masked_data.std()

    # print mean and std on masked image to console and to file
    print('masked stack {} with threshold {} has mean {} and std {}'.format(name, threshold, mean, standard_deviation))
    print('masked stack {} with threshold {} has mean {} and std {}'.format(name, threshold, mean, standard_deviation), file=file)

    # change pixels (you can see this in Imspector) below threshold to another value
    np.putmask(data, data < threshold, 4095)

file.close()
