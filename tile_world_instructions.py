"""
GNP Judgement and Processing Node Functions for Tile World Visualization.
These functions are used as nodes in the GNP network structure.
"""

# ============================================================================
# IMPORTS
# ============================================================================

import common_instructions as comins
import variables


# ============================================================================
# CONFIGURATION
# ============================================================================

number_of_rows = variables.number_of_rows
table_size = variables.table_size
movement_speed = variables.movement_speed
obstacles_index = variables.obstacles_index
initial_tiles_index = variables.initial_tiles_index
initial_holes_index = variables.initial_holes_index


# ============================================================================
# JUDGEMENT NODE FUNCTIONS
# These functions are used as judgement nodes in the GNP network.
# They return an integer representing the outcome, which dictates the next node.
# Return values: 0=agent, 1=tile, 2=hole, 3=nothing
# ============================================================================

def what_exists_front(agent, agents, tiles, holes):
    """
    Checks what exists in the square directly in front of the agent.

    Args:
        agent (object_head): The agent object.
        agents (list): List of all agent objects.
        tiles (list): List of all tile objects.
        holes (list): List of all hole objects.

    Returns:
        int: 0 if an agent, 1 if a tile, 2 if a hole, 3 if nothing exists.
    """
    front_square_index = comins.get_front_square_index(agent)
    for age in agents:
        if front_square_index == age.index:
            return 0 # agent
    for tile in tiles:
        if front_square_index == tile.index:
            return 1 # tile
    for hole in holes:
        if front_square_index == hole.index:
            return 2 # hole
    return 3 # if nothing exist


def what_exists_right(agent, agents, tiles, holes):
    """
    Checks what exists in the square directly to the right of the agent.

    Args:
        agent (object_head): The agent object.
        agents (list): List of all agent objects.
        tiles (list): List of all tile objects.
        holes (list): List of all hole objects.

    Returns:
        int: 0 if an agent, 1 if a tile, 2 if a hole, 3 if nothing exists.
    """
    right_square_index = comins.get_right_square_index(agent)
    for age in agents:
        if right_square_index == age.index:
            return 0 # agent
    for tile in tiles:
        if right_square_index == tile.index:
            return 1 # tile
    for hole in holes:
        if right_square_index == hole.index:
            return 2 # hole
    return 3 # if nothing exist


def what_exists_left(agent, agents, tiles, holes):
    """
    Checks what exists in the square directly to the left of the agent.

    Args:
        agent (object_head): The agent object.
        agents (list): List of all agent objects.
        tiles (list): List of all tile objects.
        holes (list): List of all hole objects.

    Returns:
        int: 0 if an agent, 1 if a tile, 2 if a hole, 3 if nothing exists.
    """
    left_square_index = comins.get_left_square_index(agent)
    for age in agents:
        if left_square_index == age.index:
            return 0 # agent
    for tile in tiles:
        if left_square_index == tile.index:
            return 1 # tile
    for hole in holes:
        if left_square_index == hole.index:
            return 2 # hole
    return 3 # if nothing exist


def what_exists_back(agent, agents, tiles, holes):
    """
    Checks what exists in the square directly behind the agent.

    Args:
        agent (object_head): The agent object.
        agents (list): List of all agent objects.
        tiles (list): List of all tile objects.
        holes (list): List of all hole objects.

    Returns:
        int: 0 if an agent, 1 if a tile, 2 if a hole, 3 if nothing exists.
    """
    back_square_index = comins.get_back_square_index(agent)
    for age in agents:
        if back_square_index == age.index:
            return 0 # agent
    for tile in tiles:
        if back_square_index == tile.index:
            return 1 # tile
    for hole in holes:
        if back_square_index == hole.index:
            return 2 # hole
    return 3 # if nothing exist


# ============================================================================
# DIRECTION FINDING FUNCTIONS
# ============================================================================

def find_direction(agent, obj):
    """
    Calculate the relative position of an object compared to the agent
    and return which direction the agent should choose to move toward the object.
    
    Args:
        agent (object_head): The agent object with heading and index.
        obj (object_head): The target object with index.
    
    Returns:
        int: Direction code - 0=forward, 1=right, 2=left, 3=backward
    """
    x_distance = obj.index[0] - agent.index[0]
    y_distance = obj.index[1] - agent.index[1]
    
    # Heading: 0=East, 90=North, 180=West, 270=South
    if agent.heading() == 0:  # Facing East
        if abs(x_distance) >= abs(y_distance):
            if x_distance > 0:
                return 0 # forward
            if x_distance < 0:
                return 3 # backward    
        else:
            if y_distance > 0:
                return 2 # left
            if y_distance < 0:
                return 1 # right
    
    if agent.heading() == 90:  # Facing North
        if abs(x_distance) > abs(y_distance):
            if x_distance > 0:
                return 1 # right
            if x_distance < 0:
                return 2 # left    
        else:
            if y_distance > 0:
                return 0 # forward
            if y_distance < 0:
                return 3 # backward
    
    if agent.heading() == 180:  # Facing West
        if abs(x_distance) >= abs(y_distance):
            if x_distance > 0:
                return 3 # backward
            if x_distance < 0:
                return 1 # forward
        else:
            if y_distance > 0:
                return 1 # right
            if y_distance < 0:
                return 2 # left
    
    if agent.heading() == 270:  # Facing South
        if abs(x_distance) > abs(y_distance):
            if x_distance > 0:
                return 2 # left
            if x_distance < 0:
                return 1 # right
        else:
            if y_distance > 0:
                return 3 # backward
            if y_distance < 0:
                return 0 # forward


def nearest_tile_direction(agent, not_use1, tiles, not_use2):
    """
    Find the direction toward the nearest tile relative to the agent.

    Args:
        agent (object_head): The agent object.
        not_use1: Unused parameter (for compatibility with GNP node structure).
        tiles (list): List of all tile objects.
        not_use2: Unused parameter (for compatibility with GNP node structure).

    Returns:
        int: Direction code - 0=forward, 1=right, 2=left, 3=backward
    """
    distances = []
    for tile in tiles:
        distances.append(comins.distance_between(agent, tile))
    return find_direction(agent, tiles[distances.index(min(distances))])


def second_nearest_tile_direction(agent, not_use1, tiles, not_use2):
    """
    Find the direction toward the second nearest tile relative to the agent.

    Args:
        agent (object_head): The agent object.
        not_use1: Unused parameter (for compatibility with GNP node structure).
        tiles (list): List of all tile objects.
        not_use2: Unused parameter (for compatibility with GNP node structure).

    Returns:
        int: Direction code - 0=forward, 1=right, 2=left, 3=backward
    """
    distances = []
    for tile in tiles:
        distances.append(comins.distance_between(agent, tile))
    distances_forsort = distances.copy()
    distances_forsort.sort()
    return find_direction(agent, tiles[distances.index(distances_forsort[1])])


def nearest_hole_direction(agent, not_use1, not_use2, holes):
    """
    Find the direction toward the nearest hole relative to the agent.

    Args:
        agent (object_head): The agent object.
        not_use1: Unused parameter (for compatibility with GNP node structure).
        not_use2: Unused parameter (for compatibility with GNP node structure).
        holes (list): List of all hole objects.

    Returns:
        int: Direction code - 0=forward, 1=right, 2=left, 3=backward
    """
    distances = []
    for hole in holes:
        distances.append(comins.distance_between(agent, hole))
    return find_direction(agent, holes[distances.index(min(distances))])


# ============================================================================
# PROCESSING NODE FUNCTIONS
# These functions are used as processing nodes in the GNP network.
# They perform actions that modify the simulation state.
# ============================================================================

def move_forward(agent, agents, tiles, holes):
    """
    Move the agent forward one square, handling tile pushing and collision detection.

    Args:
        agent (object_head): The agent to move.
        agents (list): List of all agent objects.
        tiles (list): List of all tile objects.
        holes (list): List of all hole objects.
    """
    candidate_index = comins.get_front_square_index(agent)
    
    # Check if movement would go out of bounds
    if check_outting(candidate_index):
        return
    
    # Check for overlapping
    overlap_result = check_overlapping(agent, agents, tiles, holes)
    
    # No overlap - simple movement
    if overlap_result == False:
        agent.index = candidate_index
        agent.goto(comins.get_position_with_index(agent.index))
    
    # Tile pushed into hole
    elif type(overlap_result) == type(()) and not overlap_result[2]:
        tile, hole, not_use = overlap_result
        tile.index = comins.get_front_square_index(tile)
        tile.goto(comins.get_position_with_index(tile.index))
        tile.color("green")  # Mark tile as dropped
        agent.index = candidate_index
        agent.goto(comins.get_position_with_index(agent.index))
    
    # Tile pushed into another tile (chain push)
    elif type(overlap_result) == type(()) and overlap_result[2]:
        tile, tile2, not_use = overlap_result
        if not check_overlapping(tile, agents, tiles, holes) == True:
            move_forward(tile, agents, tiles, holes)  # Recursively push the tile
            agent.index = candidate_index
            agent.goto(comins.get_position_with_index(agent.index))
    
    # Single tile push
    elif type(overlap_result) == type(agent):
        tile = overlap_result
        tile.index = comins.get_front_square_index(tile)
        tile.goto(comins.get_position_with_index(tile.index))
        agent.index = candidate_index
        agent.goto(comins.get_position_with_index(agent.index))


def turn_right(agent, not_use1, not_use2, not_use3):
    """
    Turn the agent 90 degrees to the right.

    Args:
        agent (object_head): The agent to turn.
        not_use1: Unused parameter (for compatibility with GNP node structure).
        not_use2: Unused parameter (for compatibility with GNP node structure).
        not_use3: Unused parameter (for compatibility with GNP node structure).
    """
    agent.right(90)


def turn_left(agent, not_use1, not_use2, not_use3):
    """
    Turn the agent 90 degrees to the left.

    Args:
        agent (object_head): The agent to turn.
        not_use1: Unused parameter (for compatibility with GNP node structure).
        not_use2: Unused parameter (for compatibility with GNP node structure).
        not_use3: Unused parameter (for compatibility with GNP node structure).
    """
    agent.left(90)


def stay(not_use1, not_use2, not_use3, not_use4):
    """
    Do nothing (agent stays in place).

    Args:
        not_use1: Unused parameter (for compatibility with GNP node structure).
        not_use2: Unused parameter (for compatibility with GNP node structure).
        not_use3: Unused parameter (for compatibility with GNP node structure).
        not_use4: Unused parameter (for compatibility with GNP node structure).
    """
    pass


# ============================================================================
# UTILITY FUNCTIONS
# These functions are used to check if the agent or tile would go outside the table boundaries,
# or if there is overlapping with obstacles, agents, holes, or tiles (used in move_forward function).
# ============================================================================

def check_outting(index):
    """
    Check if an agent or tile would go outside the table boundaries.

    Args:
        index (list): The [x, y] index to check.

    Returns:
        bool: True if the index is outside the table boundaries, False otherwise.
    """
    if index[0] > number_of_rows or index[0] < 1 or index[1] > number_of_rows or index[1] < 1:
        return True
    return False


def check_overlapping(agent, agents, tiles, holes):
    """
    Check if moving forward would cause overlapping with obstacles, agents, holes, or tiles.
    Also handles tile pushing logic when an agent moves into a tile.

    Args:
        agent (object_head): The agent attempting to move.
        agents (list): List of all agent objects.
        tiles (list): List of all tile objects.
        holes (list): List of all hole objects.

    Returns:
        Various return types:
        - False: No overlap, movement is allowed
        - True: Overlap detected (obstacle, agent, or hole), movement blocked
        - tuple (tile, hole, False): Tile can be pushed into a hole
        - tuple (tile, tile2, True): Tile can be pushed into another tile
        - tile object: Tile can be pushed forward (single tile push)
    """
    front_square_index = comins.get_front_square_index(agent)
    
    # Check for obstacles
    for obstacle_index in obstacles_index:
        if obstacle_index == front_square_index:
            return True
    
    # Check for other agents
    for age in agents:
        if age.index == front_square_index:
            return True
    
    # Check for holes
    for hole in holes:
        if hole.index == front_square_index:
            return True
    
    # Check for tiles (with pushing logic)
    for tile in tiles:
        if tile.index == front_square_index:
            # Align tile heading with agent heading
            tile.setheading(agent.heading())
            while tile.heading() != agent.heading(): # because it takes time
                tile.setheading(agent.heading())
            
            # Check if pushing tile would go out of bounds
            if check_outting(comins.get_front_square_index(tile)) == True:
                return True
            
            # Check if pushing tile would hit another tile
            for t in tiles:
                if comins.get_front_square_index(tile) == t.index:
                    t.setheading(tile.heading())
                    while t.heading() != tile.heading(): # because it takes time
                        t.setheading(tile.heading())
                    return tile, t, True
            
            # Check if pushing tile would hit a hole
            for hole in holes:
                if comins.get_front_square_index(tile) == hole.index:
                    return tile, hole, False
            
            # Check if pushing tile would hit an agent
            for agent in agents:
                if comins.get_front_square_index(tile) == agent.index:
                    return True
            
            # Check if pushing tile would hit an obstacle
            for obstacle_index in obstacles_index:
                if comins.get_front_square_index(tile) == obstacle_index:
                    return True
            
            # Tile can be pushed forward
            return tile
    
    return False