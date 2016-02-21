import numpy as np
from variables import *

def initFlowVars(inputDict):
   print '# Initializing flow variables...'
   imax = int(inputDict['iDim'])
   uInit = float(inputDict['U'])
   gammaInit = float(inputDict['gamma'])

   flowVars.U      = uInit * np.ones(imax)
   flowVars.gamma  = gammaInit * np.ones(imax)
   flowVars.phi    = np.zeros(imax)
   flowVars.sdot   = np.zeros(imax)
   flowVars.exac   = np.zeros(imax)

   # Set matrices and vectors used for numerical methods
   # Coefficient mamtrix, A and Q vector for A * phi = Q
   simulationVars.A = np.zeros((imax,imax))
   simulationVars.Q = np.zeros(imax)


def setInitialCondition(imax):
   print '# Setting up initial condition...'
   # Initialize phi vector with given equation
   #print domainVars.x
   for i in range(imax-1):
      if i == 0: continue
      flowVars.phi[i] = 1.0 / np.sqrt((0.4 * np.pi)) * np.exp( -2.5 * (domainVars.x[i] - 10.0) ** 2 )
