import utilities as utils
import gui
from tile import tile
from grid import grid
from bot import bot

def main():
    raw_data = utils.read_file(gui.ask_filepath()) #Gather raw data
    performance = gui.ask_performance()

    g = grid(raw_data) #Build grid/initial state with raw data
    b = bot(g) #Build the bot

    b.a_star(performance[0],performance[1]) #Let bot perform A* search

    #Conduct replay from initial to goal's optimal path until user exits.
    replay = True
    while replay: 
        if gui.replay(b.frontier, b.explored, False, False):
            if input("\nEnter any key to replay or X/x to Exit: ") == 'x':
                replay = False
        else:
            replay = False

if __name__ == "__main__":
    main()
    exit(0)