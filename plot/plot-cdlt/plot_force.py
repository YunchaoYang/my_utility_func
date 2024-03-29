# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 10:55:40 2019

@author: Yunchao Yang 
"""
import math
import numpy as np
import matplotlib.pyplot as plt

class read_variable(object):
    def __init__(self, fname, column):
        """Return a Customer object whose name is *name*.""" 
        self.fname = fname
        self.column = column
        self.column = self.column - 1

        self.Step_all = []
        self.V_all = []

        try:
            with open(self.fname,'r') as fl:
                line1 = fl.readline()
                lines = fl.readlines()
                for line in lines:
                    step  = float(line.split()[0])
                    varia = float(line.split()[self.column])
                    self.Step_all.append(step)
                    self.V_all.append(varia)
        except:
            print("Cannot open file name")
   # def get_list(self):
     #   return [self.Step_all, self.V_all]
    
class WriteFigure(object):

    def __init__(self, Step_all, V_all, Vname):
        """Return a Customer object whose name is *name*.""" 
        self.Step_all = Step_all
        self.V_all = V_all
        self.Vname=Vname
        self.writepng()
    
    def writepng(self, yaxis_name = None):
        # create a new figure
        plt.figure()
        # plot the point (3,2) using the circle marker
        fig, = plt.plot(self.Step_all, self.V_all)
        
        variable_number = len(self.V_all)        
        second_half = int(len(self.V_all) / 2)        
        V_avg = sum(self.V_all[second_half:]) / float(second_half)
        
        #textstr = '\n$\mathrm{median}=%.2f$\n$\sigma=%.4f$'%(median, sigma)
        textstr = 'Mean result: %.4f'%(V_avg)
# get the current axes
        ax = plt.gca()
# Set axis properties [xmin, xmax, ymin, ymax]
#    ax.axis([0,6,0,10])
        ax.set_xlabel('Iterations')        
        if yaxis_name != None:
            ax.set_ylabel(yaxis_name)
        else:
           ax.set_ylabel(self.Vname) 
        # ax.set_title('Lift coefficient vs. iterations') 
        # these are matplotlib.patch.Patch properties
        props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

        # place a text box in upper left in axes coords
        ax.text(0.5, 0.15, textstr, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=props)

        name = self.Vname + '-'+ str(int(self.Step_all[0])) + '-' + str(int(self.Step_all[-1])) + '.png'
        print(name)
        plt.savefig(name)
#    plt.close(fig)



rho = 1.0
vel = 1.0
dp = 1.0/6.0
mu =  0.0055555
qs = 0.5*rho*vel**2  * math.pi * (dp)**2 / 4
qms = 0.5*rho*vel**2 * math.pi * (dp)**3 / 4

spa = '1'
dir1 = "Spa" + spa
basefilename='SettlingPart1_F.dat'
filename = dir1 + '/' + basefilename
#Iters =  np.array(read_variable(filename, 7).Step_all)
#Fx =  np.array(read_variable(filename, 7).V_all)
Iters = []
Fx = []
Fy = []
Fz = []
Tx = []
Ty = []
Tz = []

Step_all = []
V_all = []
try:
    with open(filename,'r') as fl:
        line1 = fl.readline()
        lines = fl.readlines()
except:
    print("Cannot open file name")
for line in lines:
    step  = float(line.split()[0])
    Iters.append(step)
    Fx.append(float(line.split()[6]))
    Fy.append(float(line.split()[7]))
    Fz.append(float(line.split()[8]))
    Tx.append(float(line.split()[9]))
    Ty.append(float(line.split()[10]))
    Tz.append(float(line.split()[11]))
    
Fx =  np.array(Fx)/qs
Fy =  np.array(Fy)/qs
Fz =  np.array(Fz)/qs
Tx =  np.array(Tx)/qms
Ty =  np.array(Ty)/qms
Tz =  np.array(Tz)/qms

time_lapse  = 0.6
rav         = float(spa)/(dp/2)
iterm_angle = 720
ang = (np.array(Iters) - time_lapse) * rav * 180 / math.pi - iterm_angle

plot1 = WriteFigure(Iters, Fx, "Fx")

with open(dir1 + "_Rot_ang_F.dat", 'w') as fname:
    fname.write("angle, Fx, Fy, Fz, Tx, Ty, Tz \n")
    for i in range(ang.size):
        if ang[i] > 0 and ang[i] <= 360:
            strline = str(ang[i]) + ','+  str(Fx[i]) +  \
            ','+  str(Fy[i]) +  \
            ','+  str(Fz[i]) +  \
            ','+  str(Tx[i]) +  \
            ','+  str(Ty[i]) +  \
            ','+  str(Tz[i]) + '\n'
            fname.write(strline)
