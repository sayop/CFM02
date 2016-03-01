=============
 Problem1 - e
=============

Discuss the computational time for different methods. Examine how the computational time depends on the grid resolution and evaluate the temporal complexity of the methods.

-----------------------------------------
 Euler equation (Pure convection problem)
-----------------------------------------

In this test, only a part of Euler-Explicit cases was employed for analysis because the method was unstable beyond certain value of Courant number.

1. Computational time with different time step, dt

  - The evaluation of computational time was done for single case of grid size, N = 4001.
  - Both Euler implicit and Crank-Nicolson methods show almost equivalent levels of computational time.
  - The computational time is dramatically dropping with increase of time step. This is quite natural phenomena because the bigger time increment will jump up to the targeted solution in time.


  .. figure:: ./images/EulerEqn_elapsedT_dt.png
     :scale: 60%


|

2. Computational time with different grid resolution

  - The evaluation of computational time was done for single set of time step, dt = 0.005, so different Courant number for variable grid size.
  - Using more number of grid points will consume more computational resource so longer computational time.

  .. figure:: ./images/EulerEqn_elapsedT_dx.png
     :scale: 60%



------------------------------------------- 
 Burger's equation (Convection + Diffusion)
-------------------------------------------


In this test, all the conditions of Euler-Explicit cases were employed for time consumption analysis regardless of instability of numerical solution. Even if instability happens in the solution, the computational time can be evaluated because the simulation was running without stopping. In that case, accuracy of simulation cannot be assessed as observed in the previous section.

1. Computational time with different time step, dt

  - The evaluation of computational time was done for single case of grid size, N = 4001.
  - Most interestingly, Euler explicit is quite efficient in computational time consumption.
  - In contrary to both implicit schemes, explicit scheme will not need to construct matrix.
  - Also it does NOT necessarily conduct any vector calculus which would basically require higher consumption of CPU time and memory storage.

  .. figure:: ./images/BurgersEqn_elapsedT_dt.png
     :scale: 60%


2. Computational time with different grid resolution

  - The evaluation of computational time was done for single set of time step, dt = 0.005, so different Courant number for variable grid size.
  - The pattern is same as the discussions above.

  .. figure:: ./images/BurgersEqn_elapsedT_dx.png
     :scale: 60%

