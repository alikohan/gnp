"""
Common Instructions between Fitness Function and Tile World Agents' Functions for Visualization.
Utility functions for tile world simulation including distance calculations,
coordinate conversions, and directional index calculations.
"""

# ============================================================================
# IMPORTS
# ============================================================================

import math
import time
import variables


# ============================================================================
# CONFIGURATION
# ============================================================================

number_of_rows = variables.number_of_rows
table_size = variables.table_size


# ============================================================================
# DISTANCE CALCULATIONS
# ============================================================================

def distance_between(first, second):
    """Calculate Euclidean distance between two objects based on their indices."""
    return math.sqrt(abs(first.index[0] - second.index[0]) ** 2 + abs(first.index[1] - second.index[1]) ** 2)


# ============================================================================
# COORDINATE CONVERSION
# ============================================================================

def get_position_with_index(index, mode='turtle'):
    """
    Convert grid index to screen coordinates.
    
    Args:
        index: Grid index [row, col]
        mode: Coordinate system mode ('turtle' or 'tkinter')
             because coordinates in 'turtle' module is different from coordinates in 'tkinter' module
    
    Returns:
        List of [x, y] coordinates
    """
    coordinates = [0, 0]
    center = number_of_rows // 2 + 1

    coordinates[0] = (index[0] - center) * table_size * 2  # x coordinate
    coordinates[1] = (index[1] - center) * table_size * 2  # y coordinate

    if mode == 'tkinter':
        coordinates[1] = -coordinates[1]

    return coordinates


# ============================================================================
# DIRECTIONAL INDEX CALCULATIONS
# ============================================================================

def get_front_square_index(object):
    """
    Get the grid index of the square in front of the object.
    
    Heading directions:
        0   = East (right)
        90  = North (up)
        180 = West (left)
        270 = South (down)
    """
    front_square_index = []
    if object.heading() == 0:
        front_square_index = [object.index[0] + 1, object.index[1]]
    elif object.heading() == 90:
        front_square_index = [object.index[0], object.index[1] + 1]
    elif object.heading() == 180:
        front_square_index = [object.index[0] - 1, object.index[1]]
    elif object.heading() == 270:
        front_square_index = [object.index[0], object.index[1] - 1]
    else:
        time.sleep(0.1)
    return front_square_index


def get_right_square_index(object):
    """
    Get the grid index of the square to the right of the object.
    
    Heading directions:
        0   = East (right)
        90  = North (up)
        180 = West (left)
        270 = South (down)
    """
    right_square_index = []
    if object.heading() == 0:
        right_square_index = [object.index[0], object.index[1] - 1]
    elif object.heading() == 90:
        right_square_index = [object.index[0] + 1, object.index[1]]
    elif object.heading() == 180:
        right_square_index = [object.index[0], object.index[1] + 1]
    elif object.heading() == 270:
        right_square_index = [object.index[0] - 1, object.index[1]]
    else:
        time.sleep(0.1)
    return right_square_index


def get_left_square_index(object):
    """
    Get the grid index of the square to the left of the object.
    
    Heading directions:
        0   = East (right)
        90  = North (up)
        180 = West (left)
        270 = South (down)
    """
    left_square_index = []
    if object.heading() == 0:
        left_square_index = [object.index[0], object.index[1] + 1]
    elif object.heading() == 90:
        left_square_index = [object.index[0] - 1, object.index[1]]
    elif object.heading() == 180:
        left_square_index = [object.index[0], object.index[1] - 1]
    elif object.heading() == 270:
        left_square_index = [object.index[0] + 1, object.index[1]]
    else:
        time.sleep(0.1)
    return left_square_index


def get_back_square_index(object):
    """
    Get the grid index of the square behind the object.
    
    Heading directions:
        0   = East (right)
        90  = North (up)
        180 = West (left)
        270 = South (down)
    """
    back_square_index = []
    if object.heading() == 0:
        back_square_index = [object.index[0] - 1, object.index[1]]
    elif object.heading() == 90:
        back_square_index = [object.index[0], object.index[1] - 1]
    elif object.heading() == 180:
        back_square_index = [object.index[0] + 1, object.index[1]]
    elif object.heading() == 270:
        back_square_index = [object.index[0], object.index[1] + 1]
    else:
        time.sleep(0.1)
    return back_square_index
