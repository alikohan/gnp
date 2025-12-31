"""
Visualization module for GNP-based tile world simulation.
Provides GUI visualization using turtle graphics and tkinter.
"""

# ============================================================================
# IMPORTS
# ============================================================================

# Standard library
import threading
import time
import tkinter as tk
import turtle

# Local modules
import common_instructions as comins
import tile_world_instructions as tileins
import variables


# ============================================================================
# CONSTANTS
# ============================================================================

# Visualization constants
COLOR_BG = 'white'
LINE_WIDTH = 5
DISTANCE_TABLE_TO_OUTSIDE_RECTANGLE = LINE_WIDTH / 2

# Configuration from variables module
NUMBER_OF_ROWS = variables.number_of_rows
TABLE_SIZE = variables.table_size
MOVEMENT_SPEED = variables.movement_speed
DELAY_TIME = variables.delay_time
EACH_STEP_ACCORDING_TO_DI = variables.each_step_according_to_di

# Initial state indices
OBSTACLES_INDEX = variables.obstacles_index
INITIAL_TILES_INDEX = variables.initial_tiles_index
INITIAL_HOLES_INDEX = variables.initial_holes_index
INITIAL_AGENTS_INDEX = variables.initial_agents_index
INITIAL_REMAINING_STEP = variables.initial_remaining_step


# ============================================================================
# DATA STRUCTURES
# ============================================================================

# Base individual structure with PG=5
# Nodes 2-36: judgement nodes
# Nodes 37-56: processing nodes
BASE_INDIVIDUAL = [
    [],
    [0, 0, 0],
    [1, tileins.what_exists_front, 1],
    [1, tileins.what_exists_right, 1],
    [1, tileins.what_exists_left, 1],
    [1, tileins.what_exists_back, 1],
    [1, tileins.nearest_tile_direction, 1],
    [1, tileins.second_nearest_tile_direction, 1],
    [1, tileins.nearest_hole_direction, 1],
    [1, tileins.what_exists_front, 1],
    [1, tileins.what_exists_right, 1],
    [1, tileins.what_exists_left, 1],
    [1, tileins.what_exists_back, 1],
    [1, tileins.nearest_tile_direction, 1],
    [1, tileins.second_nearest_tile_direction, 1],
    [1, tileins.nearest_hole_direction, 1],
    [1, tileins.what_exists_front, 1],
    [1, tileins.what_exists_right, 1],
    [1, tileins.what_exists_left, 1],
    [1, tileins.what_exists_back, 1],
    [1, tileins.nearest_tile_direction, 1],
    [1, tileins.second_nearest_tile_direction, 1],
    [1, tileins.nearest_hole_direction, 1],
    [1, tileins.what_exists_front, 1],
    [1, tileins.what_exists_right, 1],
    [1, tileins.what_exists_left, 1],
    [1, tileins.what_exists_back, 1],
    [1, tileins.nearest_tile_direction, 1],
    [1, tileins.second_nearest_tile_direction, 1],
    [1, tileins.nearest_hole_direction, 1],
    [1, tileins.what_exists_front, 1],
    [1, tileins.what_exists_right, 1],
    [1, tileins.what_exists_left, 1],
    [1, tileins.what_exists_back, 1],
    [1, tileins.nearest_tile_direction, 1],
    [1, tileins.second_nearest_tile_direction, 1],
    [1, tileins.nearest_hole_direction, 1],
    [2, tileins.move_forward, 5],
    [2, tileins.turn_right, 5],
    [2, tileins.turn_left, 5],
    [2, tileins.stay, 5],
    [2, tileins.move_forward, 5],
    [2, tileins.turn_right, 5],
    [2, tileins.turn_left, 5],
    [2, tileins.stay, 5],
    [2, tileins.move_forward, 5],
    [2, tileins.turn_right, 5],
    [2, tileins.turn_left, 5],
    [2, tileins.stay, 5],
    [2, tileins.move_forward, 5],
    [2, tileins.turn_right, 5],
    [2, tileins.turn_left, 5],
    [2, tileins.stay, 5],
    [2, tileins.move_forward, 5],
    [2, tileins.turn_right, 5],
    [2, tileins.turn_left, 5],
    [2, tileins.stay, 5]
]

# Result individual (evolved solution)
RESULT_INDIVIDUAL = [
    [], 
    [0, 0, 0, 54, 0], 
    [1, "function what_exists_front at 0x7f8b2bffe3b0", 1, 52, 0, 42, 0, 55, 0, 55, 0],
    [1, "function what_exists_right at 0x7f8b2bffe950", 1, 52, 0, 55, 0, 47, 0, 48, 0],
    [1, "function what_exists_left at 0x7f8b2bffe9e0", 1, 40, 0, 56, 0, 41, 0, 51, 0],
    [1, "function what_exists_back at 0x7f8b2bffea70", 1, 49, 0, 45, 0, 55, 0, 43, 0],
    [1, "function nearest_tile_direction at 0x7f8b2bffeb90", 1, 39, 0, 48, 0, 45, 0, 56, 0],
    [1, "function second_nearest_tile_direction at 0x7f8b2bffec20", 1, 48, 0, 39, 0, 39, 0, 56, 0],
    [1, "function nearest_hole_direction at 0x7f8b2bffecb0", 1, 46, 0, 37, 0, 45, 0, 41, 0],
    [1, "function what_exists_front at 0x7f8b2bffe3b0", 1, 50, 0, 52, 0, 47, 0, 46, 0],
    [1, "function what_exists_right at 0x7f8b2bffe950", 1, 48, 0, 56, 0, 31, 0, 38, 0],
    [1, "function what_exists_left at 0x7f8b2bffe9e0", 1, 50, 0, 42, 0, 44, 0, 43, 0],
    [1, "function what_exists_back at 0x7f8b2bffea70", 1, 53, 0, 46, 0, 45, 0, 49, 0],
    [1, "function nearest_tile_direction at 0x7f8b2bffeb90", 1, 38, 0, 55, 0, 50, 0, 41, 0],
    [1, "function second_nearest_tile_direction at 0x7f8b2bffec20", 1, 51, 0, 41, 0, 50, 0, 54, 0],
    [1, "function nearest_hole_direction at 0x7f8b2bffecb0", 1, 56, 0, 55, 0, 43, 0, 54, 0],
    [1, "function what_exists_front at 0x7f8b2bffe3b0", 1, 39, 0, 50, 0, 48, 0, 29, 0],
    [1, "function what_exists_right at 0x7f8b2bffe950", 1, 40, 0, 50, 0, 52, 0, 49, 0],
    [1, "function what_exists_left at 0x7f8b2bffe9e0", 1, 45, 0, 55, 0, 44, 0, 46, 0],
    [1, "function what_exists_back at 0x7f8b2bffea70", 1, 47, 0, 40, 0, 39, 0, 50, 0],
    [1, "function nearest_tile_direction at 0x7f8b2bffeb90", 1, 54, 0, 42, 0, 46, 0, 41, 0],
    [1, "function second_nearest_tile_direction at 0x7f8b2bffec20", 1, 47, 0, 56, 0, 52, 0, 55, 0],
    [1, "function nearest_hole_direction at 0x7f8b2bffecb0", 1, 38, 0, 51, 0, 51, 0, 46, 0],
    [1, "function what_exists_front at 0x7f8b2bffe3b0", 1, 49, 0, 49, 0, 50, 0, 40, 0],
    [1, "function what_exists_right at 0x7f8b2bffe950", 1, 43, 0, 47, 0, 45, 0, 51, 0],
    [1, "function what_exists_left at 0x7f8b2bffe9e0", 1, 41, 0, 49, 0, 49, 0, 39, 0],
    [1, "function what_exists_back at 0x7f8b2bffea70", 1, 56, 0, 51, 0, 38, 0, 55, 0],
    [1, "function nearest_tile_direction at 0x7f8b2bffeb90", 1, 41, 0, 54, 0, 55, 0, 55, 0],
    [1, "function second_nearest_tile_direction at 0x7f8b2bffec20", 1, 52, 0, 46, 0, 39, 0, 44, 0],
    [1, "function nearest_hole_direction at 0x7f8b2bffecb0", 1, 52, 0, 55, 0, 40, 0, 13, 0],
    [1, "function what_exists_front at 0x7f8b2bffe3b0", 1, 52, 0, 50, 0, 49, 0, 45, 0],
    [1, "function what_exists_right at 0x7f8b2bffe950", 1, 55, 0, 44, 0, 54, 0, 41, 0],
    [1, "function what_exists_left at 0x7f8b2bffe9e0", 1, 53, 0, 45, 0, 37, 0, 48, 0],
    [1, "function what_exists_back at 0x7f8b2bffea70", 1, 43, 0, 53, 0, 42, 0, 55, 0],
    [1, "function nearest_tile_direction at 0x7f8b2bffeb90", 1, 38, 0, 50, 0, 43, 0, 39, 0],
    [1, "function second_nearest_tile_direction at 0x7f8b2bffec20", 1, 38, 0, 50, 0, 42, 0, 49, 0],
    [1, "function nearest_hole_direction at 0x7f8b2bffecb0", 1, 41, 0, 44, 0, 11, 0, 55, 0],
    [2, "function move_forward at 0x7f8b2bffee60", 5, 45, 0],
    [2, "function turn_right at 0x7f8b2bffeef0", 5, 41, 0],
    [2, "function turn_left at 0x7f8b2bffef80", 5, 27, 0],
    [2, "function stay at 0x7f8b2bfff010", 5, 52, 0],
    [2, "function move_forward at 0x7f8b2bffee60", 5, 15, 0],
    [2, "function turn_right at 0x7f8b2bffeef0", 5, 12, 0],
    [2, "function turn_left at 0x7f8b2bffef80", 5, 4, 0],
    [2, "function stay at 0x7f8b2bfff010", 5, 12, 0],
    [2, "function move_forward at 0x7f8b2bffee60", 5, 53, 0],
    [2, "function turn_right at 0x7f8b2bffeef0", 5, 42, 0],
    [2, "function turn_left at 0x7f8b2bffef80", 5, 23, 0],
    [2, "function stay at 0x7f8b2bfff010", 5, 15, 0],
    [2, "function move_forward at 0x7f8b2bffee60", 5, 8, 0],
    [2, "function turn_right at 0x7f8b2bffeef0", 5, 17, 0],
    [2, "function turn_left at 0x7f8b2bffef80", 5, 45, 0],
    [2, "function stay at 0x7f8b2bfff010", 5, 56, 0],
    [2, "function move_forward at 0x7f8b2bffee60", 5, 34, 0],
    [2, "function turn_right at 0x7f8b2bffeef0", 5, 34, 0],
    [2, "function turn_left at 0x7f8b2bffef80", 5, 45, 0],
    [2, "function stay at 0x7f8b2bfff010", 5, 3, 0]
]

# Base individual structure with PG=1
# Nodes 2-8: judgement nodes
# Nodes 9-12: processing nodes
# BASE_INDIVIDUAL = [
#     [], 
#     [0, 0, 0], 
#     [1, tileins.what_exists_front, 1], 
#     [1, tileins.what_exists_right, 1], 
#     [1, tileins.what_exists_left, 1], 
#     [1, tileins.what_exists_back, 1], 
#     [1, tileins.nearest_tile_direction, 1], 
#     [1, tileins.second_nearest_tile_direction, 1], 
#     [1, tileins.nearest_hole_direction, 1], 
#     [2, tileins.move_forward, 5], 
#     [2, tileins.turn_right, 5], 
#     [2, tileins.turn_left, 5], 
#     [2, tileins.stay, 5]
# ]

# Result individual (evolved solution)
# RESULT_INDIVIDUAL = [
#     [],
#     [0, 0, 0, 2, 0],
#     [1, tileins.what_exists_front, 1, 2, 0, 9, 0, 4, 0, 6, 0],
#     [1, tileins.what_exists_right, 1, 10, 0, 10, 0, 5, 0, 7, 0],
#     [1, tileins.what_exists_left, 1, 5, 0, 11, 0, 6, 0, 11, 0],
#     [1, tileins.what_exists_back, 1, 2, 0, 9, 0, 7, 0, 8, 0],
#     [1, tileins.nearest_tile_direction, 1, 9, 0, 10, 0, 11, 0, 10, 0],
#     [1, tileins.second_nearest_tile_direction, 1, 9, 0, 9, 0, 10, 0, 12, 0],
#     [1, tileins.nearest_hole_direction, 1, 2, 0, 3, 0, 6, 0, 12, 0],
#     [2, tileins.move_forward, 5, 11, 0],
#     [2, tileins.turn_right, 5, 6, 0],
#     [2, tileins.turn_left, 5, 2, 0],
#     [2, tileins.stay, 5, 4, 0]
# ]

# ============================================================================
# TABLE VISUALIZATION FUNCTIONS
# ============================================================================

def draw_table(canvas, size, number_of_rows):
    """
    Draw the game table/grid on the canvas.
    
    Args:
        canvas: Tkinter canvas object
        size: Size of the table
        number_of_rows: Number of rows in the table
    """
    # Draw outer border
    canvas.create_line(-size, -size, size, -size, width=LINE_WIDTH)
    canvas.create_line(-size, -size, -size, size, width=LINE_WIDTH)
    canvas.create_line(size, size, size, -size, width=LINE_WIDTH)
    canvas.create_line(size, size, -size, size, width=LINE_WIDTH)

    # Draw extended grid lines
    for row_num in range(3, number_of_rows + 1, 2):
        canvas.create_line(-size, -size, -size * row_num, -size, width=LINE_WIDTH)
        canvas.create_line(-size, -size, -size, -size * row_num, width=LINE_WIDTH)
        
        canvas.create_line(size, -size, size * row_num, -size, width=LINE_WIDTH)
        canvas.create_line(size, -size, size, -size * row_num, width=LINE_WIDTH)
        
        canvas.create_line(size, size, size * row_num, size, width=LINE_WIDTH)
        canvas.create_line(size, size, size, size * row_num, width=LINE_WIDTH)

        canvas.create_line(-size, size, -size * row_num, size, width=LINE_WIDTH)
        canvas.create_line(-size, size, -size, size * row_num, width=LINE_WIDTH)

        canvas.create_line(-size * row_num * 10, -size * row_num, 
                          size * row_num * 10, -size * row_num, width=LINE_WIDTH)
        canvas.create_line(-size * row_num, -size * row_num * 10, 
                          -size * row_num, size * row_num * 10, width=LINE_WIDTH)
        canvas.create_line(size * row_num, size * row_num * 10, 
                          size * row_num, -size * row_num * 10, width=LINE_WIDTH)
        canvas.create_line(size * row_num * 10, size * row_num, 
                          -size * row_num * 10, size * row_num, width=LINE_WIDTH)
    
    # Clear outside lines with background color
    canvas.create_rectangle(-size * number_of_rows * 10, -size * number_of_rows * 10,
                           size * number_of_rows * 10, -size * number_of_rows - DISTANCE_TABLE_TO_OUTSIDE_RECTANGLE,
                           fill=COLOR_BG, outline=COLOR_BG)
    canvas.create_rectangle(-size * number_of_rows * 10, -size * number_of_rows * 10,
                           -size * number_of_rows - DISTANCE_TABLE_TO_OUTSIDE_RECTANGLE, size * number_of_rows * 10,
                           fill=COLOR_BG, outline=COLOR_BG)
    canvas.create_rectangle(size * number_of_rows * 10, size * number_of_rows * 10,
                           size * number_of_rows + DISTANCE_TABLE_TO_OUTSIDE_RECTANGLE, -size * number_of_rows * 10,
                           fill=COLOR_BG, outline=COLOR_BG)
    canvas.create_rectangle(size * number_of_rows * 10, size * number_of_rows * 10,
                           -size * number_of_rows * 10, size * number_of_rows + DISTANCE_TABLE_TO_OUTSIDE_RECTANGLE,
                           fill=COLOR_BG, outline=COLOR_BG)


def fill_table(obstacles_index, tiles_index, holes_index, agents_index):
    """
    Create and position all game elements (obstacles, tiles, holes, agents) on the table.
    
    Args:
        obstacles_index: List of obstacle positions
        tiles_index: List of tile positions
        holes_index: List of hole positions
        agents_index: List of agent positions
    
    Returns:
        Tuple of (tiles, holes, agents) lists containing turtle objects
    """
    tiles = []
    holes = []
    agents = []
    
    # Create obstacles
    for obstacle_index in obstacles_index:
        obstacle = turtle.Turtle(shape='square')
        obstacle.speed(MOVEMENT_SPEED)
        obstacle.color('gray')
        obstacle.penup()
        obstacle.turtlesize(TABLE_SIZE / 11)
        position = comins.get_position_with_index(obstacle_index)
        obstacle.goto(position[0], position[1])
    
    # Create tiles
    for tile_index in tiles_index:
        tile = turtle.Turtle()
        tile.shape('tile.gif')
        tile.speed(MOVEMENT_SPEED)
        tile.penup()
        tile.turtlesize(TABLE_SIZE / 15)
        position = comins.get_position_with_index(tile_index)
        tile.goto(position[0], position[1])
        tile.index = tile_index
        tiles.append(tile)
    
    # Create holes
    for hole_index in holes_index:
        hole = turtle.Turtle(shape='square')
        hole.speed(MOVEMENT_SPEED)
        hole.penup()
        hole.turtlesize(TABLE_SIZE / 15)
        hole.color((0.49, 0.24, 0.54))  # Purple color
        position = comins.get_position_with_index(hole_index)
        hole.goto(position[0], position[1])
        hole.index = hole_index
        holes.append(hole)
    
    # Create agents
    for agent_index in agents_index:
        agent = turtle.Turtle(shape='turtle')
        agent.speed(MOVEMENT_SPEED)
        agent.penup()
        agent.turtlesize(TABLE_SIZE / 15)
        agent.color('green')
        position = comins.get_position_with_index(agent_index)
        agent.goto(position[0], position[1])
        agent.index = agent_index
        agents.append(agent)
    
    return tiles, holes, agents


# ============================================================================
# FITNESS CALCULATION FUNCTIONS
# ============================================================================

def nearest_hole_distance(tile, holes):
    """
    Calculate the distance from a tile to its nearest hole.
    
    Args:
        tile: Tile turtle object
        holes: List of hole turtle objects
    
    Returns:
        Minimum distance to any hole
    """
    distances = [comins.distance_between(tile, hole) for hole in holes]
    return min(distances)


def calculate_distance_between_tiles_and_holes(tiles, holes):
    """
    Calculate the total distance between all tiles and their nearest holes.
    Used for fitness calculation.
    
    Args:
        tiles: List of tile turtle objects
        holes: List of hole turtle objects
    
    Returns:
        Sum of distances from each tile to its nearest hole
    """
    return sum(nearest_hole_distance(tile, holes) for tile in tiles)


def get_dropped_tile_count(tiles, holes):
    """
    Count how many tiles have been dropped into holes (same position).
    
    Args:
        tiles: List of tile turtle objects
        holes: List of hole turtle objects
    
    Returns:
        Number of tiles that are in the same position as holes
    """
    count = 0
    for tile in tiles:
        for hole in holes:
            if tile.index == hole.index:
                count += 1
    return count


def calculate_fitness(tiles, holes, distance_between_tiles_and_holes_at_start, rest_steps):
    """
    Calculate the fitness score of the current state.
    
    Fitness = 100 * dropped_tiles + 20 * distance_approached + remaining_steps
    
    Args:
        tiles: List of tile turtle objects
        holes: List of hole turtle objects
        distance_between_tiles_and_holes_at_start: Initial total distance
        rest_steps: List of remaining steps for each agent
    
    Returns:
        Fitness score (higher is better)
    """
    approached_distance = (distance_between_tiles_and_holes_at_start - 
                          calculate_distance_between_tiles_and_holes(tiles, holes))
    rest_step = round(sum(rest_steps) / len(rest_steps)) if rest_steps else 0
    dropped_tiles = get_dropped_tile_count(tiles, holes)
    
    return 100 * dropped_tiles + round(20 * approached_distance) + rest_step


def show_fitness(tiles, holes, distance_between_tiles_and_holes_at_start, rest_steps, label):
    """
    Continuously update the fitness label in a separate thread.
    
    Args:
        tiles: List of tile turtle objects
        holes: List of hole turtle objects
        distance_between_tiles_and_holes_at_start: Initial total distance
        rest_steps: List of remaining steps for each agent
        label: Tkinter label widget to update
    """
    while (calculate_distance_between_tiles_and_holes(tiles, holes) > 0 and 
           sum(rest_steps) > 0):
        time.sleep(0.01)  # Prevent excessive CPU usage
        fitness = calculate_fitness(tiles, holes, distance_between_tiles_and_holes_at_start, rest_steps)
        label.config(text=f'fitness: {fitness}')
    
    final_fitness = calculate_fitness(tiles, holes, distance_between_tiles_and_holes_at_start, rest_steps)
    label.config(text=f'fitness: {final_fitness}', foreground='green')


# ============================================================================
# ALGORITHM EXECUTION FUNCTIONS
# ============================================================================

def run_test(agent, agents, tiles, holes):
    """
    Test function for manual agent movement testing.
    
    Args:
        agent: Agent turtle object
        agents: List of all agent turtle objects
        tiles: List of tile turtle objects
        holes: List of hole turtle objects
    """
    tileins.turn_left(agent, agents, tiles, holes)
    tileins.turn_left(agent, agents, tiles, holes)
    tileins.move_forward(agent, agents, tiles, holes)
    tileins.move_forward(agent, agents, tiles, holes)
    tileins.turn_right(agent, agents, tiles, holes)
    tileins.move_forward(agent, agents, tiles, holes)
    tileins.turn_right(agent, agents, tiles, holes)
    tileins.move_forward(agent, agents, tiles, holes)
    tileins.move_forward(agent, agents, tiles, holes)
    tileins.turn_left(agent, agents, tiles, holes)
    tileins.move_forward(agent, agents, tiles, holes)
    tileins.turn_right(agent, agents, tiles, holes)
    tileins.move_forward(agent, agents, tiles, holes)
    tileins.move_forward(agent, agents, tiles, holes)


def run_agent(individual, agent, agent_index, node, agents, tiles, holes, rest_steps):
    """
    Execute one agent's behavior for one step according to the individual's node structure.
    
    Args:
        individual: Individual data structure (GNP network)
        agent: Agent turtle object to control
        agent_index: Index of the agent in the agents list
        node: Current node index in the individual
        agents: List of all agent turtle objects
        tiles: List of tile turtle objects
        holes: List of hole turtle objects
        rest_steps: List of remaining steps for each agent (modified in place)
    
    Returns:
        Next node index to execute
    """
    temp_for_step = 0
    
    while temp_for_step < EACH_STEP_ACCORDING_TO_DI:
        time.sleep(individual[node][2] * DELAY_TIME)
        
        if individual[node][0] == 1:  # Judgement node
            result = individual[node][1](agent, agents, tiles, holes)
            temp_for_step += individual[node][2]
        elif individual[node][0] == 2:  # Processing node
            individual[node][1](agent, agents, tiles, holes)
            result = 0  # Processing nodes have one connection gene
            temp_for_step += individual[node][2]
        
        node = individual[node][3 + result * 2]
    
    rest_steps[agent_index] -= 1
    return node


def convert_individual_to_tkinter_format(individual):
    """
    Convert individual from GA format to tkinter-compatible format.
    
    Args:
        individual: Individual data structure from GA
    
    Returns:
        Converted individual compatible with tkinter visualization
    """
    converted = [row[:] for row in BASE_INDIVIDUAL]  # Deep copy
    
    for i in range(1, len(individual)):
        if i < len(converted):
            for j in range(3, len(individual[i])):
                converted[i].append(individual[i][j])
    
    return converted


def run_algorithm(individual, agents, tiles, holes, rest_steps, distance_between_tiles_and_holes_at_start, label):
    """
    Run the GNP algorithm and execute agent behaviors.
    
    Args:
        individual: Individual data structure (GNP network)
        agents: List of agent turtle objects
        tiles: List of tile turtle objects
        holes: List of hole turtle objects
        rest_steps: List of remaining steps for each agent
        distance_between_tiles_and_holes_at_start: Initial total distance
        label: Tkinter label widget for fitness display
    """
    individual = convert_individual_to_tkinter_format(individual)
    nodes_for_each_agent = [individual[1][3]] * len(agents)
    
    # Start fitness display thread
    threading.Thread(target=show_fitness, 
                    args=(tiles, holes, distance_between_tiles_and_holes_at_start, rest_steps, label),
                    daemon=True).start()
    
    # Execute algorithm
    for _ in range(INITIAL_REMAINING_STEP):
        for j in range(len(agents)):
            nodes_for_each_agent[j] = run_agent(individual, agents[j], j, 
                                               nodes_for_each_agent[j], agents, tiles, holes, rest_steps)
            if calculate_distance_between_tiles_and_holes(tiles, holes) == 0:
                return


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Initialize and run the visualization application."""
    # Initialize screen and canvas
    screen = turtle.Screen()
    screen.addshape('tile.gif')
    screen.bgcolor(COLOR_BG)
    screen.setup(width=0.6, height=0.8)
    canvas = screen.getcanvas()
    
    # Create UI elements
    label = tk.Label(canvas.master, text='fitness:', font=('Times', 15), bg=COLOR_BG)
    canvas.create_window(variables.label_position_width, variables.label_position_height, window=label)
    
    # Initialize rest steps for each agent
    rest_steps = [INITIAL_REMAINING_STEP] * len(INITIAL_AGENTS_INDEX)
    print(f"Rest steps: {rest_steps}")
    
    # Draw table and create game elements
    draw_table(canvas, TABLE_SIZE, NUMBER_OF_ROWS)
    tiles, holes, agents = fill_table(OBSTACLES_INDEX, INITIAL_TILES_INDEX, 
                                     INITIAL_HOLES_INDEX, INITIAL_AGENTS_INDEX)
    
    # Calculate initial distance
    distance_between_tiles_and_holes_at_start = calculate_distance_between_tiles_and_holes(tiles, holes)
    
    # Create run button
    button = tk.Button(canvas.master, text='RUN', 
                      command=lambda: run_algorithm(RESULT_INDIVIDUAL, agents, tiles, holes,
                                                   rest_steps, distance_between_tiles_and_holes_at_start, label))
    canvas.create_window(variables.button_position_width, variables.button_position_height, window=button)
    
    # Start turtle main loop
    turtle.done()


if __name__ == '__main__':
    main()
