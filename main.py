#!/usr/bin/env python3
"""
Created on Mon Dec 13 14:54:55 2021

@author: paveenju
"""
## These two following statements are used for the non-interactive mode
#import matplotlib
#matplotlib.use('Agg')

import matplotlib.pyplot as plt
#import tkinter as tk
import traffic

COLORS = ['blue', 'green']

def display(data, labels, savefig=False):
    plt.figure(figsize=(16,9))
    for (i, d) in enumerate(data):
        for p in d:
            plt.plot(p.x, p.y, '.', color='red' if p.cost > 0 else COLORS[i % len(COLORS)])

    plt.title('Flow intersection of two aircraft', pad=20, fontsize=18)
    plt.xlabel('X (NM)', fontsize=16)
    plt.ylabel('Y (NM)', fontsize=16)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.grid(linestyle='--')
    #plt.axis([-10, 10, -10, 10])
    #plt.legend(fontsize=14)

    if (savefig):
        plt.savefig('eps/flow_intersection.eps', pad_inches=0.1, bbox_inches='tight')

    plt.show()

if __name__ == '__main__':

    flights = traffic.from_file('DATA/TRAJECTORIES_A.out')
    display( [f.plots for f in flights], [f.call_sign for f in flights], True )
    