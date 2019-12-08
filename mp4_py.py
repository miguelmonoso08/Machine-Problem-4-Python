import numpy as np
import math as mt
import matplotlib.pyplot as plt
import time

h = float(input("Initial height: "))
v = float(input("Initial velocity: "))
ad = float(input("Angle (in degrees): "))
ax = float(input("x-component acceleration: "))
ay = float(input("y-component acceleration (in negative): "))

if ay >= 0:
    print("Invalid vertical acceleration value.")
    time.sleep(3)
    quit()
    
ad = mt.radians(ad)
vx = v*mt.cos(ad)
vy = v*mt.sin(ad)
rt = [ay/2, vy, h]
tm = max(np.roots(rt))
r = np.arange(0,tm,0.1)
x = np.zeros(len(r)+1)
y = np.zeros(len(r)+1)
t = 0.1
x[0] = 0
y[0] = h
p = np.arange(0,len(r)-1,1)

for o in p:
    xt = (ax*(t**2))/2 + vx*t
    yt = (ay*(t**2))/2 + vy*t + h
    x[o+1] = xt
    y[o+1] = yt
    t=t+0.1
    
x[len(r)] = ((ax/2)*tm**2) + vx*tm
y[len(r)] = 0

plt.plot(x,y, color="purple")
plt.title ("Projectile Motion")
plt.xlabel ("Distance")
plt.ylabel ("Height")
plt.grid()