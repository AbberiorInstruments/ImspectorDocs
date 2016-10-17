=====================
Measurement Templates
=====================

In Imspector a template-driven workflow is implemented.

Measurement templates are ready-to-use parameter sets that enable a quick start into the use of Imspector and the
microscope without the need for the user to be familiar with each and every detail of the microscope and the software.
They contain the acquisition parameters (as field of view, pixel size, scan speed, scan direction, dimensionality,
activated lasers, activated detectors....) that are required for a type of measurement. As in an Imspector measurement,
multiple windows may be included.

To open a Template select 'File' → 'New' → 'File from Template'...

During installation of the system a set of standard measurements schemes is pre-defined (Fig. 1).

.. figure:: /images/hardware/load_template_dialog.png
   :align: center

   'Load Template' dialog.

Based on these templates users can start with several basic measurement. Later, the given templates can be either adapted
for the users measurement of interest or new templates can be created by the user.
In contrast to easyCommander driven work-flows, measurement templates are not restricted to simplified measurement settings,
but may contain most parameters that are available in Imspector at a given the setup.

Use of Existing Measurements as Templates
-----------------------------------------

In Imspector existing measurements can be used as templates, because they contain required instrument parameters/ meta-data
for starting a new measurement. After opening a saved measurement, all experiments can be done in the exact same way by
restarting the saved measurement with 'REC'.

Note: When several measurements are imported into Imspector, the scan settings of the active measurement window will be applied, when the 'REC' button is pressed. This allows a rapid change between different measurement modes.
