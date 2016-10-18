Examples for Arithmetics Plugin
**********************************

Thresholding an Image (one sided thresholding)
...............................................

First select the image to threshold at 'Stacks' using the pipette. Then set parameters to function. Then insert the formula: ``r>15?r:0``.  Finally Press 'Go …'
The formula contains following function: If a gray value is larger than 15 counts, leave it like it is. Otherwise set it to 0.

Thresholding an Image (two sided thresholding)
...............................................

First select the image to threshold at 'Stacks' using the pipette. Then set parameters to function. Then insert the formula: ``r>=15&r<20?r:0``.  Finally Press 'Go …'
The formula contains following function: If a gray value is larger than or equal to 15 counts and smaller than 20 counts, leave it like it is. Otherwise set it to 0.

Creation of an Image with Poisson noise (no structure)
............................................................

Insert the formula: ``poidev(n)``, where you substitute ``n`` with the desired average intensity value within the resulting image stack.

Creation of an Image with Poisson noise on an existing structure
...................................................................

First select the image to threshold at 'Stacks' using the pipette. Then set parameters to function. Insert the formula:
``poidev(r)`` which uses ``r``, the current intensity value of each pixel of the selected image stack.



Scale stack content about a factor a without changing the stack size
.......................................................................

**Solution using the Interpolation-function**

* Obtain the size of the stack in pixel (using :kbd:`ctrl + t`)
* Using 'Analysis'-'Interpolation' create a new stack with size ``aN_i`` (possible rounding errors!)
* Change the stack size of the interpolated stack (using kbd:`ctrl + t`) to the old size and chose thereby the middle
  of the interval in past position (whatever the signs are)

**Solution using Analysis/Arithmetics**

If you did not have set an offset on the stack but want to scale about the center position:

Parser expression: ``zoom=a,"stack name".func((x-X/2)/zoom+X/2,(y-Y/2)/zoom+Y/2,z,t)``

Scaling is here done in the first two dimensions. Extension to 1D or 3D is straightforward.
Insert the correct stack name instead of ``"stack name"``.


Rotate a 2D stack by angle
.............................................

Assuming the rotation should be anti-clockwise in the XY plane (first two dimensions) and the rotation angle ``alpha`` is given in deg.

Parser expression: ``arad=alpha/180*pi, stack.func((x-X/2)*cos(arad)-(y-Y/2)*sin(arad)+X/2,(x-X/2)*sin(arad)+(y-Y/2)*cos(arad)+Y/2,z,t)``

where stack is the name of the input data stack and alpha is the rotation angle in deg. Interpolation is applied.

Rotate a 2D-stack and produce a rotational symmetric 3D-stack out of it
...........................................................................

This recipe is for a vertical rotation axis at :math:`x=a` (a is number of pixel):

* Copy 2D stack in new window, and set third dimension (:kbd:`ctrl + t`) to the desired pixel size (in most case comparable to first dimension)
* Rename the new stack to eg. ``stack3d``
* Use the following formula on the new stack: ``a=??, stack3d.val(sqrt((s-a)\^2+(v-a)\^2)+a,u,0,0)``

Calculate a 2D Gaussian peak at the center
..........................................

Parser expression: ``sigma=5e-7,exp(-((x-(x0+X/2))^2+(y-(y0+Y/2))^2)/(2*sigma^2))``

Can be used to calculate a 2D Gaussian peak at the center of the current data stack.

A shortcut is: ``gaussian2D(x-(x0+X/2),y-(y0+Y/2),5e-7)``

where the width is given as full width half maximum (FWHM) and you can use 1D/2D/3D versions and as well for a Lorentzian function (use lorentzian1/2/3D in this case).

Note: Often made mistake is applying this function to a data stack with an integer data type and not changing the output
data type to a floating point type before evaluating the parser expression.