#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 21:38:48 2020

@author: seanbray
"""

from classes import Passenger, Route, Journey

## Tests for Passenger class 

def test_passenger_constructor_startingpoint():
    passenger = Passenger((0,0),(1,2),10)
    result = passenger.starting_point
    assert result == (0,0)

def test_passenger_constructor_endpoint():
    passenger = Passenger((0,0),(1,2),10)
    result = passenger.end_point
    assert result == (1,2)

def test_passenger_constructor_speed():
    passenger = Passenger((0,0),(1,2),10)
    result = passenger.speed
    assert result == 10

def test_passenger_at_endpoint():
    passenger_enpoint = Passenger((1,2),(1,2),10)
    result = passenger_enpoint.walk_time()
    assert result == 0
    
def test_passenger_zero_speed():
    passenger_zero_speed = Passenger((0,0),(2,2),0)
    result = passenger_zero_speed.walk_time()
    assert result == 0
    

## Tests for Route class 
def test_route_constructor():
    route = [ ( 2, 1, 'A'), ( 3, 1, ''), ( 4, 1, ''), ( 5, 1, ''),
              ( 6, 1, ''), ( 7, 1, 'B'), ( 7, 2, ''), ( 8, 2, ''),
              ( 9, 2, ''), (10, 2, ''), (11, 2, 'C'), (11, 1, ''),
              (12, 1, ''), (13, 1, ''), (14, 1, ''), (14, 2, 'D'),
              (14, 3, ''), (14, 4, ''), (13, 4, ''), (12, 4, ''),
              (11, 4, ''), (10, 4, ''), ( 9, 4, ''), ( 9, 5, 'E'),
              ( 9, 6, ''), (10, 6, ''), (11, 6, 'F'), (12, 6, ''),
              (13, 6, ''), (14, 6, ''), (15, 6, ''), (16, 6, 'G') ]

    test_route = Route(route)
    result = test_route.route
    assert result == route

def test_route_timetable_no_stops():
    route_no_stops = [( 2, 1, ''), ( 3, 1, ''), ( 4, 1, ''), ( 5, 1, ''),
                      ( 6, 1, ''), ( 7, 1, ''), ( 7, 2, ''), ( 8, 2, ''),
                      ( 9, 2, ''), (10, 2, ''), (11, 2, ''), (11, 1, ''),
                      (12, 1, ''), (13, 1, ''), (14, 1, ''), (14, 2, ''),
                      (14, 3, ''), (14, 4, ''), (13, 4, ''), (12, 4, ''),
                      (11, 4, ''), (10, 4, ''), ( 9, 4, ''), ( 9, 5, ''),
                      ( 9, 6, ''), (10, 6, ''), (11, 6, ''), (12, 6, ''),
                      (13, 6, ''), (14, 6, ''), (15, 6, ''), (16, 6, '') ]
    test_route_no_stops = Route(route_no_stops)
    result = test_route_no_stops.timetable()
    assert result == {} 

## Tests for Journey class 
    
    