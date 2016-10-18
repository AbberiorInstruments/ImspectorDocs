.. _Quickstart:

=================
Quickstart
=================

Imspector contains a few data analysis plugins and drivers for

- VidCap (for most webcams) 
- SimCam (a simulated camera for testing) 
- SyncDriver (provides dummy axes, allows synchronization via serial port)
- ComDriver (a generic driver for com/gpib devices with a simple protocol)
- Timer (for time-lapse type measurements)
- Becker&Hickl SPCM cards
- National instruments DAQ cards (through the NiDAQmx drivers) which control scanners, shutters and read out detectors
- Scanners from PI
- Various CCD cameras
 
.. warning::
   Drivers are simply dll's that Interface Imspector to the drivers you install with your hardware. They have to
   be compatible with both, the version of Imspector used and the version of the hardware drivers and support dll's
   installed on your system. Always download all necessary drivers together with a new version of Imspector. And
   make sure you have updated your hardware drivers.

Installation
-------------

For simply running Imspector (e.g. for data analysis) all you have to do is to extract the zip Archive into a
directory on your computer. Imspector will start and ask you for configuration directory. If this is the first time
you use Imspector, create one and select it. Otherwise point Imspector to your
existing directory.

.. note::
   Depending on your OS configuration you may have to install some additional libraries.
   Please see the `program start chapter in the FAQ <https://imspector.mpibpc.mpg.de/documentation/faq.html#errors-during-startup>`_ if you encounter errors during startup.

The configuration directory can be chosen independently for each user on each computer Imspector is run.
The directory itself can contain computer-specific configurations and also contains custom color maps,
fit functions, formulas created by the user. Therefore it is reasonable to use one directory per user
which is accessible from (or synchronized between) computers. You can change its location at any time
by copying/moving it and directing Imspector to the new location through
:menuselection:`&Edit --> &Preferences --> &Configuration Directory`.

There are other useful options in this menu, too. 
To avoid an error message upon startup, explicitly disable logging for now.

.. warning:: 
   You should regularly back up your configuration directory as settings, custom colormaps etc.
   can take some effort to re-create if you loose them. Also a regular backup allows you to reconstruct
   a working configuration if, for some reason your hardware does not behave as expected any
   more and you are unsure what you changed.

  
Adding devices
---------------

Go to :menuselection:`&Hardware --> &Add/Remove Devices` to add devices and then
click on the add button of the list box. You get a dialog with a combo 
list. Choose the device type. you will be asked a name. 
Choose one that is recognized by you and other potential users and keep in 
mind you may want to add more than one 'Camera' or 'Scanner'. 
 
.. note:: 
   Imspector can be extended by custom drivers compiled against the SDK.
   This requires knowledge of C++, the MFC and an installation of the 
   Visual Studio 2008 (currently) 

Adjust the hardware settings
----------------------------

Hardware settings are set in :menuselection:`&Hardware --> &Configure`. Usually you
will have to enter an identifier for the device. After adjusting the settings
press initialize to see whether the device was found and can be 
configured using your chosen settings. 

.. note:: 
   The device id for the NI card is a string, e.g. "Dev1" and can be found in the
   measurement & automation explorer. For NIDAQ cards you should restart Imspector
   right after initializing it for the first time and saving the hardware settings
   because the the number of available channels (and thus the configuration of 
   the settings dialogs) depends on the device model.  
   The µm -> Volts mapping is done in the Hardware settings of the NiCard
   after the restart (extra page with a channel selector and the possibility
   to set min and max Volts and the corresponding area your scanner will do).
 
Configuring a measurement
-------------------------

Open a document and go to :menuselection:`&Measurement --> Edit Settings`. This
lets you configure parameters that define your measurement. You can have many measurements
(i.e. documents) open at the same time and start them in turn to switch between different
settings. 

Most property pages are specific to the devices you configured in the hardware settings,
only the first page configures the measurement itself, i.e. selects which axes will be 
scanned and whether this is controlled automatically by trigger signals or through
Imspector. 

'Sync first axis' in the first page means that the first axis is controlled 
by hardware. The computer assumes that a pixel sync is shared by the 
devices (but has no way of checking it).
The devices have to be configures such that exactly one will be responsible
for creating the sync pulses (and will tell the framework that it does)
[e.g. when you enable 'Create sync pulses' in the NiDAQ card]

Exactly one device is responsible for 'waiting' until the axis sync has
finished during each measurement stack. Currently this is always the same
device that also creates the sync pulses.

All other devices have to acknowledge that they can deal with the synced
axis and must be configured to listen to the sync pulses (and tell the 
framework about it).

Measuring with just one NiDAQmx card
------------------------------------

Choose an appropriate 'sync out' for the NI card and 'disabled'
for sync in and set the dwell time in the 'DACs' configuration 
page.  Also set the 'Create Sync pulses' option in the DACs configuration

Select all other settings to your liking. (e.g. whether you want to 
measure histograms or not in the SPCM, AI channels in the NI card, have
one or two counter inputs etc. Please roam the config dialogs and tell
me what does and what doesn't make sense to you).

Select at least one analog input or a CNTR input if only using the NiDAQ 
card. When starting the measurement, a stack should then pop up.
 
If you need to configure the TTL outputs of the NiDAQ card, please check back
with us.


Analyzing data
---------------

All analysis functions are accessible through context menus. Right click 
on a stack, graph, axis, color map for those. For most of the frequently
used functions there are toolbar buttons.
 
Please write an email with as much detail of what you intended to do and what
you already tried if there is trouble.
 
 
