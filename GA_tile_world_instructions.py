"""
GNP Judgement and Processing Node Functions for Tile World Evolutionary Process.
These functions are used as nodes in the GNP network structure.
"""

# ============================================================================
# IMPORTS
# ============================================================================

import GA_common_instructions as comins
import variables


# ============================================================================
# CONFIGURATION
# ============================================================================

number_of_rows = variables.number_of_rows
table_size = variables.table_size
movement_speed = variables.movement_speed
obstacles_index = variables.obstacles_index


# ============================================================================
# JUDGEMENT NODE FUNCTIONS
# ============================================================================
# These functions are used as judgement nodes in the GNP network.
# They return values that determine which connection gene to follow.

def what_exists_front(agent, agents, tiles, holes):
    """
    Check what exists in front of the agent (CF - Check Front).
    
    Returns:
        0: agent exists
        1: tile exists
        2: hole exists
        3: nothing exists
    """
    front_square_index = comins.get_front_square_index(agent)
    if not front_square_index:
        return 3
    
    for age in agents:
        if front_square_index == age.index:
            return 0  # agent
    for tile in tiles:
        if front_square_index == tile.index:
            return 1  # tile
    for hole in holes:
        if front_square_index == hole.index:
            return 2  # hole
    return 3  # if nothing exist


def what_exists_right(agent, agents, tiles, holes):
    """
    Check what exists to the right of the agent (CR - Check Right).
    
    Returns:
        0: agent exists
        1: tile exists
        2: hole exists
        3: nothing exists
    """
    right_square_index = comins.get_right_square_index(agent)
    if not right_square_index:
        return 3
    
    for age in agents:
        if right_square_index == age.index:
            return 0  # agent
    for tile in tiles:
        if right_square_index == tile.index:
            return 1  # tile
    for hole in holes:
        if right_square_index == hole.index:
            return 2  # hole
    return 3  # if nothing exist


def what_exists_left(agent, agents, tiles, holes):
    """
    Check what exists to the left of the agent (CL - Check Left).
    
    Returns:
        0: agent exists
        1: tile exists
        2: hole exists
        3: nothing exists
    """
    left_square_index = comins.get_left_square_index(agent)
    if not left_square_index:
        return 3
    
    for age in agents:
        if left_square_index == age.index:
            return 0  # agent
    for tile in tiles:
        if left_square_index == tile.index:
            return 1  # tile
    for hole in holes:
        if left_square_index == hole.index:
            return 2  # hole
    return 3  # if nothing exist


def what_exists_back(agent, agents, tiles, holes):
    """
    Check what exists behind the agent (CB - Check Back).
    
    Returns:
        0: agent exists
        1: tile exists
        2: hole exists
        3: nothing exists
    """
    back_square_index = comins.get_back_square_index(agent)
    if not back_square_index:
        return 3
    
    for age in agents:
        if back_square_index == age.index:
            return 0  # agent
    for tile in tiles:
        if back_square_index == tile.index:
            return 1  # tile
    for hole in holes:
        if back_square_index == hole.index:
            return 2  # hole
    return 3  # if nothing exist


# ============================================================================
# DIRECTION FINDING FUNCTIONS
# ============================================================================

def find_direction(agent, obj):
    """
    Calculate the direction from agent to object and return which direction
    the agent should choose to arrive at the object.
    
    Return values:
        0: forward
        1: right
        2: left
        3: backward
    
    Note: FIXME - when agent and object are in same index it returns None
    """
    x_distance = obj.index[0] - agent.index[0]
    y_distance = obj.index[1] - agent.index[1]
    
    if agent.heading() == 0:  # East
        if abs(x_distance) >= abs(y_distance):
            if x_distance > 0:
                return 0  # forward
            if x_distance < 0:
                return 3  # backward
        else:
            if y_distance > 0:
                return 2  # left
            if y_distance < 0:
                return 1  # right
    
    if agent.heading() == 90:  # North
        if abs(x_distance) > abs(y_distance):
            if x_distance > 0:
                return 1  # right
            if x_distance < 0:
                return 2  # left
        else:
            if y_distance > 0:
                return 0  # forward
            if y_distance < 0:
                return 3  # backward
    
    if agent.heading() == 180:  # West
        if abs(x_distance) >= abs(y_distance):
            if x_distance > 0:
                return 3  # backward
            if x_distance < 0:
                return 1  # forward
        else:
            if y_distance > 0:
                return 1  # right
            if y_distance < 0:
                return 2  # left
    
    if agent.heading() == 270:  # South
        if abs(x_distance) > abs(y_distance):
            if x_distance > 0:
                return 2  # left
            if x_distance < 0:
                return 1  # right
        else:
            if y_distance > 0:
                return 3  # backward
            if y_distance < 0:
                return 0  # forward


def nearest_tile_direction(agent, not_use1, tiles, not_use2):
    """
    Find the direction to the nearest tile (NTD - Nearest Tile Direction).
    
    Returns:
        0: forward
        1: right
        2: left
        3: backward
    """
    distances = []
    for tile in tiles:
        distances.append(comins.distance_between(agent, tile))
    return find_direction(agent, tiles[distances.index(min(distances))])


def second_nearest_tile_direction(agent, not_use1, tiles, not_use2):
    """
    Find the direction to the second nearest tile (SNT - Second Nearest Tile).
    
    Returns:
        0: forward
        1: right
        2: left
        3: backward
    """
    distances = []
    for tile in tiles:
        distances.append(comins.distance_between(agent, tile))
    distances_forsort = distances.copy()
    distances_forsort.sort()
    return find_direction(agent, tiles[distances.index(distances_forsort[1])])


def nearest_hole_direction(agent, not_use1, not_use2, holes):
    """
    Find the direction to the nearest hole (NHD - Nearest Hole Direction).
    
    Returns:
        0: forward
        1: right
        2: left
        3: backward
    """
    distances = []
    for hole in holes:
        distances.append(comins.distance_between(agent, hole))
    return find_direction(agent, holes[distances.index(min(distances))])


# ============================================================================
# PROCESSING NODE FUNCTIONS
# ============================================================================
# These functions are used as processing nodes in the GNP network.
# They perform actions that modify the simulation state.

def check_outting(index):
    """Check if agent or tile is going out of bounds from the table."""
    if index[0] > number_of_rows or index[0] < 1 or index[1] > number_of_rows or index[1] < 1:
        return True
    return False


def check_overlapping(agent, agents, tiles, holes):
    """
    Check if elements would overlap (except overlapping between tiles and holes).
    
    Returns:
        False: no overlap, movement is allowed
        True: overlap detected (obstacle, agent, or hole)
        tuple (tile, hole, False): tile can be pushed into hole
        tuple (tile, tile2, True): two tiles would overlap
        tile object: single tile can be pushed
    """
    front_square_index = comins.get_front_square_index(agent)
    if not front_square_index:
        return True
    
    # Check obstacles
    for obstacle_index in obstacles_index:
        if obstacle_index == front_square_index:
            return True
    
    # Check agents
    for age in agents:
        if age.index == front_square_index:
            return True
    
    # Check holes
    for hole in holes:
        if hole.index == front_square_index:
            return True
    
    # Check tiles (can be pushed)
    for tile in tiles:
        if tile.index == front_square_index:
            tile.setheading(agent.heading())
            while tile.heading() != agent.heading():  # because it takes time
                tile.setheading(agent.heading())
            
            tile_front = comins.get_front_square_index(tile)
            if not tile_front or check_outting(tile_front):
                return True
            
            # Check if tile would push into another tile
            for t in tiles:
                if tile_front == t.index:
                    t.setheading(tile.heading())
                    while t.heading() != tile.heading():  # because it takes time
                        t.setheading(tile.heading())
                    return tile, t, True
            
            # Check if tile would be pushed into a hole
            for hole in holes:
                if tile_front == hole.index:
                    return tile, hole, False
            
            # Check if tile would push into an agent
            for agent in agents:
                if tile_front == agent.index:
                    return True
            
            # Check if tile would push into an obstacle
            for obstacle_index in obstacles_index:
                if tile_front == obstacle_index:
                    return True
            
            # Tile can be pushed
            return tile
    
    return False


def move_forward(agent, agents, tiles, holes):
    """
    Move the agent forward one square (MF - Move Forward).
    Handles tile pushing and collision detection.
    """
    candidate_index = comins.get_front_square_index(agent)
    if not candidate_index or check_outting(candidate_index):
        return
    
    overlap_result = check_overlapping(agent, agents, tiles, holes)
    
    if overlap_result == False:
        # No overlap, move agent
        agent.index = candidate_index
    
    elif type(overlap_result) == type(()) and not overlap_result[2]:
        # Tile can be pushed into hole
        tile, hole, not_use = overlap_result
        tile.index = comins.get_front_square_index(tile)
        agent.index = candidate_index
    
    elif type(overlap_result) == type(()) and overlap_result[2]:
        # Two tiles would overlap, try to push the first tile
        tile, tile2, not_use = overlap_result
        if not check_overlapping(tile, agents, tiles, holes):
            move_forward(tile, agents, tiles, holes)
            agent.index = candidate_index
    
    elif type(overlap_result) == type(agent):
        # Single tile can be pushed
        tile = overlap_result
        tile.index = comins.get_front_square_index(tile)
        agent.index = candidate_index


def turn_right(agent, not_use1, not_use2, not_use3):
    """
    Turn the agent right (clockwise) by 90 degrees (TR - Turn Right).
    """
    agent.setheading(agent.heading() - 90)
    if agent.heading() < 0:
        agent.setheading(agent.heading() + 360)


def turn_left(agent, not_use1, not_use2, not_use3):
    """
    Turn the agent left (counter-clockwise) by 90 degrees (TL - Turn Left).
    """
    agent.setheading(agent.heading() + 90)
    if agent.heading() >= 360:
        agent.setheading(agent.heading() - 360)


def stay(not_use1, not_use2, not_use3, not_use4):
    """
    Agent stays in place (ST - Stay).
    No action is performed.
    """
    pass
