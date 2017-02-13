from cell import Cell
from a_star import AStar


class Board(object):
    def __init__(self, columns, rows, start_loc, end_loc):
        self.columns = columns
        self.rows = rows
        self.show_grid = [[" " for x in range(columns)] for y in range(rows)]
        
        self.start_yx = self.__cell_num_to_xy_cord(start_loc)
        self.end_yx = self.__cell_num_to_xy_cord(end_loc)
        grid = self.__generate_board(columns, rows)
        self.astar = AStar(self.start_yx, self.end_yx, grid)

    def __cell_num_to_xy_cord(self, cell_num):
        row = cell_num/self.rows
        column = cell_num%self.rows
        return [row, column]

    def __generate_board(self, columns, rows):
        grid = [[0 for x in range(columns)] for y in range(rows)]
        cell_num = 0
        for col in range(columns):
            for row in range(rows):
                grid[col][row] = Cell(row, col ,cell_num)
                cell_num+=1

        for col in range(columns):
            for row in range(rows):
                grid[col][row].find_valid_neighbors(grid, self.columns, self.rows)

        return grid

    def  run_calc(self, draw_grid):
        response = self.astar.run_calc()
        if draw_grid:
            self.update_show_grid()
            self.draw_grid()
        return response




    def grid_path(self):
        for col in range(self.columns):
            for row in range(self.rows):
                self.show_grid[col][row] = " "
        for path in self.astar.path:
            self.show_grid[path.y][path.x] = "$"


    def update_show_grid(self):
        end_y = self.end_yx[0]
        end_x = self.end_yx[1]
        self.show_grid[end_y][end_x] = "X"
        for set in self.astar.open_set:
            self.show_grid[set.y][set.x] = "@"
        for set in self.astar.closed_set:
            self.show_grid[set.y][set.x] = "*"

    def draw_grid(self):
        print("_______________________________")
        for row in self.show_grid:
            print(row)


