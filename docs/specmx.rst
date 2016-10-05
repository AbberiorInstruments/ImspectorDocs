==========================
Imspector Matlab Interface
==========================

Imspector comes with a Matlab Interface named SpecMx which can be used by Matlab running on the same computer (to
enable sharing of measurement data) or even running on a different computer.

The usage is very similar to :ref:`specpy_`. The syntax is identical with the obvious conversions (dictionaries to structs, None to []).

The data content of a Stack in Imspector (obtained by Stack.data()) can only be read, not written from Matlab.