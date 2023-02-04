import utils
from tile import tile

class grid:
    def __init__(self, n:int, raw_data:list):
        self.n = n
        self.tiles = self.set_tiles(raw_data)  
    def set_tiles(self, raw_data):
        tiles = []
        for i in range(1,self.n+1,1): #Row/Y
            row = list(raw_data[i-1])
            row_tiles = []
            for j in range(self.n): #Column/X
                row_tiles.append(tile(j+1,i,row[j]))
            tiles.append(row_tiles)
        return tiles
    def show_tiles(self):
        print("")
        print("Pattern: type, x, y, dist, g_cost, h_cost, f_cost")
        print("".center(43,"="))
        print()
        for row in self.tiles:
            out = ""
            for col in row:
                out = out + col.get_attribute_str().center(18," ") + "    "
            print(out)
            print("")
        print("")
    def init_distance(self):
        important_pos = self.get_sg_pos() #2D, Format: (S,G)
        for row in self.tiles:
            for col in row:
                col.dist = utils.distance(col.get_xy(), important_pos[1])
    def get_sg_pos(self):
        pos = [[0,0],[0,0]] #s(x,y), g(x,y)
        for row in self.tiles:
            for col in row:
                if col.type == 'S':
                    pos[0][0] = col.x
                    pos[0][1] = col.y
                if col.type == 'G':
                    pos[1][0] = col.x
                    pos[1][1] = col.y
        return pos
