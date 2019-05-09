#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 31 19:49:06 2018

@author: iswariya
"""
import copy
import math
import random


def plot_cost_function(cost):
    """ Function to plot the no. of iterations (x-axis) vs
    cost (y-axis). X-axis of the plot should contain xticks
    from 0 to 10000 in steps of 2000.
    Use matplotlib.pyplot to generate the plot as .png file and store it
    in the results folder. An example plot is
    there in the results folder.

    Parameters
    ----------
    cost : [type]
        [description]
    """

    raise NotImplementedError


def get_successors(curr_seq):
    """ Function to generate a list of 100 random successor sequences
    by swapping any cities. Please note that the first and last city
    should remain unchanged since the traveller starts and ends in
    the same city.

    Parameters
    ----------
    curr_seq : [type]
        [description]

    Returns
    -------
    [type]
        [description]
    """

    raise NotImplementedError


def get_distance(distance_matrix, seq):
    """ Function to get the distance while travelling along
    a particular sequence of cities.
    HINT : Keep adding the distances between the cities in the
    sequence by referring the distances from the distance matrix

    Parameters
    ----------
    distance_matrix : [type]
        [description]
    seq : [type]
        [description]

    Returns
    -------
    [type]
        [description]
    """

    raise NotImplementedError


def get_distance_matrix(coordinates):
    """ Function to generate a distance matrix. The distance matrix
    is a square matrix.
    For eg: If there are 3 cities then the distance
    matrix has 3 rows and 3 colums, with each city representing a row
    and a column. Each element of the matrix represents the euclidean
    distance between the coordinates of the cities. Thus, the diagonal
    elements will be zero (because it is the distance between the same city).

    Parameters
    ----------
    coordinates : [type]
        [description]

    Returns
    -------
    [type]
        [description]
    """

    raise NotImplementedError
