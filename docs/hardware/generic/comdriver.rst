Com Driver
************

This is a generic comport driver. It allows you to run small scripts at the beginning and the end of the whole
measurement and for each measurement step. A measurement axis is registered by the driver, so a simple stepping motor
or scanning device can be programmed through this driver.

What does wait/line mean?
..........................

Line refers here to the command line, not a scan line. Wait/line is the time that Imspector waits after it has send a command line.
If this waiting time is to short, part of the following commands may be lost. A value of about 300ms seems to work well at 9600baud.

What are Consts?
.................

Consts provides 10 constants to which you can refer to in the command sequence. E.g. \%f[C1] is replaced by the value of the constant C1. 
