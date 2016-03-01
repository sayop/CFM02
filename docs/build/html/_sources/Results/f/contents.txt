=============
 Problem1 - f
=============

Discuss stability for different methods.

- Euler explicit method:

  - Euler explicit is conditionally stable for Burger's equation, which is having diffusion term.
  - This diffusion term tends to smooth the numerical solution out such that some possibility of instailiby appearance is reduced.
  - However, the stability can be acquired with proper *Peclet* number criteria, :math:`Pe \leq 2`
  - Euler explicit is necessarily unstable for Euler equation which is NOT having a diffusion term.
  - The central finite difference in Euler explicit does NOT guarantee the stability because numerical domain of influence of this scheme covers the redundant neighbor in pure convection problem.
  - This type of central finite difference creates a truncation error which makes numerical solution unstable.

- Euler implicit method:

  - This scheme is unconditionallyl stable.
  - This means any choice of dt and grid space will give stable solution set with some possibility of inaccuracy.

- Crank-Nicolson method:

  - This method of solution tends to be more stable than the Euler explicit even though it slows down the simulation.


Examine the maximum time step that leads to a stable solution.

- The maximum time step will depend on what type of solution method you use.
- Theoretically, Euler implicit will ensure you have stable solution with any time step choice if the equation is linear.
- The maximum time step you may choose for Euler explicit should be determined with consideration of *Peclet* number for Burger's equation only. Euler equation will be 100% unstable.

Which method provides the fastest solution for a given value of the numericall error?

- Euler explicit method will be fastest way of solving the problem if given equation contains the diffusion terms.
- Otherwise, for Euler equation with pure convection term, Crank-Nicolson scheme is the best solution for the faster solution rather than the Euler implicit.
 
