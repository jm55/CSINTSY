import utilities as utils
import gui
from tile import tile
from grid import grid

def main():
    raw_data = utils.read_file(gui.ask_filepath())

    g = grid(raw_data)    
    gui.main(g)
    input()
    
    g.update_bot(0,0)
    gui.main(g)
    input()

    g.update_bot(4,0)
    gui.main(g)
    input()

    #gui.print_simple_grid(g)

def chk():
    print("This is driver.py")

if __name__ == "__main__":
    main()
    exit(0)