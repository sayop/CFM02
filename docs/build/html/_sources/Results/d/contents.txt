=============
 Problem1 - d
=============

Examine the numerical errors for different schemes as a function of the grid spacing and the integration time step. Evaluate the spatial and temporal accuracy of the numerical schemes.

Here, temporal and spatial accuracies were evaluated using following parameter:

.. math::

   P_{temporal} = \frac{log(\frac{\phi_{2t} - \phi_{4t}}{\phi_{t} - \phi_{2t}})}{log(2)}   

.. math::

   P_{spatial} = \frac{log(\frac{\phi_{2h} - \phi_{4h}}{\phi_{h} - \phi_{2h}})}{log(2)}




-----------------------------------------
 Euler equation (Pure convection problem)
----------------------------------------- 

In this test, the Euler-Explicit scheme was not employed because it is unconditionally unstable method for pure convection problem.

1. Errors as a function of time step, dt

  - The evaluation of time step change effect was done for single case of grid size, N = 4001.

  .. figure:: ./images/EulerEqn_error_dt.png
     :scale: 60%

  +------------------+-----------------+------------------+
  | Courant no. (dt) |    EI           |   CR             |
  +==================+=================+==================+
  | 0.25 (0.0025)    | 0.0166148385052 | 0.00099101659914 |
  +------------------+-----------------+------------------+
  | 0.5  (0.005)     | 0.0281716938047 | 0.00108091830901 |
  +------------------+-----------------+------------------+
  | 0.75 (0.0075)    | 0.0368227088826 | 0.0012308579817  |
  +------------------+-----------------+------------------+
  | 0.1  (0.01)      | 0.0436049875194 | 0.00144069783592 |
  +------------------+-----------------+------------------+

|


  - Evaluation of temporal accuracy :math:`P_{temporal}` defined below with different methods:

    - :math:`P_{temporal}` for EI = 0.4173
    - :math:`P_{temporal}` for CR = 2.0007

|

2. Errors as a function of grid spacing

  - The evaluation of grid resolution effect on error was done for single set of time step, dt = 0.005, so different Courant number.

  .. figure:: ./images/EulerEqn_error_dx.png
     :scale: 60%


  +----------------------+---------+-----------------+-------------------+
  | Number of nodes (Cr) | dx      |    EI           |   CR              |
  +======================+=========+=================+===================+
  | 1001 (0.125)         | 0.04    | 0.0294768440151 | 0.0150567999236   |
  +----------------------+---------+-----------------+-------------------+
  | 2001 (0.25)          | 0.02    | 0.0282487385682 | 0.00395484817586  |
  +----------------------+---------+-----------------+-------------------+
  | 4001 (0.5)           | 0.01    | 0.0281716938047 | 0.00108091830901  |
  +----------------------+---------+-----------------+-------------------+
  | 6001 (0.75)          | 0.00667 | 0.0281685389275 | 0.000547240822165 |
  +----------------------+---------+-----------------+-------------------+

  
|

  - Evaluation of spatial accuracy :math:`P_{spatial}` defined below with different methods:

    - :math:`P_{spatial}` for EI = 3.9946
    - :math:`P_{spatial}` for CR = 1.9497

|

------------------------------------------- 
 Burger's equation (Convection + Diffusion)
-------------------------------------------

In this test, only a part of Euler-Explicit cases was employed for analysis because the method was unstable beyond certain value of Courant number.

1. Errors as a function of time step, dt

  - The evaluation of time step change effect was done for single case of grid size, N = 4001.

  .. figure:: ./images/BurgersEqn_error_dt.png
     :scale: 60%


  +------------------+------------------+------------------+-------------------+
  | Courant no. (dt) |     EE           |    EI            |   CR              |
  +==================+==================+==================+===================+
  | 0.25 (0.0025)    | 0.00383043947008 | 0.00340998441819 | 8.76084904269e-05 |
  +------------------+------------------+------------------+-------------------+
  | 0.5  (0.005)     | 0.00818535015496 | 0.00646574830074 | 9.55709046347e-05 |
  +------------------+------------------+------------------+-------------------+
  | 0.75 (0.0075)    | inf              | 0.00922821563363 | 0.000108841001593 |
  +------------------+------------------+------------------+-------------------+
  | 0.1  (0.01)      | inf              | 0.0117416771678  | 0.000127423869135 |
  +------------------+------------------+------------------+-------------------+

|

  - Evaluation of temporal accuracy :math:`P_{temporal}` defined below with different methods:

    - :math:`P_{temporal}` for EI = 0.7879
    - :math:`P_{temporal}` for CR = 2.0001


|

2. Errors as a function of grid spacing

  .. figure:: ./images/BurgersEqn_error_dx.png
     :scale: 60%


  +----------------------+---------+------------------+------------------+-------------------+
  | Number of nodes (Cr) | dx      |     EE           |    EI            |   CR              |
  +======================+=========+==================+==================+===================+
  | 1001 (0.125)         | 0.04    | 0.00829334418324 | 0.00659287238512 | 0.00136897946621  |
  +----------------------+---------+------------------+------------------+-------------------+
  | 2001 (0.25)          | 0.02    | 0.00818432743363 | 0.00647642954911 | 0.000350398456828 |
  +----------------------+---------+------------------+------------------+-------------------+
  | 4001 (0.5)           | 0.01    | 0.00818535015496 | 0.00646574830074 | 9.55709046347e-05 |
  +----------------------+---------+------------------+------------------+-------------------+
  | 6001 (0.75)          | 0.00667 | inf              | 0.00646469348398 | 4.83756513792e-05 |
  +----------------------+---------+------------------+------------------+-------------------+


|

  - Evaluation of spatial accuracy :math:`P_{spatial}` defined below with different methods:

    - :math:`P_{spatial}` for EI = 3.4465
    - :math:`P_{spatial}` for CR = 1.9990



|



