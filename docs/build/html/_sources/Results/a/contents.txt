=============
 Problem1 - a
=============

Develop a finite difference algorithm for this transportation equation. Use Euler explicit, Euler implicit and Crank-Nicolsol schemes. Employ TDMA for solving implicit terms.

----------------------------------------
 Generalized form of numerical algorithm
----------------------------------------

In this project, three different methods are supposed to be employed to solve the give transport equation. Many terms of three methods are having very similar form in common, so it is better to construct the algorithm with a parameters that switch the solution methods in specified condition. This is called :math:`\beta`-method. In this method of solution, a user-specified parameter :math:`\beta` is employed amd used for swtiching the solution method with proper value varying from 0 to 1.

The given equation is manipulated by employing a new function :math:`f(\phi)` that represents the time derivative quantity as a function of dependent variable :math:`\phi`.

.. math::

   \frac{\partial \phi}{\partial t} = f(\phi)

where, 

.. math::

   f(\phi) = -U\frac{\partial \phi}{\partial x} + \frac{\partial}{\partial x}\left ( \Gamma \frac{\partial \phi}{\partial x} \right )


This form of equation can then be recast with forward finite difference in time as a explicit form:

.. math::

   \phi^{n+1} = \phi^{n} + \Delta t f(\phi^{n})


An implicit form of this finite difference can also be expressed as:

.. math::

   \phi^{n+1} = \phi^{n} + \Delta t f(\phi^{n+1})


Here, a new parameter :math:`\beta` applies to give finite difference above and creates a new from of finite difference as:

.. math::

   \phi^{n+1} = \phi^{n} + \Delta t \left [ (1-\beta)f(\phi^{n}) + \beta f(\phi^{n+1}) \right ]


Applying central finite difference with second order accuracy in space to :math:`f(\phi)` gives following:

.. math::

   f(\phi^{n}) = -U\frac{\phi^{n}_{i+1} - \phi^{n}_{i-1}}{2 \Delta x} + \Gamma \frac{\phi^{n}_{i+1} - 2\phi^{n}_{i} + \phi^{n}_{i-1}}{\Delta x^2}


Manipulating the above form of solution method gives the generalized form of solution method. This can be applied to any implicit method as well as explicit method. :math:`\beta = 0` indicates the Euler explicit method and :math:`\beta = 1` reformulates the method to Euler implicit. :math:`\beta = 0.5` will form a Crank-Nicolson method.

In case of Euler explicit method, only one unkown appears in the left hand side at :math:`i` position, so it can be solved exclusived for the new time levet at the corresponding position with known values of neighbor node information. Otherwise, three unknowns including left and right neighbors will appear so it should be resolved implicitly. For the implicit solution method, block-iterative method, TDMA for example, should be employed for resolving all the unkown values for the next time level.

With give generalized method of formulation, the code will construct :math:`A` matrix for any case of :math:`\beta` value. However, if :math:`\beta` is specified with 0, the coefficient matrix :math:`A` will be formed as a unity diagonal matrix with all zero values of off-diagonal elements. Thus, the explicit case with :math:`\beta = 0` does not necessarily have to perform TDMA method, which is computationally expensive. Rather, it can be exclusively solved as the present Python code is constructed for this purpose.


   


