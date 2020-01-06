#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 22:18:17 2020

@author: seanbray
"""

import math 
import numpy as np
from matplotlib import pyplot as plt

class Passenger:
    def __init__(self, starting_point, end_point, speed):
        self.starting_point = starting_point
        self.end_point = end_point
        self.speed = speed
    
    def walk_time(self):
        distance = math.sqrt((self.starting_point[0]-self.end_point[0])**2+
                             (self.starting_point[1]-self.end_point[1])**2)
        return distance*self.speed

class Route:
    def __init__(self, route):
        self.route = route
    
    def plot_map(self):
         max_x = max([n[0] for n in self.route]) + 5 # adds padding
         max_y = max([n[1] for n in self.route]) + 5
         grid = np.zeros((max_y, max_x))
         for x,y,stop in self.route:
             grid[y, x] = 1
             if stop:
                 grid[y, x] += 1
         fig, ax = plt.subplots(1, 1)
         ax.pcolor(grid)
         ax.invert_yaxis()
         ax.set_aspect('equal', 'datalim')
         plt.show()
       
    def timetable(self):    
        '''
        Generates a timetable for a route as minutes from its first stop.
        '''
        time = 0
        stops = {}
        for step in self.route:
            if step[2]:
                stops[step[2]] = time
            time += 10
        return stops   
    
    def generate_cc(self):
        start = self.route[0][:2]
        cc = []
        freeman_cc2coord = {0: (1, 0),
                            1: (1, -1),
                            2: (0, -1),
                            3: (-1, -1), 
                            4: (-1, 0),
                            5: (-1, 1),
                            6: (0, 1),
                            7: (1, 1)}
        freeman_coord2cc = {val: key for key,val in freeman_cc2coord.items()}
        for b, a in zip(self.route[1:], self.route):
            x_step = b[0] - a[0]
            y_step = b[1] - a[1]
            cc.append(str(freeman_coord2cc[(x_step, y_step)]))
        return start, ''.join(cc)


class Journey:
    def __init__(self, route, Passengers):
        self.route = route
        self.passengers = Passengers
        self.starting_points = [self.passengers[i].starting_point for i in  range(len(Passengers))]
        self.end_points = [self.passengers[i].end_point for i in  range(len(Passengers))]
        self.speed = [self.passengers[i].speed for i in  range(len(Passengers))]
        
        
        
    def passenger_trip(self, passenger_id):
         start = self.starting_points[passenger_id]
         end   = self.end_points[passenger_id]
         pace  = self.speed[passenger_id]
         stops = [value for value in self.route.route if value[2]]
         # calculate closer stops
         ## to start
         distances = [(math.sqrt((x - start[0])**2 +
                            (y - start[1])**2), stop) for x,y,stop in stops]
         closer_start = min(distances)
         ## to end
         distances = [(math.sqrt((x - end[0])**2 +
                            (y - end[1])**2), stop) for x,y,stop in stops]
         closer_end = min(distances)
         return (closer_start, closer_end)
    
    
    def plot_bus_load(self):
        stops = {step[2]:0 for step in self.route.route if step[2]}
        for passenger_id in range(len(self.passengers)):
            trip = self.passenger_trip(passenger_id)
            stops[trip[0][1]] += 1
            stops[trip[1][1]] -= 1
        for i, stop in enumerate(stops):
            if i > 0:
                stops[stop] += stops[prev]
            prev = stop
        fig, ax = plt.subplots()
        ax.step(range(len(stops)), list(stops.values()), where='post')
        ax.set_xticks(range(len(stops)))
        ax.set_xticklabels(list(stops.keys()))
        plt.show()


    def travel_time(self, passenger_id):
        walk_distance_stops = self.passenger_trip(passenger_id)
        bus_times = self.route.timetable()
        bus_travel = bus_times[walk_distance_stops[1][1]] - \
                     bus_times[walk_distance_stops[0][1]]
        walk_travel = walk_distance_stops[0][0] * self.speed[passenger_id] + \
                     walk_distance_stops[1][0] * self.speed[passenger_id]
        return {"bus":bus_travel,"walk":walk_travel}

      
    def print_time_stats(self):
        trave_time_list = [self.travel_time(i) for i in range(len(self.passengers))]
        bus = [travel_time_list[i]["bus"] for i in range(len(self.passengers))]
        walk = [travel_time_list[i]["walk"] for i in range(len(self.passengers))]
        bus_average = np.mean(bus)
        walk_average = np.mean(walk)
        print((f" Average time on bus: {bus_average:3.2f} min \n"
               f" Average walking time: {walk_average:3.2f} min \n"))
   
