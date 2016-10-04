SyncDriver
*************
The sync driver has two functions. It serves as a provider for 'dummy' axes and it
can do a low-accuracy sync with external devices by stopping the measurement until
a certain event has occurred on a serial-port line or by triggering an external
device by setting a serial-port line low or high.

Dummy Axes
..............

Passive Syncing
...............

Active Syncing
................

The SyncDriver cannot provide a pixel clock. It can, however set the output lines of 
the computers RS232 to high or low or pulse them in arbitrary sequences along the measurement
axes. The triggering is set up throught the 'TTL' property sheet in the measurement settings
and follows the standard TTLChannels scheme (\ref{sec:TTLChannels})
