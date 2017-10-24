-------------------------
Python Interface Examples
-------------------------

There are a couple of examples.

.. _specpy_example_hello_imspector:

Hello Imspector Example
=======================

Connects to Imspector, displays the parameters and doubles the exposure time of the sample camera
if a camera is existing as device.

`hello_imspector_example.py <https://raw.githubusercontent.com/AbberiorInstruments/ImspectorDocs/master/docs/specpy/examples/hello_imspector_example.py>`__

.. include:: /specpy/examples/hello_imspector_example.py
	:code: python

.. _specpy_example_data_analysis:

Data Analysis Example
=====================

Connects to Imspector, opens a recorded measurement, computes statistical measures on this data
and prints them in a file.

`data_analysis_example.py <https://raw.githubusercontent.com/AbberiorInstruments/ImspectorDocs/master/docs/specpy/examples/data_analysis_example.py>`__ -
`data_analysis_example.msr <https://github.com/AbberiorInstruments/ImspectorDocs/raw/master/docs/specpy/examples/data_analysis_example.msr>`__

.. include:: /specpy/examples/data_analysis_example.py
	:code: python

.. _specpy_example_measurement:

Measurement Example
===================

Example of how to traverse the measurements, configurations, stacks hierarchy of Imspector with Python.
Also runs a measurement.

`measurements_example.py <https://raw.githubusercontent.com/AbberiorInstruments/ImspectorDocs/master/docs/specpy/examples/measurements_example.py>`__

.. include:: /specpy/examples/measurements_example.py
	:code: python