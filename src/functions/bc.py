from variables import simulationVars

def updateDirichletBC(inputDict,imax):
   print '# Updating boundary condition...'
   # left boundary
   phiL = float(inputDict['phiL'])
   simulationVars.A[0][0] = 1.0
   simulationVars.Q[0] = phiL
   # right boundary
   phiR = float(inputDict['phiR'])
   simulationVars.A[imax-1][imax-1] = 1.0
   simulationVars.Q[imax-1] = phiR
