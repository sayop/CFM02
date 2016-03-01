=================
 Code Instruction
=================

The present project is aimed to develop a computer program for solving an unsteady solution with different numerical method. The code being used for answering all the question here is written with Python language. This program is to run with simple command::
 
  $ python main.py

Quick instruction for running the simulation
--------------------------------------------

The Python code used for this project can be cloned from *github.com* repository::

  $ git clone https://github.com/sayop/CFM02.git

Once you clone the code, you will see the following set of files and directories::

  $ sayop@reynolds:~$ ls CFM02/
  docs  README.md  src

*docs* contains the document files set for the current project using *Sphinx* software. This *pdf* document is online available at: http://cfm02-gatech.readthedocs.org. The Python script for this simulation is stored in *src* folder.

Before running the simulation, you need to open the file named *input.in* using editor for example, VI on unix system::
 
  $ vi input.in

Then, you should be able to see the following set of simulation parameters::

  #grid dimension
  iDim            6001
  xmin            5
  xmax            45
  #flow properties
  U               1
  gamma           0.01
  #boundary condition
  phiL            0.0
  phiR            0.0
  #simulation setup
  tStart          10.0
  tEnd            40.0
  maxIter         999999
  Courant         0.75
  implicit        0.0
  #Post-Process
  nIterWrite      200
  xMeas1          15.0
  xMeas2          25.0


The parameter's name above will literally tell you what every single variables indicates in the simulation. For the post-processing as requested in this project, two measurement point are specified with *xMeas1* and *xMeas2*. *nIterWrite* will write a solution plot and CSV file at speicifed interval of time integration number. 

Most importantly the current project code is constructed with :math:`\beta` method as described in the following section. The parameter *implicit* will specified :math:`\beta` value. *Courant* number will change the time integration interval, dt.

