============
Live Dialogs
============

In Imspector most imaging settings/parameters may be adjusted in live dialogs including activity of devices as lasers and
detectors, settings such as laser power or pinhole size and guiding activity along the measurement process such as time
lapse measurements.
Single live dialogs can simply be hidden by closing the corresponding live dialogs window! Every live dialog (in addition)
can be re-opened by clicking on :menuselection:`Tab --> Windows --> Live Dialogs` (:ref:`fig_livedialogs`).
If none of the live dialogs should be visible, all of them can be hidden using the :kbd:`TAB` button of the keyboard.

.. _fig_livedialogs:
.. figure:: /images/hardware/live_dialogs.png
   :width: 10 cm
   :align: center

   'Live Dialogs' window.

Experimental Control Live Dialog
--------------------------------

In the 'Experiment Control' live dialog (:ref:`fig_livedialog_control`) the basic scan settings are done:

- Type of scan (xy, yx, yz,xz, xt, xyt, xyz ...)
- Scan 'Range' in X, Y, Z, T
- Local and global offsets of the scanner i.e. the displacement from the central axis
  A local offset (given in the upper half of the panel) applies only for a single measurement.
  A global offset applies to all further measurements in addition to the local offsets.
- Pixel size ('Pix. Size') and the number of pixels ('# Pixel')
- Line accumulation settings ('Line Accu')
- Time steps ('T')
  Here only consecutive time steps can be selected. For using time steps with breaks in between, the 'TimeLapse'
  live dialog has to be used.
- The 'Orientation' parameters allow to change the orientation of the scan field: scan field rotation ('Rot'), tilting of
  the scan field ('Tilt') or rolling of the scan field ('Roll') may be applied.
- 'Dwell Time'

.. note::
   The Line Frequency ('Line Freq') is given at the bottom right of the dialog. It may not be changed, but is
   calculated from the scan parameters above.

**Check boxes**

- 'Lock Aspect': If selected, the aspect ratio of the image ist locked (i.e. ranges).
- 'Lock pixel Size': if selected, only the size of the pixels and the range may be changed. The # of pixels is adjusted
  automatically.
  Note that the range may be rounded, when the change is incompatible to size and range.
- 'Square pixels': When selected, the pixel sized in x and y are kept being equal. Only one of them may be changed. The
  other one is changed together with it.

.. _fig_livedialog_control:
.. figure:: /images/hardware/live_dialog_experimental_control.png
   :width: 6 cm
   :align: center

   'Experiment Control' live dialog.

Hardware Acquisition Timing Live Dialog
---------------------------------------

The measurement timing parameters as 'Elapsed Time' for the complete Scan, for the line, frame etc. are given in the
'Hardware Acquisition Timing' live dialog (:ref:`fig_livedialog_acq_timing`) .

.. _fig_livedialog_acq_timing:
.. figure:: /images/hardware/live_dialog_hardware_acquisition_timing.png
   :width: 6 cm
   :align: center

   'Hardware Acquisition Timing' live dialog.

Lasers and Channels Live Dialog
-------------------------------

In the 'Lasers and Channels' live dialog (:ref:`fig_livedialog_lasers`) is one of the most important live dialogs. Here important settings on
the channels, 'Detectors' and lasers are shown and can be modified. Furthermore the imaging modes 'Pixel Steps',
'Line Steps', 'Pulse Steps' and 'Pulse Gates' can be activated.

**Detectors**

Detection channels can be activated in the check box on the left side ('Ch1', 'Ch2','Ch3','Ch4').
In the drop-down menus, the different detectors (APDs/PMTs) can be selected and assigned to the (logical) detection channels.
If PMT detectors are selected, the gain of the PMT may be adjusted.
On the right side, further the RESCue mode can be activated.
Note that up to four logical (detection) channels can be used.

**Lasers**

In the middle of the live dialog, the excitation, STED and RESOLFT lasers ('L1', 'L2', 'L3', 'L4', 'L5', 'L6', 'L7', 'L8')
can be activated. Further the power can be adjusted using the %-values on the right. For alignment purposes, the lasers
can be continuously activated using the check box on the right. (This is only possible if the user is logged in as 'expert'.)
Note that the %-values are calibrated to show a linear response.

**Scan Options & Gating**

On the bottom of this live dialog, following scan options can be selected:
'Pulse Steps', 'Pixel Steps' , 'Line Steps'.
Further the fluorescence time-gating for the different detection channels can be activated by selecting 'Pulse Gates'.

.. _fig_livedialog_lasers:
.. figure:: /images/hardware/live_dialog_lasers_channels.png
   :width: 6 cm
   :align: center

   'Lasers and Channels' live dialog.

Microscope Control Live Dialogs
-------------------------------

Imspector is able to communicate with the microscope stands of several vendors and all of its motorized components.
It is able to drive most functions of the microscopy body (:ref:`fig_livedialog_microscope`).
Those functions include:

- switching of the observation mode
- changing the light path (Light Path)
- setting and reading out the stage position (x, y)
- changing objective lenses
- setting and reading out the z-position of the objective lens
- switching on/off the auto-focusing device (optional upgrade)
- brightness of the tungsten lamp in the transillumination path (TransIllum)
- open/close Shutter

.. _fig_livedialog_microscope:
.. figure:: /images/hardware/live_dialog_olympusIX.png
   :width: 6 cm
   :align: center

   'OlympusIX' live dialog.

Time Lapse Live Dialog
----------------------

In the 'TimeLapse' live dialog (:ref:`fig_livedialog_timelapse`), time lapse measurements with breaks in between the individual steps can be devised.
More advanced settings with unequal steps can be further devised using the 'Sequence Scheduler'.

.. note::
   The tool-tips on the usage of the sequence scheduler which can be opened using the question mark at the
   right side of the live dialog.

.. _fig_livedialog_timelapse:
.. figure:: /images/hardware/live_dialog_time_lapse.png
   :width: 6 cm
   :align: center

   'Time Lapse' live dialog.