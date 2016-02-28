import numpy as np

class flowVars:
   U = []       # Convective velocity: coefficient of divergence term
   gamma = []   # diffusivity: coefficient of laplacian term
   sdot  = []   # source terms
   phi   = []   # dependent variable: principle variable for numerical solution
   exac  = []   # analytical solution
   phiL = 0.0
   phiR = 0.0
   
class simulationVars:
   A = []
   Q = []
   implicit = 0.0   

class domainVars:
   x = []
   dx = 0.0

class postVars:
   timeTrace = []
   phiMeasured1 = []
   phiMeasured2 = []
