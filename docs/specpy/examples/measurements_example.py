"""
    Example of how to traverse the measurements, configurations, stacks hierarchy of Imspector with Python.
	Also runs a measurement.

    Requirements: Latest Python 2.X or 3.X, specpy (https://pypi.python.org/pypi/specpy/1.0.2)
    which itself requires NumPy >= 1.8.1, Imspector with "Run Server" checked and an open measurement.

    March, 2015, Jan Keller (jan.keller@mpibpc.mpg.de)

    See also: http://imspectordocs.readthedocs.io/en/latest/specpy/examples.html
"""

# Python 2/3 compatibility
from __future__ import absolute_import, division, print_function

import pprint
pp = pprint.PrettyPrinter(indent=2)

# import NumPy
import numpy as np

# import specpy
import specpy as sp

# get imspector object and print version
im = sp.Imspector()
print('Imspector {} on {}'.format(im.version(), im.host()))

# print existing device drivers
print('devices')
pp.pprint(im.device_drivers())

# print current imspector parameters
print('parameters')
pp.pprint(im.parameters())

# list all open measurements
print('names of open measurements')
pp.pprint(im.measurement_names())

# get currently active measurement
msr = im.active_measurement()
print('name of active measurement: {}'.format(msr.name()))
print('configurations in active measurement')
pp.pprint(msr.configuration_names())
print('number of stacks: {}'.format(msr.number_of_stacks()))
pp.pprint(msr.stack_names())

# get another measurement (the first one, should be at least one open)
measurement_name = im.measurement_names()[0]
msr = im.measurement(measurement_name)
print('name of chosen measurement: {}'.format(msr.name()))
print('configurations in chosen measurement')
pp.pprint(msr.configuration_names())
print('active configuration: {}'.format(msr.active_configuration().name()))
print('number of stacks: {}'.format(msr.number_of_stacks()))
pp.pprint(msr.stack_names())

# set active configuration (the first one, should contain at least one)
configuration_name = msr.configuration_names()[0]
configuration = msr.configuration(configuration_name)
msr.activate(configuration)
print('active configuration: {}'.format(msr.active_configuration().name()))

# create new stack (will be added to active measurement)
s = msr.create_stack(np.int32, [100, 100, 1, 1])
print('number of stacks: {}'.format(msr.number_of_stacks()))
pp.pprint(msr.stack_names())

# runs the measurement
print('active configuration {}'.format(msr.active_configuration().name()))
im.run(msr)
print('number of stacks: {}'.format(msr.number_of_stacks()))
pp.pprint(msr.stack_names())

# set a configuration and runs it
configuration = msr.configuration(configuration_name)
msr.activate(configuration)
print('active configuration {}'.format(msr.active_configuration().name()))
im.run(msr)
print('number of stacks: {}'.format(msr.number_of_stacks()))
pp.pprint(msr.stack_names())