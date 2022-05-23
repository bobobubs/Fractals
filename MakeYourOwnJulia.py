# -*- coding: utf-8 -*-
"""
Created on Mon May 23 10:58:39 2022

@author: macwr
"""

# -*- coding: utf-8 -*-
"""
Created on Sat May 21 23:33:46 2022

@author: macwr
"""
import numpy as np
import matplotlib.pyplot as plt
xmin= -1
xmax = 1
ymin = -1.5
ymax = 1.5
xs = np.linspace(xmin, xmax, 1000)
ys = np.linspace(ymin, ymax, 1000)

xlen = len(xs)
ylen = len(ys)

c = complex(0.355534, - 0.337292)

atlas = np.zeros((ylen, xlen))


def julia(z, c, iters):
    for i in range(iters):
        z = (z*z) + c
        if abs(z) > 4:
            break
        else:
            pass
    return i

def create(c, iters, xs, ys):
    for ix in range(xlen):
        for iy in range(ylen):           
            zx = xs[ix]
            zy = ys[iy]
            z = complex(zx, zy)
            atlas[iy, ix] = julia(z, c, iters)
            pass
        pass
    return atlas

atlas = create(c,  1000, xs, ys)
plt.figure(figsize=(18, 18))
extent = [xmin , xmax, ymin , ymax]
plt.imshow(atlas, interpolation = "nearest", extent=[xmin , xmax, ymin , ymax])


