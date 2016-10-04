"""
    Connects to Imspector, displays the parameters and doubles the exposure time of the sample camera
    if a camera is existing as device.

    Requirements: Latest Python 2.X or 3.X, specpy (https://pypi.python.org/pypi/specpy/1.0.2)
    which itself requires NumPy >= 1.8.1, Imspector with "Run Server" checked and an open measurement

    See also: https://imspector.mpibpc.mpg.de/documentation/specpy_examples.html
"""

# Python 2/3 compatibility
from __future__ import absolute_import, division, print_function

# import specpy
import specpy as sp

# connect to local Imspector
im = sp.Imspector()

# print Imspector host and version
print('Connected to Imspector {} on {}'.format(im.version(), im.host()))

# get active measurement and print nicely
msr = im.active_measurement()
from pprint import pprint
print('Parameters of measurement {}'.format(msr.name()))
pprint(msr.parameters())

# read and write a parameter
if 'SimCam' in msr.parameters():
    time = msr.parameters('SimCam/ExposureTime')
    msr.set_parameters('SimCam/ExposureTime', 2 * time)

# now have a look at Imspector, the parameter should have changed in the measurement properties of this measurement