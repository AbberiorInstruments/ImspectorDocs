=============================
Installing Imspector
=============================

If this is your first time setting up Imspector please refer to the section :ref:`Quickstart` for installation instructions.
The basics of setting up the configuration directory are covered in the :ref:`ConfigDir` chapter of the :ref:`ShortTutorial`.

This chapter contains some more advanced aspects of setting up your measurement environment in Imspector and how to
set up and test your measurement-independent hardware.

Setting up the MPD panel
------------------------

The MPD panel is a custom made USB device that allows you to control the origin of scan axes. Support for
controlling other parameters is pending.

.. image:: /images/installation/mpd_panel.png
   :width: 12 cm
   :align: center

Currently the MPD panel is not available to parties outside the MPI. If you are interested in using it, please
contact the support team and let us know. If there is enough interest we may try to find a solution to this problem.

Install the drivers
.......................

Download the `modified FTDI drivers <http://imspector.mpibpc.mpg.de/extra/drivers/FTDI_CDM_Drivers_2.08.02.zip>`_ from the Imspector website.

.. note::

   As a side remark these are just the standard drivers found at FTDI `here <http://www.ftdichip.com/FTDrivers
   .htm>`_ with modified INF files to fit the IDs of our MPD panel. So in case the above version is incompatible with
   another FTDI device you can create a package based on another version of the FTDI drivers by modifying the INF files
   analogously.

Unpack the drivers to your local hard drive, connect the panel. When asked you should choose to manually point
windows to the location of the drivers. Depending on the windows version this will look something like this:

.. image:: /images/installation/mpd_panel_installation_browse.png
   :width: 10 cm
   :align: center

where the path is the location of the unpacked driver files. You may have to do this twice, once for a 'USB to Serial
converter' and once for a 'USB Serial Port'. You may be warned that the driver is a security risk:

.. image:: /images/installation/mpd_panel_installation_driver_warning.png
   :width: 10 cm
   :align: center

In case installation just fails without asking you to provide drivers, go to the device manager, find the new device not
running properly, right click and select6 'Update Driver'. Then continue as above. Again you may have to do this
twice. Eventually you should be successful:

.. image:: /images/installation/mpd_panel_installation_success.png
   :width: 10 cm
   :align: center

Run MpdCtrl.exe 
...............

Currently the MPD panel is controlled by a separate application, MpdCtrl.exe which manages access to the panel(s)
for different programs (we internally have some other applications that can share the panel with Imspector). You can
start MpdCtrl.exe directly from the installation directory of Imspector or through the tools menu:

.. image:: /images/installation/tools_menu.png
   :width: 10 cm
   :align: center

If the entry is greyed out this is either a glitch in Imspector (try to start it directly) or it is missing from
your installation. In this case make sure you did not accidentally delete it and then contact support.

When MpcCtrl starts it creates a tray icon which looks either like this:

.. image:: /images/installation/mpd_ctrl_not_connected.png
   :width: 10 cm
   :align: center

if either the panel is not connected or the driver is not correctly installed or like this:

.. image:: /images/installation/mpd_ctrl.png
   :width: 10 cm
   :align: center

if everything is just fine. You can start the app which does nothing except allowing you to rename a panel (if you
use more than one this is an important feature) and to show you which dials are in use by which app. Through the tray
icon you can also tell MpdCtrl.exe to start up automatically when you log on.


.. image:: /images/installation/mpd_ctrl.png
   :width: 10 cm
   :align: center

.. warning::
   It is important that the MPDCtrl.exe running is the same version as the Imspector executable accessing it.
   This is due to bad software design but will not be changes soon. If there is any trouble with the MPD panel,
   exit MPDCtrl.exe through its tray icon and restart it from the correct directory.

Configure the panel 
.......................

You configure the panel from the Imspector main menu. Go to :menuselection:`&Edit -> &Preferences -> Configure MPD Panel`.
You will see the following dialog provided that MpcCtrl.exe is running and has recognized a panel.

.. image:: /images/installation/mpd_config.png
   :width: 10 cm
   :align: center

You can load previous configurations by choosing them in the 'Select configuration name' combo box. You can save the current
configuration by typing a (new) name in the combo box (or choosing an old one to overwrite) and pressing 'Save'.
Delete configurations by selecting them and pressing 'Delete'. To modify configurations you edit the dial entries for
all connected panels. The values to configure are:

*Click Limit*
   The panel generates a clicking sound when the value is changed (on every step). If the time between value changes
   goes below the entered value in ms the clicking is suppressed. (i.e. the higher the value, the earlier this happens
   when rotating a dial fast). This is to avoid a high-pitched sound when moving values fast which will quickly annoy
   your colleagues in the lab.

*Occupant*
   The value to assign to a dial

*Factor*
   The dial's response is nonlinear, i.e. when advancing N 'clicks' the value will be advanced by N*(1+Factor*Speed)
   where speed is the speed at which the dial is rotated and Factor is the one you set here.

*Average*
   The speed is determined as the minimum speed registered during the last 'Average' clicks. Average is thus
   mis-labeled but that has no practical consequences. It just turned out to work better this way.

*Speed*
   While you can vary values using the panel at very high speeds it is not always advisable to update a scanning
   parameter at very high rates. The speed in ms given here tells Imspector how often it should test the (modified)
   value and adjust the measurement process or move the stage depending on the internal configuration.

*Click*
   Whether or not to issue the clicking sound for each movement.

*Beep*
   Whether or not to beep (system beep from the computer, will not be audible if the computer is muted) when hitting
   the minimum or maximum values.

Remarks 
........

.. note::
    While all parameters directly related to the MPD panel are set here, the size of a single step (i.e. the movement
    during a single click) is configured through the hardware parameters of the axis in question. Go to
    :menuselection:`&Hardware --> &Configure` and select the appropriate page (usually the 'DACs' subpage of a scanning
    device).
    For the NIDAQ driver the resolution is determined by the 'Resolution' parameter in logical units.
    A negative value will use a reasonable default which may, however, be too coarse for you. Other devices may be
    configured differently, refer to their documentation for details.

.. warning::
    The FTDI chip is used by many devices. All of them will eventually share one dll and driver located in the windows system directory.
    If installing the panel stops other hardware from working or vice versa, this is most probably due to
    incompatibilities of some older software with the newly installed drivers. Get someone with a thorough knowledge of such matters.
    MpcCtrl.exe should work with most version of the drivers - so all you have to do is to make sure that the dlls
    ('ftd2xx.dll' for 32bit Imspector and 'ftd2xx64.dll' for 64 bit Imspector) Imspector finds in the path and loads
    (dynamically) match the installed drivers.
