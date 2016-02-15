from variables import *

def readInput():
   print '# Reading input file...'

   inputDict = {}
   with open("input.in") as f:
      for line in f:
         li = line.strip()
         if li.startswith("#"): continue
         (key, val) = line.split()
         inputDict[key] = val

   # Set implicit factor
   simulationVars.implicit = float(inputDict['implicit'])

   return inputDict


