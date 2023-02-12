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
                row_tiles.append(tile(j,i-1,row[j]))
            tiles.append(row_tiles)
        return tiles
    def show_simple_tiles(self):
        print("")
        for row in self.tiles:
            out = ""
            for col in row:
                out = out + col.type + "    "
            print(out)
            print("")
        print("")
    def show_tiles(self):
        print("")
        print("Definitions:\nG Cost = Distance from Starting Tile\nH Cost = Distance from Goal Tile\nF Cost = G + H\n")
        print("Pattern: [type, x, y, f_cost, g_cost, h_cost]")
        print()
        for row in self.tiles:
            out = ""
            for col in row:
                out = out + col.get_attribute_str().ljust(28," ") + "  "
            print(out)
        print("")
    def init_distance(self):
        important_pos = self.get_sg_pos() #2D, Format: (S,G)
        #Get distance from S
        for row in self.tiles:
            for col in row:
                col.set_costs(important_pos[0], important_pos[1])
    def get_sg_pos(self): #Gets Start and Goal Position [[s_x,s_y],[g_x,g_y]]
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
    def get_adjacent_tiles(self,x,y): #Return a list of tiles adjacent to the given coordinate. Formatted as [N,W,S,E] with tile's respective x,y coordinates
        search_coor = [[x,y-1],[x-1,y],[x,y+1],[x+1,y]]
        for s in range(len(search_coor)):
            if search_coor[s][0] < 0 or search_coor[s][0] >= self.n or search_coor[s][1] < 0 or search_coor[s][1] >= self.n:
                search_coor[s] = None
        return search_coor
