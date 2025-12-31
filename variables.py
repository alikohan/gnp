"""
Configuration variables for GNP-based tile world simulation.
This module contains the parameters needed for the evolutionary process,
simulation environment, and visualization.
"""

# ============================================================================
# SIMULATION ENVIRONMENT CONFIGURATION
# ============================================================================

# Grid dimensions
number_of_rows = 9  # Number of rows/columns in the tile world grid
table_size = 30  # Size of each grid cell in pixels (for visualization)

# Movement and timing
movement_speed = 50  # Speed of agent movement (for visualization)
initial_remaining_step = 60  # Maximum number of steps per simulation run
delay_time = 0.01  # Delay between steps for visualization (seconds)
each_step_according_to_di = 5  # Step cost calculation parameter


# ============================================================================
# INITIAL WORLD STATE
# ============================================================================

# Environment 1:
# Obstacles (static barriers in the world)
obstacles_index = [[4, 1], [5, 1], [6, 2], [6, 3], [6, 4], [8, 6], [8, 7], [8, 8], [8, 9], [9, 2], [9, 3]]

# Initial tile positions (tiles that need to be moved to holes)
initial_tiles_index = [[3, 2], [5, 3], [8, 3]]

# Initial hole positions (target locations for tiles)
initial_holes_index = [[3, 4], [4, 5], [7, 7]]

# Initial agent positions (agents that will be controlled by GNP networks)
initial_agents_index = [[3, 1], [7, 4], [9, 9]]

# Environment 2:
# obstacles_index = [[4, 1], [5, 1], [2, 7], [2, 8], [2, 9], [5, 8], [6, 2], [6, 3], [6, 8], [8, 6], [8, 7], [8, 8], [9, 2], [9, 3]]
# initial_tiles_index = [[1, 7], [2, 3], [7, 8]]
# initial_holes_index = [[1, 9], [2, 5], [4, 5]]
# initial_agents_index = [[3, 1], [8, 2], [9, 9]]

# Environment 3:
# obstacles_index = [[1, 4], [2, 4], [2, 8], [2, 9], [4, 1], [5, 1], [2, 7], [5, 8], [6, 2], [6, 3], [6, 8], [8, 7], [8, 8], [9, 2], [9, 3]]
# initial_tiles_index = [[1, 7], [2, 3], [7, 8]]
# initial_holes_index = [[1, 9], [3, 5], [6, 4]]
# initial_agents_index = [[3, 1], [8, 2], [3, 9]]


# ============================================================================
# VISUALIZATION CONFIGURATION
# ============================================================================

# UI element positions (for tkinter/turtle visualization)
label_position_width = -340
label_position_height = -250
button_position_width = -340
button_position_height = -200


# ============================================================================
# GENETIC ALGORITHM PARAMETERS
# ============================================================================

# Population settings
population_size = 100  # Number of individuals in the population (should be even)

# Genetic operators
pc = 0.4  # Probability of crossover
pm = 0.01  # Probability of mutation
fitness_bias = 10  # Bias value for roulette wheel selection calculation

# Evolution settings
epoch_number = 10  # Number of generations/epochs to run
run_GA_times = 2  # Number of independent GA runs to execute (for statistical analysis)
