-----------------------------------
Imspector Python Interface Examples
-----------------------------------

`Save <specpy_examples.zip>`_ examples.

.. _specpy_example_hello_imspector:

Hello Imspector Example
=======================

Connects to Imspector, displays the parameters and doubles the exposure time of the sample camera
if a camera is existing as device.

.. include:: specpy_examples\hello_imspector_example\hello_imspector_example.py 
	:code: python

.. _specpy_example_data_analysis:

Data Analysis Example
=====================

Connects to Imspector, opens a recorded measurement, computes statistical measures on this data
and prints them in a file.

.. include:: specpy_examples\data_analysis_example\data_analysis_example.py 
	:code: python

.. _specpy_example_measurement:

Measurement Example
===================

Example of how to traverse the measurements, configurations, stacks hierarchy of Imspector with Python.
Also runs a measurement.

.. include:: specpy_examples\measurements_example\measurements_example.py 
	:code: python