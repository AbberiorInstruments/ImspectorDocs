Cameras with DirectShow Drivers 
*******************************

Some, usually lower end, cameras come with DirectShow drivers which allow Imspector to drive them using a generic
driver. The driver is tested with the following models:

*mvBlueFox* (`Matrix Vision <http://www.matrix-vision.com/bildverarbeitungshardware.html>`_)
   Produced by Matrix Vision. Please install the appropriate driver from Matrix vision and test the camera using the
   software that comes with it before trying to use it with Imspector.
   In order to use the DirectShow driver you have to run the Matrix Vision configuration tool (mvDeviceConfigure
   .exe). Here you can set the DirectShow friendly name (the name which will show up in Imspector) and you HAVE TO
   register the device (in the Menu, there is a DirectShow entry that allows you to do this).
   If you have an x64 system you have to do this separately for x64 and x86 by running both the 32bit and 64bit version of the configuration utility.
   
   A (not necessarily up-to-date) version of the drivers can be found here: `(32bit) <http://imspector.mpibpc.mpg
   .de/extra/drivers/mvBlueFOX.msi>`_ and `(64bit) <http://imspector.mpibpc.mpg.de/extra/drivers/beta_mvBlueFOX-x64.msi>`_.

*Philips SPC900NC* (`Philips webpage <http://www.p4c.philips.com/cgi-bin/dcbint/cpindex.pl?ctn=SPC900NC/00&slg=en&scy=GB>`_)
   This camera is unfortunately not produced any more. If you have one: Lucky you, it has a decent chip and serves well as an overview cam.
*The Imaging Source* (`Products <http://www.theimagingsource.com/en_US/products/cameras/>`_)
   Offers a wide range of cameras. The driver runs with several of them - give it a try and if it does not work we will fix it.



