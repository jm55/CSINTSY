import utils

class bot:
    def __init__(self, grid, sg_loc):
        print("This is bot!")
        self.grid = grid
        self.sg_loc = sg_loc
        self.grid.show_tiles()
        self.frontier = []
        self.explored = []
    def check_sides(self, x, y):
        print(x,y,self.grid.get_adjacent_tiles(x,y))