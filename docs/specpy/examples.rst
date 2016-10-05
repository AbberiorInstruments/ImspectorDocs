-----------------------------------
Imspector Python Interface Examples
-----------------------------------

.. _specpy_example_hello_imspector:

Hello Imspector Example
=======================

Connects to Imspector, displays the parameters and doubles the exposure time of the sample camera
if a camera is existing as device.

.. include:: examples\hello_imspector_example.py
	:code: python

.. _specpy_example_data_analysis:

Data Analysis Example
=====================

Connects to Imspector, opens a recorded measurement, computes statistical measures on this data
and prints them in a file.

.. include:: examples\data_analysis_example.py
	:code: python

.. _specpy_example_measurement:

Measurement Example
===================

Example of how to traverse the measurements, configurations, stacks hierarchy of Imspector with Python.
Also runs a measurement.

.. include:: examples\measurements_example.py
	:code: python