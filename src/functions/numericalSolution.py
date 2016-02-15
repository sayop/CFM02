import numpy as np
from variables import *

def solveFullyExplicit(imax):
   for i in range(imax):
      flowVars.phi[i] = simulationVars.Q[i] / simulationVars.A[i][i]

def solveImplicit(imax):
   A = simulationVars.A
   Q = simulationVars.Q

   # TDMA
   # Reference: http://www.cfd-online.com/Wiki/Tridiagonal_matrix_algorithm_-_TDMA_%28Thomas_algorithm%29
   # Forward elimination:
   b = np.zeros(imax)
   d = np.zeros(imax)
   b[0] = A[0][0]
   d[0] = Q[0]
   for i in range(imax):
      if i == 0: continue
      m = A[i][i-1] / b[i-1]
      b[i] = A[i][i] - m * A[i-1][i]
      d[i] = Q[i] - m * d[i-1]
   # Backward substitution:
   for i in reversed(range(imax)):
      if i == imax-1:
         flowVars.phi[i] = d[i] / b[i]
      else:
         flowVars.phi[i] = (d[i] - A[i][i+1] * flowVars.phi[i+1]) / b[i]


def findExactSolution(imax,t):
   for i in range(imax-1):
      if i == 0: continue
      if flowVars.gamma[i] != 0.0:
         flowVars.exac[i] = 1.0 / np.sqrt(0.4 * np.pi * flowVars.gamma[i] * t) * np.exp( -(domainVars.x[i] - flowVars.U[i] * t) ** 2 / (4.0 * flowVars.gamma[i] * t) )
      elif flowVars.gamma[i] == 0.0:
         flowVars.exac[i] = 1.0 / np.sqrt(0.4 * np.pi) * np.exp( -2.5 * (domainVars.x[i] - flowVars.U[i] * t) ** 2 )

