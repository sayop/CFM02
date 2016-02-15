import numpy as np
import time
from discretization import updateAQMatrix
from bc import *
from variables import *
from init import setInitialCondition
from numericalSolution import *

def timeIntegrate(inputDict):
   tStart  = float(inputDict['tStart'])
   tEnd    = float(inputDict['tEnd'])
   Cr      = float(inputDict['Courant'])
   imax    = int(inputDict['iDim'])
   maxIter = int(inputDict['maxIter'])

   # start to count time for calculting computation performance
   start = time.clock()

   #
   # This part is to compute following finite difference equation:
   #     LHS = RHS
   #     LHS: phi^(n+1) - alphaImp * dt * f{phi^(n+1)}
   #     RHS: phi^(n) + (1-alphaImp) * dt * f{phi^(n)} + dt * Q
   # LHS: composed of next time level variable
   # RHS: composed of constants and present time level variable

   # alphaImp: implicit factor (0 ~ 1)
   # this factor is user-specified in 'inputs.in'
   # 0: fully explicit
   # 0.5: Crank-Nicolson method
   # 1: fully implicit
   alphaImp = simulationVars.implicit
   if alphaImp == 0:
      print '|- Simulation setup: Fully Explicit'
   elif alphaImp == 1:
      print '|- Simulation setup: Fully Implicit'
   elif alphaImp == 0.5:
      print '|- Simulation setup: Crank-Nicolson method'
   else:
      print '|- Simulation setup: Implicit factor %s' % alphaImp

   # Set boundary condition
   # This will populate the first and last elements of A matrix and Q vector
   updateDirichletBC(inputDict,imax)
 
   # Set initial condition
   # This will populate inner points of phi vector
   #setInitialCondition(imax)

   #
   # Time Marching:
   #
   print '=============================================='
   print '# Time integration starts at t = %s' % tStart
   print '=============================================='
   t = tStart
   nIter = 0
   while True:
      nIter += 1
      # Estimate dt from Courant number
      dt, Pe, Df = computeTimeStep(Cr,imax) 
      t += dt
      print "nIter = %s" % nIter, ", Time = %s" % t, ", dt = %s" % dt, ", Pe = %s" % Pe, ", Diffusion no = ", Df

      # IMPLICIT solution: will run only if alphaImp is non-zero.
      # EXPLICIT solution: will run only if alphaImp is zero.
      # Construct a coefficient matrix for system of linear equations
      updateAQMatrix(imax,dt,alphaImp)

      if alphaImp == 0.0:
         solveFullyExplicit(imax)
      elif alphaImp > 0.0:
         solveImplicit(imax)


      # Evaluate analytical solution
      #findExactSolution(imax,t)

      #print flowVars.exac
      if (t >= tEnd or nIter >= maxIter): break

   # EXPLICIT solution: will run only if alphaImp is zero.
   # This will solve following relation:
   #   phi^(n+1) = phi^(n) + dt * f{phi^(n)} + dt * Q

   #
   # time elapsed:
   elapsedTime = (time.clock() - start)
   print "## Elapsed time: ", elapsedTime



def computeTimeStep(Cr,imax):
   # Estimate time step from Courant number criteria.
   # Check Cr on every nodes and track the minimum among 
   dx = domainVars.dx
   dtMin = 99999.9
   Pe = 0.0
   for i in range(imax-1):
      if i == 0: continue
      dtMin = min(dtMin, Cr * dx / flowVars.U[i])
      # Peclet number: ratio of convection over diffusion
      Pe    = max(Pe, flowVars.U[i] * dx / flowVars.gamma[i])

   # diffusion number
   dfMin = 99999.9
   for i in range(imax-1):
      if i == 0: continue
      dfMin = min(dfMin, flowVars.gamma[i] * dtMin / dx ** 2)

   return dtMin, Pe, dfMin
