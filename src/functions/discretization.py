from variables import simulationVars, domainVars, flowVars
import numpy as np

def updateQvector(imax,dt,alphaImp):
   # This is to only update Q vector for use of explicit scheme.
   # If it runs with explicit, updating A matrix is not necessary. 
   # Updating A matrix with explicit is redundant process.
   f = np.zeros((imax,imax))

   # Construct first f matrix
   # f is a temporary matrix to store each of coefficients set associated with
   # divergence and laplacian terms, respectively: f = f_divergence + f_laplacian
   f = constructDivergenceTerm(f,imax)
   f = constructLaplacianTerm(f,imax)
   #
   # This will populate the Q vector elements: RHSs
   #
   
   for i in range(imax-1):
      if i == 0: continue
      # RHS-(1)
      simulationVars.Q[i] = flowVars.phi[i]

      # RHS-(2)
      iL = i - 1
      iR = i + 1
      simulationVars.Q[i] += (1.0 - alphaImp) * f[i][i]  * flowVars.phi[i]  * dt
      simulationVars.Q[i] += (1.0 - alphaImp) * f[i][iL] * flowVars.phi[iL] * dt
      simulationVars.Q[i] += (1.0 - alphaImp) * f[i][iR] * flowVars.phi[iR] * dt

      # RHS-(3)
      simulationVars.Q[i] += dt * flowVars.sdot[i]
   
   

def updateAQMatrix(imax,dt,alphaImp):
   # Updating A matrix and Q vector for implicit scheme!
   
   # Construct A*phi = Q
   f = np.zeros((imax,imax))

   # This part is to compute following finite difference equation:
   #     LHS = RHS
   #     LHS: phi^(n+1) - alphaImp * dt * f{phi^(n+1)}
   #          --------- ------------------------------
   #           LHS-(1)            LHS-(2)
   #     RHS: phi^(n) + (1-alphaImp) * dt * f{phi^(n)} + dt * sdot
   #          -------   ------------------------------   ---------
   #          RHS-(1)              RHS-(2)                RHS-(3)
   # LHS: composed of next time level variable
   # RHS: composed of constants and present time level variable

   #
   # This will populate the tridiagonal elements of A matrix: LHSs
   #
   # NOTE: This will skip elements corresponding to boundary node points
   # First job is to populate '1' along the diagonal components to reflect
   # phi^(n+1).

   # LHS-(1)
   for i in range(imax-1):
      if i == 0: continue
      simulationVars.A[i][i] = 1.0
      # remove previously updated neighbor's coefficients
      simulationVars.A[i][i-1] = 0.0
      simulationVars.A[i][i+1] = 0.0

   # LHS-(2)
   # Construct first f matrix
   # f is a temporary matrix to store each of coefficients set associated with
   # divergence and laplacian terms, respectively: f = f_divergence + f_laplacian
   f = constructDivergenceTerm(f,imax)
   f = constructLaplacianTerm(f,imax)
   # Add LHS-(2) to LHS-(1) and complete A matrix
   simulationVars.A += -alphaImp * dt * f

   #
   # This will populate the Q vector elements: RHSs
   #
   
   for i in range(imax-1):
      if i == 0: continue
      # RHS-(1)
      simulationVars.Q[i] = flowVars.phi[i]

      # RHS-(2)
      iL = i - 1
      iR = i + 1
      simulationVars.Q[i] += (1.0 - alphaImp) * f[i][i]  * flowVars.phi[i]  * dt
      simulationVars.Q[i] += (1.0 - alphaImp) * f[i][iL] * flowVars.phi[iL] * dt
      simulationVars.Q[i] += (1.0 - alphaImp) * f[i][iR] * flowVars.phi[iR] * dt

      # RHS-(3)
      simulationVars.Q[i] += dt * flowVars.sdot[i]
  

#def updateDirichletBC(imax,A,Q):

def constructDivergenceTerm(f,imax):
   dx = domainVars.dx
   # f_divergence = -U/(2dx) * [phi_(i+1) - phi_(i-1)]
   # NOTE: This is a coefficient matrix. 'phi' can't be included in this matrix!!
   for i in range(imax-1):
      if i == 0: continue
      iL = i - 1
      iR = i + 1
      f[i][iL] += + 0.5 * flowVars.U[i] / dx
      f[i][iR] += - 0.5 * flowVars.U[i] / dx

   return f


def constructLaplacianTerm(f,imax):
   # f_laplacian = gamma/dx^2 * [phi_(i+1) - 2*phi_(i) + phi_(i-1)]
   dx = domainVars.dx
   invDxSqr = 1.0 / dx ** 2
   # NOTE: This is a coefficient matrix. 'phi' can't be included in this matrix!!
   for i in range(imax-1):
      if i == 0: continue
      iL = i - 1
      iR = i + 1
      gammaL = 0.5 * ( flowVars.gamma[i] + flowVars.gamma[iL] )
      gammaR = 0.5 * ( flowVars.gamma[i] + flowVars.gamma[iR] )
      f[i][i]  += -invDxSqr * (gammaL + gammaR)
      f[i][iL] += +invDxSqr * gammaL
      f[i][iR] += +invDxSqr * gammaR

   return f 

