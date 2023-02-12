import utils

class tile:
    def __init__(self, x:int, y:int, tile_type:chr):
        self.x = x
        self.y = y
        self.type = tile_type
        self.f_cost = 0 #f=g+h
        self.g_cost = 0 #dist from starting node
        self.h_cost = 0 #dist from end node
        self.prev_tile = []
    def print_attributes(self):
        print(self.get_attribute_str())
    def get_attribute_str(self):
        return self.type + " " + str(self.x) + " " + str(self.y) + " " + str("%.2f" % self.f_cost) + " " + str("%.2f" % self.g_cost) + " " + str("%.2f" % self.h_cost)
    def get_xy(self):
        return [self.x, self.y]
    def get_costs(self):
        return [round(self.g_cost,2), round(self.h_cost,2), round(self.f_cost,2)]
    def get_attribute_list(self):
        return [self.type, self.x, self.y, self.g_cost, self.h_cost, self.f_cost]
    def set_costs(self, start_pos:list, goal_pos:list):
        #if(self.type == "#"):
            self.g_cost = -1
            self.h_cost = -1
            self.f_cost = -1
        #else:
            self.g_cost = utils.distance(self.get_xy(), start_pos)
            self.h_cost = utils.distance(self.get_xy(), goal_pos)
            self.f_cost = self.g_cost + self.h_cost