==============
 Test Matrices
==============

Given equation to solve is following Burger's equation with having both convection and diffusion terms:

.. math::

   \frac{\partial \phi}{\partial t} + U \frac{\partial \phi}{\partial x} = \frac{\partial}{\partial x}\left ( \Gamma \frac{\partial \phi}{\partial x} \right )

One dimensional domain is set to 40 as size with :math:`5 \leqslant x\leqslant 45`. Boundary conditions at both left and right node points are set to 0.

Consider two cases:

- CASE1: Euler equation without diffusion term: :math:`\Gamma = 0`

- CASE2: Burger's equation with diffusion term: :math:`\Gamma = 001`


-----------------------------------------
 Euler equation (Pure convection problem)
-----------------------------------------

- Grid setups: N = 1001, 2001, 4001, 6001
- Different Couran't number conditions: Cr = 0.25, 0.5, 0.75, 0.1 for N = 4001 only
- Test methods: Euler Explicit (EE), Euler Implicit (EI), and Crank-Nicolson (CR)
- No diffusivity: :math:`\Gamma` = 0


Stability check
^^^^^^^^^^^^^^^

1. Test on different time step

  - Stability was checked on grid setup with N = 4001 with different time step conditions.
  - If unstable solution appears with any inappropriate values, stability is NOT considered to be achieved.


    +------------------+---------+----------+---------+
    | Courant no. (dt) |   EE    |    EI    |   CR    |
    +==================+=========+==========+=========+
    | 0.25 (0.0025)    |   X     |    O     |    O    |
    +------------------+---------+----------+---------+
    | 0.5  (0.005)     |   X     |    O     |    O    |
    +------------------+---------+----------+---------+
    | 0.75 (0.0075)    |   X     |    O     |    O    |
    +------------------+---------+----------+---------+
    | 0.1  (0.01)      |   X     |    O     |    O    |
    +------------------+---------+----------+---------+
    (O: stable, X: unstable)

|

2. Test on different grid resolution

  - Stability was checked on different grid setup with fixed time step of dt = 0.005 [sec]
  - Note that Courant number must vary for different grid size to fix the time step: Following Courant numbers in table were chosed to set the 'dt' constant.

    +----------------------+---------+----------+---------+
    | Number of nodes (Cr) |   EE    |    EI    |   CR    |
    +======================+=========+==========+=========+
    | 1001 (0.125)         |   X     |    O     |   O     |
    +----------------------+---------+----------+---------+
    | 2001 (0.25)          |   X     |    O     |   O     |
    +----------------------+---------+----------+---------+
    | 4001 (0.5)           |   X     |    O     |   O     |
    +----------------------+---------+----------+---------+
    | 6001 (0.75)          |   X     |    O     |   O     |
    +----------------------+---------+----------+---------+
    (O: stable, X: unstable)

|


---------------------------------------------------
 Burger's equation (Convection + Diffusion problem)
---------------------------------------------------

- Grid setups: N = 1001, 2001, 4001, 6001
- Different Couran't number conditions: Cr = 0.25, 0.5, 0.75, 0.1 for N = 4001 only
- Test methods: Euler Explicit, Euler Implicit, and Crank-Nicolson
- Diffusivity: :math:`\Gamma` = 0.01


Stability check
^^^^^^^^^^^^^^^

1. Test on different time step

  - Stability was checked on grid setup with N = 4001 with different time step conditions.
  - If unstable solution appears with any inappropriate values, stability is NOT considered to be achieved.


    +------------------+---------+----------+---------+
    | Courant no. (dt) |   EE    |    EI    |   CR    |
    +==================+=========+==========+=========+
    | 0.25 (0.0025)    |   O     |    O     |    O    |
    +------------------+---------+----------+---------+
    | 0.5  (0.005)     |   O     |    O     |    O    |
    +------------------+---------+----------+---------+
    | 0.75 (0.0075)    |   X     |    O     |    O    |
    +------------------+---------+----------+---------+
    | 0.1  (0.01)      |   X     |    O     |    O    |
    +------------------+---------+----------+---------+
    (O: stable, X: unstable)


|

2. Test on different grid resolution

  - Stability was checked on different grid setup with fixed time step of dt = 0.005 [sec]
  - Note that Courant number must vary for different grid size to fix the time step: Following Courant numbers in table were chosed to set the 'dt' constant.
  - *Peclet* number are specifed in the following table. (Note: *Peclet* number can only be defined in diffusion term contained solution)

    +---------------------------+--------+--------+--------+
    | Number of nodes (Cr / Pe) |   EE   |   EI   |   CR   |
    +===========================+========+========+========+
    | 1001 (0.125 / 4.0)        |   O    |    O   |   O    |
    +---------------------------+--------+--------+--------+
    | 2001 (0.25 / 2.0)         |   O    |    O   |   O    |
    +---------------------------+--------+--------+--------+
    | 4001 (0.5 / 1.0)          |   O    |    O   |   O    |
    +---------------------------+--------+--------+--------+
    | 6001 (0.75 / 0.667)       |   X    |    O   |   O    |
    +---------------------------+--------+--------+--------+
    (O: stable, X: unstable)

|

