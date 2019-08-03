import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

g = 9.81

class particle_teo:
    def __init__(self, dist_total, ang, dt=0.033):
        self.dist_total = dist_total
        self.ang = ang
        self.v0 = np.sqrt(self.dist_total * g / np.sin(2 * self.ang * np.pi / 180))
        self.t_total = 2 * self.v0 * np.sin(self.ang * np.pi / 180) / g
        self.v_xi = self.v0*np.cos(self.ang * np.pi /180)
        self.v_yi = self.v0*np.sin(self.ang * np.pi /180)
        self.dt = dt
        self.iters = self.t_total / self.dt
        
    def mov_x(self, vel_ini_x, t):
        vel_y = 0.5*g*t
        return vel_y

    def mov_y(self, vel_ini_y, t):
        pos_y = vel_ini_y * t - 0.5*g*t**2
        return pos_y
    
    def sim(self):
        t = np.linspace(0, self.t_total, int(np.around(self.iters)))
        posx_t = self.mov_x(self.v_xi, t)
        posy_t = self.mov_y(self.v_yi, t)
        res = np.array([t, posx_t, posy_t]).transpose()
        np.savetxt('test.txt', res, delimiter=',', header='t,x,y')

    def plot_sim(self):
        t, x, y = np.genfromtxt('test.txt', comments='#', skip_header=1, delimiter=',', unpack=True)
        plt.scatter(t,y)

class part_err(particle_teo):
    def __init__(self, dist_total, ang, dt=0.033, err1=0.03, err2=0.005):
        particle_teo.__init__(self, dist_total, ang, dt=0.033)
        self.err1 = err1
        self.err2 = err2
        
    def sim_Err(self):
        t = np.linspace(0, self.t_total, int(np.around(self.iters)))
        size_t = len(t)
        posx_t = self.mov_x(self.v_xi, t)
        posy_t = self.mov_y(self.v_yi, t)
        posx = posx_t + np.random.normal(size=size_t)*self.err1
        posy = posy_t + np.random.normal(size=size_t)*self.err1
        res = np.array([t, posx, posy]).transpose()
        np.savetxt('test_err.txt', res, delimiter=',', header='t,x,y')
        
    def plot_sim(self):
        terr, xerr, yerr = np.genfromtxt('test_err.txt', comments='#', skip_header=1, delimiter=',', unpack=True)
        t, x, y = np.genfromtxt('test.txt', comments='#', skip_header=1, delimiter=',', unpack=True)
        plt.scatter(terr,yerr)
        plt.plot(t, y)
