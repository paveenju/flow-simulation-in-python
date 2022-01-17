#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 15:22:28 2021

@author: paveenju
"""
class LoadingFileDescriptionError(Exception): pass

class Flight:
    
    def __init__(self, id, call_sign):
        self.id = id
        self.call_sign = call_sign
        self.plots = None
        
    def __repr__(self):
        return "<traffic.Flight {0}>".format(self.call_sign)
        
class FDPlot:
    
    def __init__(self, id, t, x, y, h, cat):
        self.id = id
        self.t = t
        self.x = x
        self.y = y
        self.h = h
        self.cat = cat
        self.vx = 0.
        self.vy = 0.
        self.hrate = 0.
        self.cost = 0.
        
    def __repr__(self):
        return "<traffic.FDPlot> ({0},{1},{2},{3})".format(self.t, self.x, self.y, self.h)
    
def from_file(filename):
    print ("Loading traffic:", filename + '...')
    file = open(filename)
    flights = []
    i = -1
    j = 0
    for line in file:
        try:
            if line[0] == '[':
                i += 1
                j = 0
                words = line.strip('[]\n').split()
                flight = Flight(int(words[0]), words[2])
                flight.plots = []
                flights.append(flight)
                
            else:
                words = line.strip().split()
                clock = words[1].split(':')
                t = int(clock[0])*60*60 + int(clock[1])*60 + int(clock[2])
                plot = FDPlot(int(words[0]), t, float(words[2]), float(words[3]), int(words[6]), int(words[8]))
                plot.vx = float(words[4])
                plot.vy = float(words[5])
                plot.hrate = float(words[7])
                plot.cost = float(words[9])
                flight.plots.append(plot)
        except IndexError as ie:
            print (line)
            raise LoadingFileDescriptionError(line)
            
    file.close()
    return flights