import numpy as np
from variables import domainVars

def createDomain(inputDict):
   print '# Creating one-dimensional domain...'
   imax = int(inputDict['iDim'])
   xmin = float(inputDict['xmin'])
   xmax = float(inputDict['xmax'])
   x = np.zeros(imax)
   
   dx = (xmax - xmin) / (imax - 1)
   for i in range(imax):
      x[i] = xmin + dx * i
   
   domainVars.x = x
   domainVars.dx = dx
   return 
