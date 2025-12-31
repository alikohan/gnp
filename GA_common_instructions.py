"""
Common Instructions between Fitness Function and Tile World Agents' Functions for Evolutionary Process.
Utility functions for genetic algorithm operations in tile world simulation,
including distance calculations, coordinate conversions, and directional index calculations
"""

# ============================================================================
# IMPORTS
# ============================================================================

import math
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
    
    Returns:
        List [row, col] if valid heading, False otherwise
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
        return False
    return front_square_index


def get_right_square_index(object):
    """
    Get the grid index of the square to the right of the object.
    
    Heading directions:
        0   = East (right)
        90  = North (up)
        180 = West (left)
        270 = South (down)
    
    Returns:
        List [row, col] if valid heading, False otherwise
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
        return False
    return right_square_index


def get_left_square_index(object):
    """
    Get the grid index of the square to the left of the object.
    
    Heading directions:
        0   = East (right)
        90  = North (up)
        180 = West (left)
        270 = South (down)
    
    Returns:
        List [row, col] if valid heading, False otherwise
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
        return False
    return left_square_index


def get_back_square_index(object):
    """
    Get the grid index of the square behind the object.
    
    Heading directions:
        0   = East (right)
        90  = North (up)
        180 = West (left)
        270 = South (down)
    
    Returns:
        List [row, col] if valid heading, False otherwise
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
        return False
    return back_square_index
