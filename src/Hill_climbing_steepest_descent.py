#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 31 11:04:22 2018

@author: iswariya
"""
import argparse
import os
import random
import timeit

from helper import *


def hill_climb_steepest_descent(start_seq, distance_matrix):
    """ Function to implement steepest descent hill climbing algorithm
    for the travelling salesman problem.
    Run the hill climbing algorithm for 10000 iterations and
    print the results for every 2000 iterations.
    Please use the functions in helper.py to complete the algorithm.
    Please do not clutter the code this file by adding extra functions.
    Additional functions if required should be added in helper.py

    Parameters
    ----------
    start_seq : [type]
        [description]
    distance_matrix : [type]
        [description]

    Returns
    -------
    [type]
    """

    best_cost = float('inf')
    best_seq = None
    cost = [0]
    seen_states = []
    curr_seq = start_seq
    curr_seq.append(start_seq[0])
    curr_dist = 0
    restarts_count = 0

    # FILL IN YOUR CODE HERE

    return best_cost, best_seq


if __name__ == '__main__':

    # Reading txt file from command line
    parser = argparse.ArgumentParser()
    parser.add_argument('--filename', type=str)
    args = parser.parse_args()
    file_path = os.path.join(os.getcwd(), args.filename)
    with open(file_path) as file:
        data = file.readlines()

    # Getting the list of cities and their coordinates
    list_of_cities = [i.strip().split(',') for i in data]
    city_names = [row[0] for row in list_of_cities[1:]]
    coordinates = [[row[1], row[2]] for row in list_of_cities[1:]]

    # Generating a random soln.
    random_seq = random.sample(range(0, len(list_of_cities[1:])),
                               len(list_of_cities[1:]))

    # Calculating the least dist using steepest descent hill climbing
    start_time = timeit.default_timer()
    least_distance, best_seq = hill_climb_steepest_descent(random_seq,
                                                           coordinates)
    end_time = timeit.default_timer()

    print("Best Sequence:", best_seq)
    print("Least distance from Steepest Ascent:", least_distance)
    print("Time: {}s".format(end_time-start_time))
