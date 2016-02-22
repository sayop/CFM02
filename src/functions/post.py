from variables import flowVars, domainVars
import matplotlib.pyplot as plt

def plotSolution(time):
   x = domainVars.x
   phi = flowVars.phi
   imax = len(phi)
   pltFile = 'solution_%5.3f.png' % float(time)
   MinX = min(x)
   MaxX = max(x)
   MinY = -0.1#min(phi)
   MaxY = 1.0#1.1*max(phi)

   p = plt.plot(x,phi, 'k-', label='Numerical solution')
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
             loc='lower left',
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
