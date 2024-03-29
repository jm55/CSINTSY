import os
import datetime
import codecs

from objects import *
global dimension

def find_direction(prev_pos:tuple, curr_pos:tuple):
    x_diff = curr_pos[0] - prev_pos[0]
    y_diff = curr_pos[1] - prev_pos[1]
    if x_diff == -1: #left
        return '←'
    elif x_diff == 1: #right
        return '→'
    elif y_diff == -1: #up
        return '↑'
    elif y_diff == 1: #down
        return '↓'
    return '-'

def read_maze(filepath:str):
    """Generates a 2d list of the maze and creates a grid object after completing the 
    parsing of the maze file"""
    
    with open(filepath, "r") as maze_file:
        size = int(maze_file.readline())
        tiles = [[0]*size for i in range(size)]
        for y in range(size):
            line = maze_file.readline().strip()
            for x in range(len(line)):
                tile_type = line[x]
                tiles[x][y] = tile(x, y, tile_type)
                
        grid_obj = grid(tiles)
    return grid_obj

def get_manhattan(pos1, pos2):
    """Returns the manhattan distance between two points"""
    return (abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1]))

def readfile(filename):
    maze = []
    with open(filename) as maze_file:
        str_dimension = maze_file.readline().strip()
        
        global dimension
        dimension = int(str_dimension)

        maze_contents = maze_file.readlines()
        for row in maze_contents:
            maze.append(row.strip())
    return maze

def save_file(printable:list):
    filename = str(datetime.datetime.utcnow())
    ctr = 0
    with codecs.open(filename.replace(':','-')+".txt", "w", "utf-8") as output_file:
        output_file.write("".center(40,"=")  + "\n")
        output_file.write("MazeBot: MCO1".center(40," ")  + "\n")
        output_file.write("CSINTSY S14".center(40," ")  + "\n")
        output_file.write("Cruzada, Escalona, Francisco, Loyola".center(40," ")  + "\n")
        output_file.write("".center(40,"=")  + "\n")
        output_file.write("")
        output_file.write("\nResulting Grid Movement:\n")
        output_file.write(printable[0])
        output_file.write("\nResulting Grid Movement (by  Coordinates):\n")
        for p in printable[1]:
            output_file.write(str(p)  + " ")
            ctr += 1
            if ctr == 6:
                ctr = 0
                output_file.write("\n")
        output_file.close()

def cls():
    """Execute 'cls' command on Command Prompt"""
    os.system("cls")
