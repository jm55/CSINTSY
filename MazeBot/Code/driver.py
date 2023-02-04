import utils
import file
from grid import grid

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
    g.show_tiles()
    proceed = input("Proceed with search (Y/N): ")
    if proceed.upper() == "Y":
        search_driver(g)
    else:
        utils.cls()
        input("Tracing won't proceed, please press enter to exit...")

def search_driver(grid:grid):
    utils.cls()
    print("Insert search driver code here.")
    input("Press Enter to exit...")

if __name__ == "__main__":
    utils.cls()
    main()
    utils.cls(True)
    exit(0)