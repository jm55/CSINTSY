import utils
import file
from grid import grid
from bot import bot

def main():
    filename = input("Enter filename (including .txt; Empty for default): ")
    if filename == "":
        filename = "maze.txt"
    utils.cls()

    n, raw_data = file.readfile("maze.txt")
    print("Grid Size: " + str(n))
    print("Raw_Data: ", raw_data)
    g = grid(n, raw_data)
    g.init_distance()
    
    print("")
    proceed = input("Proceed with search (Y/N): ")
    if proceed.upper() == "Y":
        search_driver(g)
    else:
        utils.cls()
        print("Searching won't proceed!")

def search_driver(grid:grid):
    utils.cls()
    b = bot(grid, grid.get_sg_pos())

if __name__ == "__main__":
    utils.cls()
    main()
    print("")
    input("Press Enter to exit...")
    utils.cls(True)
    exit(0)