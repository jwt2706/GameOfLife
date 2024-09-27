from random import random
from time import sleep
import os

# excludes borders
ARENA_WIDTH = 25
ARENA_HEIGHT = 25

CELL_SPAWN_RATE = 0.5 #0.07

ALIVE_CELL = "*"
DEAD_CELL = "."
BORDER = "#"


def generate_arena():

    # the arena is represented with a matrix
    arena = []

    for i in range(ARENA_HEIGHT):
        
        # build row
        row = []
        for j in range(ARENA_WIDTH):
            if (random() < CELL_SPAWN_RATE):
                row.append(ALIVE_CELL)
            else:
                row.append(DEAD_CELL)
        arena.append(row)

    return arena


def print_arena(arena):
    def border():
        print(BORDER+' ', end='')
    
    def x_border():
        for i in range(ARENA_HEIGHT+2):
            border()
        print()

    x_border() # x border, top side
    for i in range(ARENA_HEIGHT): 
        border() # y border, left side
        
        for j in range(ARENA_WIDTH):    
            print(arena[i][j]+' ', end='')
            
        border() # y border, right side
        print()
    x_border() # x border, bottom side

#1. any live cell with fewer than two live neighbors dies as if caused by underpopulation
#2. any live cell with two or three live neighbors lives on the next generation
#3. any live cell with more than three live neighbords dies, as if by overpopulation
#4. any dead cell with exactly three live nieghtbors becomes a live cell, as if by reporoduction
def update_arena(arena):
    for i in range(ARENA_HEIGHT):
        for j in range(ARENA_WIDTH):
            num_of_neighbors = get_neighborhood_population(arena, i, j)                
            arena[i][j] = update_cell(arena[i][j], num_of_neighbors)
    return arena

def get_neighborhood_population(arena, x, y):
    num_of_neighbors = 0
    neighbor_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for direction in neighbor_directions:
        neighbor_x = x + direction[0]
        neighbor_y = y + direction[1]
        
        # just a sanity check to make sure we aren't out of bound
        if (neighbor_x > 0 and neighbor_x < ARENA_WIDTH) and (neighbor_y > 0 and neighbor_y < ARENA_HEIGHT):
            if (arena[neighbor_x][neighbor_y] == ALIVE_CELL):
                num_of_neighbors += 1
    return num_of_neighbors

def update_cell(cell_state, num_of_neighbors):
    if (num_of_neighbors < 2) or (num_of_neighbors > 3) or (cell_state == DEAD_CELL and num_of_neighbors != 3):
        return DEAD_CELL
    else:
        return ALIVE_CELL 


os.system('clear')
arena = generate_arena()
while (True):
    print_arena(arena)
    arena = update_arena(arena)
    sleep(1)
    os.system('clear')
