from grid import grid
import utilities as utils
import time

def ask_performance():
    cont = True
    fast_search = False
    print(utils.header())
    if input("Manual Control (Y/N): ").lower() == 'n':
        cont = False
    if input("Fast Search (Y/N): ").lower() == 'y':
        fast_search = True
    return cont, fast_search

#Prints the major components of a grid printout
def main(grid:grid):
    utils.cls()
    print(utils.header())
    print_simple_grid(grid)

#Get the contents of a given item list (frontier or explored) 
#and return contents of bot's x,y as str list
def get_grid_list(items:list):
    output = ""
    ctr = 0
    br_limit = 6
    for item in items:
        output += str(item.locate_bot()) + " "
        ctr += 1
        if ctr == br_limit:
            ctr = 0
            output += "\n"
            output += "".center(17," ")
    return output

#Conduct a replay from using the frontier and explored list.
#Parameter cont if to display the "Press Enter key to continue..." input
def replay(frontier:list, explored:list, cont:bool=True, fast_search:bool=False):
    if len(frontier) == 0 or len(explored) == 0:
        utils.cls()
        print(utils.header())
        print("No path found for given maze!")
        return False
    elif not fast_search: 
        utils.cls()
        for c in explored:
            main(c)
            print("Bot's Frontier: ", get_grid_list(frontier))
            print("Bot's Explored: ", get_grid_list(explored))
            time.sleep(0.1)
        if cont:
            input("\n\nPress Enter key to continue...")
        return True

#Asks the user for filepath of maze file
def ask_filepath():
    utils.cls()
    print(utils.header())
    fp = input("Enter filename (include .txt; Empty defaults to maze.txt): ")
    utils.cls()
    if fp == "":
        return "maze.txt"
    else:
        return fp

#Prints the grid with its auxiliary information such as distances and costs of bot.
def print_simple_grid(grid:grid):
    tiles = grid.get_tiles()
    size = grid.get_size()

    #Print the grid
    print("MAZE GRID")
    print(utils.bar(size*2))
    for y in range(size):
        row = ""
        for x in range(size):
            tile = tiles[y][x].get_attributes()
            row = row + tile[0] + " "
        print(row)
    print(utils.bar(size*2))
    
    #Print auxiliary information
    print("\nStart Location:", grid.locate_s())
    print("Goal Location: ", grid.locate_g())
    print("\nBot Location: ", grid.locate_bot())
    print("Bot's Distance from S: ", grid.get_bot().s_dist)
    print("Bot's Distance from G: ", grid.get_bot().g_dist)
    print("Bot's Moves Count: ", grid.g_cost)
    print("Bot's Total Move Cost (F_Cost): ", str(grid.f_cost) + " = (" + str(grid.g_cost) + " + " + str(grid.h_cost) + ")")