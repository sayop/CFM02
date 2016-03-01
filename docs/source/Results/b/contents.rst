=============
 Problem1 - b
=============

Plot :math:`\phi` vs. :math:`x` at :math:`t` = 20, 30, 40 and compare the numerical solution using the three methods with the analytical solution.

All the test case shown here were done with single set of grid size, N = 4001, and time step, dt = 0.005. 

-----------------------------------------
 Euler equation (Pure convection problem)
----------------------------------------- 

- CASE1: Euler-Explicit (EE) method

  This case was NOT successfully done with stability. Any change of time step and grid resolution didn't give stable solution because the Euler explicit for pure convection problem is unconditionally unstable.

- CASE2: Euler-Implicit (EI) method

  .. figure:: ./images/EI000.png
     :scale: 80%


- CASE3: Crank-Nicolson (CR) method

  .. figure:: ./images/CR000.png
     :scale: 80%


|


-------------------------------------------
 Burger's equation (Convection + Diffusion)
-------------------------------------------


- CASE1: Euler-Explicit (EE) method

  .. figure:: ./images/EE001.png
     :scale: 80%


- CASE2: Euler-Implicit (EI) method

  .. figure:: ./images/EI001.png
     :scale: 80%


- CASE3: Crank-Nicolson (CR) method

  .. figure:: ./images/CR001.png
     :scale: 80%


|



