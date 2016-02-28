from variables import flowVars, domainVars, postVars
import matplotlib.pyplot as plt

def plotSolution(time):
   x = domainVars.x
   phi = flowVars.phi
   exac = flowVars.exac
   imax = len(phi)
   pltFile = 'solution_%5.3f.png' % float(time)
   MinX = min(x)
   MaxX = max(x)
   MinY = -0.1#min(phi)
   MaxY = 1.0#1.1*max(phi)

   p = plt.plot(x,phi, 'k-', label='Numerical solution')
   p = plt.plot(x,exac, 'r--', label='Exact solution')
   plt.setp(p, linewidth='3.0')

   plt.axis([MinX,MaxX, MinY, MaxY])
   plt.xscale('linear')
   plt.yscale('linear')
   plt.xlabel('x', fontsize=22)
   plt.ylabel('phi', fontsize=22)

   plt.grid(True)
   #plt.text(0.01, 0.2, 'Grid size = %s' % len(phi), fontsize=22 )
   ax = plt.gca()
   xlabels = plt.getp(ax, 'xticklabels')
   ylabels = plt.getp(ax, 'yticklabels')
   plt.setp(xlabels, fontsize=18)
   plt.setp(ylabels, fontsize=18)
   plt.legend(
             loc='upper right',
             borderpad=0.25,
             handletextpad=0.25,
             borderaxespad=0.25,
             labelspacing=0.0,
             handlelength=2.0,
             numpoints=1)
   legendText = plt.gca().get_legend().get_texts()
   plt.setp(legendText, fontsize=18)
   legend = plt.gca().get_legend()
   legend.draw_frame(False)

   fig = plt.gcf()
   fig.set_size_inches(8,5)
   plt.tight_layout()
   plt.savefig(pltFile, format='png')
   plt.close()

   print "%s DONE!!" % (pltFile)

   # write a CSVfile
   csvFile = 'solution_%5.3f.csv' % float(time)
   writeCSV(csvFile,x,phi,exac)

def writeCSV(csvFile,x,phi,exac):
   import csv
   imax = len(x)
   c = csv.writer(open(csvFile, "wb"))
   c.writerow(["x","solution","exactSolution"])
   for i in range(imax):
      c.writerow([x[i], phi[i], exac[i]])
   print "%s DONE!!" % (csvFile)


def writeCSVtemporalPhi(csvFile,t,phi1,phi2):
   import csv
   imax = len(t)
   c = csv.writer(open(csvFile, "wb"))
   c.writerow(["t","xMeas1","xMeas2"])
   for i in range(imax):
      c.writerow([t[i], phi1[i], phi2[i]])
   print "%s DONE!!" % (csvFile)



def storeTemporalChange(tCurrent,iWriteCSV,xMeas1,xMeas2):
   postVars.timeTrace.append(tCurrent)
   # Search phi value at specified measurement position in x
   x = domainVars.x
   phi = flowVars.phi
   imax = len(x)
   for i in range(imax):
      if i == 0: continue
      # Find phi at xMeas1
      if (xMeas1 >= x[i-1]) and (xMeas1 < x[i]):
         distL = xMeas1 - x[i-1]
         distR = x[i] - xMeas1
         tmp = phi[i-1] + distL * phi[i] / (distL + distR)
         postVars.phiMeasured1.append(tmp)

      # Find phi at xMeas2
      if (xMeas2 >= x[i-1]) and (xMeas2 < x[i]):
         distL = xMeas2 - x[i-1]
         distR = x[i] - xMeas2
         tmp = phi[i-1] + distL * phi[i] / (distL + distR)
         postVars.phiMeasured2.append(tmp)

  
   # When simulation ends, the stored temporal phi trace should be stored in separate CSV file.
   if (iWriteCSV == 1):
      csvFile = 'temporalPhiChange.csv'
      writeCSVtemporalPhi(csvFile, postVars.timeTrace, postVars.phiMeasured1, postVars.phiMeasured2)
 
def computeError(imax,phiN,phiE):
   import numpy as np
   # Calculate RMS of error
   sumE = 0.0
   for i in range(imax):
      sumE += (phiN[i] - phiE[i]) ** 2
   RMS = np.sqrt(sumE / imax)
   return RMS
