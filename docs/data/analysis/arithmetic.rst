The Arithmetic Plugin
*************************

The Analysis/Arithmetics plugin is used to create new data stacks from existing data stacks and the relation between the old and the new
data is given as a function.

One or two Stacks can be selected (upper left panel of the Arithmetics dialog). The format of the data values of the output stack is
selected below. On the right upper panel you either select a pre-determined function (Scale, Add, Subtract, Multiply, Divide, Offset, Invert,
Normalize) which obvious meanings of the parameters and requiring one (scale, offset, invert, nomalize) or two (add, subtract, multiply,
divide) input stacks. The last option (Function) allows to input an arbitrary term (edit box in the lower part) which is then evaluated for
every position and data value of the input stack(s) and determines the values of the output stack.

The output stack can re-evaluate itself, should the data of the input stack change (Watch checkbox).

The Function parser which is used to evaluate the custom expressions is explained below.

The Function Parser
....................................

The size of the output stack equals the size of the input stack. The parser expression is evaluated at every position. The simplest possible

.. code-block::

  r
  
  

Get the pixel values of a stack to include it into your function: "STACKNAME".val(s,u,v,w)) Keep the "". You can get the stackname by pressing F2. 

Builtins 
++++++++

Variables
#########

Operators
#########
**%**
   The modulo operator. It works for real numbers too. 'r % (2*pi)' wraps a signal to the range of :math:`[0,2\pi]`
**//**
   The integer division operator. 'b*(a//b)+(a\% b)=a'

Functions
#########

Data Access
#########

Constants
#########
