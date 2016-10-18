============
Introduction
============

Imspector is a robust software system for experimental control and quantitative data analysis in microscopy and
spectroscopy. Integration of data processing and acquisition allows real-time analysis and visualization of
experimental results.

Features
--------

.. figure:: /images/intro/customization.jpg
   :width: 8 cm
   :align: center

   Customization of toolbars, menus and shortcuts.

.. figure:: /images/intro/workspace.jpg
   :width: 8 cm
   :align: center

   The workspace allows you to keep track of all your measurements.

.. figure:: /images/intro/new_device.jpg
   :width: 8 cm
   :align: center

   Add new devices derived from standard or custom drivers.

Imspector offers a variety of functions for speed-optimized visualization of up to 4-dimensional data as graphs and
pictures, an intuitive user interface and access to analysis methods. Data can be graphically cropped, moved, copied
and combined in overlays. In addition to ordinary cuts, zooming, multi-channel display and user-defined color tables,
many tools are provided that are especially useful in quantitative microscopy. There are tools for the calculation of
point-spread functions and simple linear de-convolution, frequency filtering etc. A tool for off-line nonlinear
de-convolution is also included.

.. figure:: /images/intro/parser.jpg
   :width: 8 cm
   :align: center

   Use the built-in parser to analyse and process your data.

.. figure:: /images/intro/analysis.jpg
   :width: 8 cm
   :align: center

   Nonlinear fitting of single data curves or e.g. along the time axis of a TCSPC stack in each spatial point.

A built-in function parser allows for user-defined filters, transformations and other numerical operations on the
data and as part of the 'FitPlugin' nonlinear parameter fitting with user-defined functions and a choice of several
optimized algorithms.

Imspector imports and exports many commonly used data formats and communicates with other applications as e.g.
Origin, Photoshop, Freehand and Excel through cut- and paste operations.

Hardware drivers exist for analog output devices, multi-channel scales, time correlated single photon counting
(TCSPC), various CCD cameras (e.g. Apogee, Hamamatsu, PCO), laser power controllers, positioning stages (PIFOCs etc.).

Adding the ability to control new hardware components is straight-forward and achieved through a Plugin structure. Such
hardware drivers can provide dialogs for hard- and software-specific settings and parameter adjustment during
measurements. Data readout can be synchronous or asynchronous, the program handles the measurement flow,
synchronization of different devices and the coordination of data readout, analysis and visualization during the
measurement.

.. figure:: /images/intro/docsettings.jpg
   :width: 8 cm
   :align: center

   An intuitive GUI allows you to adjust your measurement parameters.

.. figure:: /images/intro/setasroi.jpg
   :align: center

   All measurement parameters are remembered. So you can derive measurements from previous 
   ones, image regions of interest etc.

The program administers the settings defined by the Hardware drivers and allows the creation of template
measurements including embedded analysis and visualization. Measurements can therefore be repeated at any time with
identical settings by pressing a single button. Experimental data is always saved together with all relevant settings
for later reference.

All data dependencies are remembered by the program so if data changes during a measurement or manual processing all
necessary steps to update dependent data are repeated automatically. Imspector will even remember dependencies on
data saved on disk and can 'watch' these files and re-load them if necessary. It can therefore serve as a graphical
front-end for your command-line numerical analysis tools. All such dependencies, as well as settings and window
positions are conserved when saving and re-loading documents.

Current state of Documentation
------------------------------

Many features of Imspector were inspired by its users in the |NanoBio|_ at the |MPI|.

Not all of them found their way into this documentation as of now. Also, Imspector is under constant development, so
features might be added or functionality might be replaced by superior implementations. Thus some of the information
presented here might be outdated. Anybody is encouraged to explore the context-menus - a lot of the functionality is
intuitive enough to figure it out by trial and error.

Imspector has been originally developed in the |NanoBio|_ at the |MPI|_ in Göttingen, Germany.

Imspector was always and is currently lacking appropriate documentation. All users of Imspector are welcome to
contribute. The source format of this manual is `restructured text`_ and we are using Sphinx_ to create the manual
from it. You may send manual pages or sections in any format and they will be incorporated.

Citing Imspector
----------------

If you are using Imspector for your data acquisition or analysis and would like to cite the program or its documentation please use the following reference:
	
	| Schönle A., 2006. *Imspector Image Acquisition & Analysis Software*, v0.1
	| http://www.imspector.de

.. _Sphinx: http://www.sphinx-doc.org/en/stable/index.html

.. _`restructured text`: https://en.wikipedia.org/wiki/ReStructuredText

.. |NanoBio| replace:: department of NanoBiophotonics

.. _NanoBio: http://www.mpibpc.mpg.de/hell

.. |MPI| replace:: Max Planck Institute for biophysical Chemistry

.. _MPI: http://www.mpibpc.mpg.de/
