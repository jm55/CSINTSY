class tile:
    def __init__(self, x:int, y:int, tile_type:chr):
        self.x = x
        self.y = y
        self.dist = 0.0
        self.type = tile_type
        self.g_cost = 0
        self.h_cost = 0
        self.f_cost = 0
    def print_attributes(self):
        print(self.get_attribute_str())
    def get_attribute_str(self):
        return self.type + " " + str(self.x) + " " + str(self.y) + " " + str("%.2f" % self.dist) + " " + str(self.g_cost) + " " + str(self.h_cost) + " " + str(self.f_cost)
    def get_xy(self):
        return [self.x, self.y]