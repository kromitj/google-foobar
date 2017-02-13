import math

class Cell(object):

    def __init__(self,x,y, val):
        self.moves = [[-1,-2],[-2,-1],[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2]]
        self.x = x
        self.y = y
        self.f = 0
        self.g = 0
        self.h = 0
        self.val = val
        self.neighbors = []
        self.previous = False

    def add_neighbor(self, grid, calc_neighbor):
            self.neighbors.append(grid[calc_neighbor[0]][calc_neighbor[1]])

    def calc_heuristic(self, neighbor):
        return math.sqrt( ( (self.y - neighbor.y)**2 + (self.x - neighbor.y)**2) )
    
    def calc_neighbor(self, move):
        return [(self.y + move[0]), (self.x + move[1])]

    def find_valid_neighbors(self, grid, columns, rows):
        for move in self.moves :
            calc_neighbor = self.calc_neighbor(move)
            if self.move_valid(calc_neighbor, columns, rows):
                self.add_neighbor(grid, calc_neighbor)

    def move_valid(self, move, columns, rows):
        y_move = move[0]
        x_move = move[1]
        return self.y_valid(y_move, columns) and self.x_valid(x_move, rows)

    def x_valid(self, x_move, rows):
        return x_move >= 0 and x_move < rows


    def y_valid(self, y_move, cols):
        return y_move >= 0 and y_move < cols

    def yx_cord(self):
        y = self.y
        x = self.x
        return [y, x]        

