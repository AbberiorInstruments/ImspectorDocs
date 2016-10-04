.. _Changelog:

======================
Changelog
======================

This changelog is currently completely outdated.



Version v0.10 
-------------


v0.10rev4881
************

* Initialization of MppLib (COM/parallel/Remote/Usb ports) now runs in a separate thread and 
  startup can continue while initialization is unfinished.
* Serial ports are no longer tested during MppLib initialization, so delays are very unprobable
  now. Opening a serial port during initialization of a device can now fail with some OS error where
  before this port would not have been listed 
* Crash reports are now based on a modified `CrashRpt library`_.  
  Symbol files are no longer distributed. Crash reports are sent to the `imspector webserver`_.


