Examples
*********************

Scale stack content about a factor a without changing the stack size
.......................................................................

Solution using the Interpolation-function:
+++++++++++++++++++++++++++++++++++++++++++

1. Obtain the size of the stack in pixel (using Ctrl + T) 
2. Using 'Analysis'-'Interpolation' create a new stack with size $aN_i$ (possible rounding errors!)
3. Change the stack size of the interpolated stack (using Strg. + T) to the old size and chose thereby the middle of the interval in pase position (whatever the signs are) 

Solution using Analysis/Arithmethics:
+++++++++++++++++++++++++++++++++++++++

If you did not have set an offset but want to scale about the center position:

zoom=a,
stack.func((x-X/2)/zoom+X/2,(y-Y/2)/zoom+Y/2,z,t)

Scaling is here in two dimensions, extension to 1D or 3D is straightforward
Insert the correct stack name instead of 'stack' 

without offset:

zoom=a,
stack.func(x/zoom,y/zoom,z,t)

Rotate stack by angle 'alpha'
..................................

Assumed you want to rotate in the xy-plain (first two dimensions) and the angle is provided in degree, rotation should be anti-clockwise...

arad=alpha/180*pi,
stack.func((x-X/2)*cos(arad)-(y-Y/2)*sin(arad)+X/2,(x-X/2)*sin(arad)+(y-Y/2)*cos(arad)+Y/2,z,t)

Rotate a 2D-stack and produce a rotational symmetric 3D-stack out of it
...........................................................................

This recipe is for a vertical rotation axis at x=a (a is number of pixel)

1. Copy 2D stack in new window, and set third dimension (Strg. + T) to the desired pixel size (in most case comparable to first dimension)
3. Rename the new stack to eg. stack3d
2. Use the following formula on the new stack

   a=??, stack3d.val(sqrt((s-a)\^2+(v-a)\^2)+a,u,0,0)

Creation of test objects
..............................

