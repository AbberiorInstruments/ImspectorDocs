The Arithmetics Plugin
*************************

The Analysis/Arithmetics plugin is used to create new data stacks from already existing data stacks and the relation
between the old and the new data is specified by a function.

.. figure:: /images/data/analysis/arithmetics_dialog.png
   :width: 10 cm
   :align: center

   Arithmetic operations dialog.

One or two Stacks can be selected (upper left panel of the Arithmetic Operations dialog). The format of the data values
of the output stack is selected below.

On the right upper panel, you either select a pre-determined function (Scale, Add, Subtract, Multiply, Divide, Offset,
Invert, Normalize) with obvious meanings of the parameters and requiring one (scale, offset, invert, normalize) or two
(add, subtract, multiply, divide) input stacks.

The last option (Function) allows to input an arbitrary term (edit box in the lower part) which is then evaluated for
every position and of the input stack(s) and determines the values of the output stack.

The function parser expression executes point-wise through the input stack and therefore has some restrictions compared
to a general treatment of input data with a script containing loops and conditions (although simple conditions can be
included).

The output stack can re-evaluate itself, should the data of the input stack change (Watch checkbox). And a convenient
way to modify the function later on is Right-Click/Manage and Manipulate Data/Edit Stack (:kbd:`ctrl + shift + e`).

The Function parser which is used to evaluate the custom expressions is explained below.


The Function Parser
----------------------------

The dimensions of the output stack will equal the dimensions of the input stack. The given parser expression is evaluated
at every position and the resulting value is stored in the output stack.

A very simple expression is ``r`` which just replicates the input stack (because ``r`` denotes the actual value of the input stack).

*Substitutions* are possible, new variables can be assigned and are used in all remaining terms, the last term must then
yield a value which determines the value of the output stack.

Example: ``a=5,r*a``

Creates a variable ``a`` with the value ``5`` and then computes ``r*a`` which means the output stack will be equal to
values of the input stack multiplied by five.

Numerical values can be also inserted in scientific notation, for example: ``3.5e-6``.

In the following the different element types are listed.

================= =========================================================================================================================
Built-in variable Description
================= =========================================================================================================================
``r``             Value of each pixel in the input stack.
``R``             Value of each pixel in the second input stack (if given).
``s,u,v,w``       Pixel position (starting at zero) of the actual position in the input stack(s) in 1st, 2nd, 3rd, 4th dimension.
``x,y,z,t``       Physical position of the actual position in the input stack in 1st, 2nd, 3rd, 4th dimension.
================= =========================================================================================================================

================== =========================================================================================================================
Built-in operators Description
================== =========================================================================================================================
``+,-,*,/``        Basic algebraic operations.
``<,>,==,>=,<=``   Logical comparisons, results in 0 (false) or 1 (true).
``^``              Power
``%``              Modulo. Also for real valued input (example: ``r%(2*pi)`` wraps to :math:`[0,2\pi)`)
``//``             Integer division (example: ``b*(a//b)+a%b==a`` should return 1)
================== =========================================================================================================================

================== =========================================================================================================================
Built-in constants Description
================== =========================================================================================================================
``pi``             Pi
``S,U,V,W``        Total number of pixels in the input stack(s) in 1st, 2nd, 3rd, 4th dimension.
``X,Y,Z,T``        Total physical lengths of input stack(s) in 1st, 2nd, 3rd, 4th dimension.
``x0,y0,z0,t0``    Physical offsets of input stack(s) in 1st, 2nd, 3rd, 4th dimension.
================== =========================================================================================================================

Some common built-in functions are listed here. A complete list can be obtained by pressing :kbd:`F2` in the parser window.
Built-in functions are used with parenthesis and comma separated arguments.

================== =========================================================================================================================
Built-in functions Description
================== =========================================================================================================================
``sqrt``           Square root
``sin,cos,tan``    Since, cosine, tangent
``asin,acos,atan`` Inverse sine, cosine, tangent
``asin2``          Inverse tangent given ``y,x`` separately.
``min, max``       Minimum/maximum of two values
``abs``            Absolute value (for integer and floating point numbers)
``floor,ceil``     Closest integer values rounded towards -Infinity/Infinity
``exp,ln``         Exponential, natural logarithm
================== =========================================================================================================================

Example of an advanced parser expression
++++++++++++++++++++++++++++++++++++++++

``sigma=5e-7,exp(-((x-(x0+X/2))^2+(y-(y0+Y/2))^2)/(2*sigma^2))``

Creates a new stack with the same dimensions and pixel sizes of the input stack and the values of this new stack will
be correspond to a 2D centered Gaussian with a certain standard deviation ``sigma``. Current values in the input stack
are not regarded.

Access of input stack values
++++++++++++++++++++++++++++

When applying a parser expression the arithmetics plugin:

* loops over all pixel of the input stack,
* evaluates the parser expression at each pixel position and
* assign the generated value as value of the output stack at this position.

Access to the current value of the input stack in the parser expression is via the variable ``r`` (and ``R`` for the
second input stack if a second stack has been selected).

However, it is also possible to access values at different positions in the actual data stack or values in a different
data stack with variables ``s,u,v,w`` or ``x,y,z,t``. In this case, the ``stack name`` (can access any open data stack in Imspector)
has to be given followed by a dot and ``val(s,u,v,w)`` or ``func(x,y,z,t)``. Stack names are typically printed in quotes since
they can contain spaces.

Example: ``"ExpControl #2 {6}".val(s,u,v,w)``

This expression would produce equal results to the much simpler ``r`` if the selected stack has the name ``“ExpControl #2 {6}”``.
(Press :kbd:`F2` to get a list of all known objects.) The arguments ``(s,u,v,w)`` do not have to be in this order and can
be complex expressions themselves (see example Rotate a 2D stack).

Example: ``"ExpControl #2 {6}".val(u,s,v,w)``

For a square (equal number of pixels in 1st and 2nd dimension) 2D stack this exchanges the 1st and 2nd dimension, effectively
mirroring the stack along the y=x line.

Notes:

* ``func(x,y,z,t)`` will interpolate if pixel positions are not hit directly
* ``val(..)`` and ``func(..)`` will return 0 if the given arguments are outside of the current data stack position ranges

Built-in advanced expressions
+++++++++++++++++++++++++++++

*Conditionals*: ``Condition ? expression 1 : expression 2``

Condition is a logical expression (zero is regarded as false and everything not zero is regarded as true). Depending on
the outcome either expression 1 (true) or expression 2 (false) is evaluated.

Example: ``a > b ? a : b`` is equivalent to ``max(a,b)``.

*Random number generation*

Random numbers can be generated at each pixel position and the parameter for the random number generation can depend on
the value of the input stack or an expression containing the value of the input stack.

===================== ======================================================================================
``rand(max, min)``	  Equally distributed random numbers in [min, max)
``gaussdev(sigma)``	  Normally distributed random numbers with a certain standard deviation.
``poidev(avrg)``	  Poisson distributed random numbers with a certain mean value.
===================== ======================================================================================

Summary
-----------

The Arithmetic Operations dialog can be used to create derived data stacks calculating functions depending on values of
input stacks. The functions are calculated point-wise which restricts the flexibility compared to for example running a
custom script on the data with Python. Nevertheless, advanced features like conditionals or generation of random numbers
make it a versatile and relatively easy to use tool. Imspector can keep track of updates in underlying input stacks and
update the values of the derived stacks automatically by re-evaluating the stored parser expressions.
