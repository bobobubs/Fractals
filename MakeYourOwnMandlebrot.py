# -*- coding: utf-8 -*-
"""
Created on Sat May 21 23:33:46 2022

@author: macwr
"""
import numpy as np
import matplotlib.pyplot as plt

xs = np.linspace(-.22, -0.21, 1000)
ys = np.linspace(-.70, -.69, 1000)

xlen = len(xs)
ylen = len(ys)

atlas = np.zeros((ylen, xlen))


def mandle(c, iters):
    z = complex(0,0)
    for i in range(iters):
        z = (z*z) + c
        if abs(z) > 4:
            break
        else:
            pass
    return i

for ix in range(xlen):
    for iy in range(ylen):
        
        cx = xs[ix]
        cy = ys[iy]
        c = complex(cx, cy)
        atlas[iy, ix] = mandle(c, 120)
        pass
    pass

plt.figure(figsize=(18, 18))
plt.imshow(atlas, interpolation = "nearest")


