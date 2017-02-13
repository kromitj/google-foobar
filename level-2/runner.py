import math
from board import Board

def answer(src, dest):
    lowest = 1000
    board = Board(8,8,src,dest)
    status = True
    while status == True:
        status = board.run_calc(False)
        if type(status) == int:
            print status      
            board.grid_path()
            board.draw_grid()
            lowest =  status
    board = Board(8,8,dest, src)
    status = True
    while status == True:
        status = board.run_calc(False)
        if type(status) == int:
            print  status    
            board.grid_path()
            board.draw_grid()
            if status < lowest:
                lowest = status
    return lowest

answers = []
for start in range(63):
    for dest in range(63):
        result = answer(start, dest)
        result_hash = {"start": str(start), "end": str(dest), "result": str(result)}
        answers.append(result_hash)


sorted = sorted(answers, key=lambda answer: answer["result"])
for answer in sorted:
    sentence = "start: " + str(answer["start"]) + "  end: " + answer["end"] + " result: " + answer["result"]
    f = open('all_answers.txt', 'a+')
    f.write(sentence)
    f.write("\n")
# answer(62, 20)
# answer(20,62)




# class Cell(object):

#     def __init__(self,x,y, val):
#         self.moves = [[-1,-2],[-2,-1],[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2]]
#         self.x = x
#         self.y = y
#         self.f = 0
#         self.g = 0
#         self.h = 0
#         self.val = val
#         self.neighbors = []
#         self.previous = False

#     def add_neighbor(self, grid, calc_neighbor):
#             self.neighbors.append(grid[calc_neighbor[0]][calc_neighbor[1]])

#     def calc_heuristic(self, neighbor):
#         return math.sqrt( ( (self.y - neighbor.y)**2 + (self.x - neighbor.y)**2) )
    
#     def calc_neighbor(self, move):
#         return [(self.y + move[0]), (self.x + move[1])]

#     def find_valid_neighbors(self, grid, columns, rows):
#         for move in self.moves :
#             calc_neighbor = self.calc_neighbor(move)
#             if self.move_valid(calc_neighbor, columns, rows):
#                 self.add_neighbor(grid, calc_neighbor)

#     def move_valid(self, move, columns, rows):
#         y_move = move[0]
#         x_move = move[1]
#         return self.y_valid(y_move, columns) and self.x_valid(x_move, rows)

#     def x_valid(self, x_move, rows):
#         return x_move >= 0 and x_move < rows


#     def y_valid(self, y_move, cols):
#         return y_move >= 0 and y_move < cols

#     def yx_cord(self):
#         y = self.y
#         x = self.x
#         return [y, x]       

# ## open_set =  op_set
# ## closed_set = cl_set
# ## start_loc = start_location

# class AStar(object):

#     def __init__(self, start_loc, destination_loc, grid):
#         self.path = []
#         self.open_set = []
#         self.closed_set = []
#         self.grid = grid
#         self.start_loc = self.set_start_loc(start_loc)
#         self.destination_loc = self.set_end_loc(destination_loc)
#         self.lowest_f_val_idx = -1
#         self.current_set = ""
#         self.open_set.append(self.start_loc)

#     def run_calc(self):
#         if self.op_set_not_empty():
#             self.set_lowest_f_val_idx(0)               
#             self.check_for_lowest_f_val()
#             self.set_current_set()
#             if self.current_on_destination() == True:
#                 self.find_path()
#                 return len(self.path)-1
#             self.transfer_current_to_closed()
#             neighbors = self.currents_neighbors()
#             self.neighbor_logic(neighbors)
#             return True
#         else:
#             return False

#     def assign_current_set(self):
#         self.current_set = open_set[self.lowest_f_val_idx]
        
#     def cell_has_new_lower_g_val(self, set_cell, comparision_val):
#         return (comparision_val < set_cell.g)

#     def check_for_lowest_f_val(self):
#         for idx, set in enumerate(self.open_set):
#             if set.f < self.open_set[self.lowest_f_val_idx].f:
#                 self.set_lowest_f_val_idx(idx)
                
#     def current_on_destination(self):
#         return self.open_set[self.lowest_f_val_idx]== self.destination_loc
        
#     def currents_neighbors(self):
#         return self.current_set.neighbors

#     def find_path(self):
#         temp = self.current_set
#         self.path.append(temp)
#         while temp.previous:
#             self.path.append(temp.previous)
#             temp = temp.previous

#     def neighbor_in_op_set(self, neigbor):
#         return (neigbor in self.open_set)
            
#     def neighbor_logic(self, neighbors):
#         for neighbor in neighbors:
#             if self.neighbor_not_in_cl_set(neighbor):
#                 self.set_neighbor_values(neighbor)

#     def neighbor_not_in_cl_set(self, neighbor):
#         return (neighbor not in self.closed_set)
        
#     def op_set_not_empty(self):
#         return (len(self.open_set) > 0)
        
#     def set_cell_g_val(self, cell, value):
#         cell.g = value

#     def set_current_set(self):
#         self.current_set = self.open_set[self.lowest_f_val_idx]

#     def reset_lowest_f_val_idx(self):
#         self.lowest_f_val_idx = 0


#     def set_lowest_f_val_idx(self, value):
#         self.lowest_f_val_idx = value

#     def set_neighbor_f_val(self,neighbor):
#         neighbor.f = neighbor.g + neighbor.h

#     def set_neighbor_g_val(self, neighbor):
#         temp_g = self.current_set.g+1
#         if self.neighbor_in_op_set(neighbor):
#             if self.cell_has_new_lower_g_val(neighbor, temp_g):
#                 self.set_cell_g_val(neighbor, temp_g)
#         else:
#             self.set_cell_g_val(neighbor, temp_g)
#             self.open_set.append(neighbor)

#     def set_neighbor_h_val(self,neighbor):
#         dist = self.current_set.calc_heuristic(neighbor)
#         neighbor.h = dist    

#     def set_neighbor_previous(self, neighbor):
#         neighbor.previous = self.current_set

#     def set_neighbor_values(self, neighbor):
#         self.set_neighbor_g_val(neighbor)
#         self.set_neighbor_h_val(neighbor)
#         self.set_neighbor_f_val(neighbor)
#         self.set_neighbor_previous(neighbor)

#     def set_end_loc(self, end_yx):
#         y = end_yx[0]
#         x = end_yx[1]
#         return self.grid[y][x]       

#     def set_start_loc(self, start_yx):
#         y = start_yx[0]
#         x = start_yx[1]
#         return self.grid[y][x]


#     def transfer_current_to_closed(self):
#         self.closed_set.append(self.current_set)
#         self.open_set.remove(self.current_set)


# class Board(object):

#     def __init__(self, columns, rows, start_loc, end_loc):
#         self.columns = columns
#         self.rows = rows
#         self.show_grid = [[" " for x in range(columns)] for y in range(rows)]
        
#         self.start_yx = self.__cell_num_to_xy_cord(start_loc)
#         self.end_yx = self.__cell_num_to_xy_cord(end_loc)
#         grid = self.__generate_board(columns, rows)
#         self.astar = AStar(self.start_yx, self.end_yx, grid)

#     def __cell_num_to_xy_cord(self, cell_num):
#         row = cell_num/self.rows
#         column = cell_num%self.rows
#         return [row, column]

#     def __generate_board(self, columns, rows):
#         grid = [[0 for x in range(columns)] for y in range(rows)]
#         cell_num = 0
#         for col in range(columns):
#             for row in range(rows):
#                 grid[col][row] = Cell(row, col ,cell_num)
#                 cell_num+=1

#         for col in range(columns):
#             for row in range(rows):
#                 grid[col][row].find_valid_neighbors(grid, self.columns, self.rows)

#         return grid

#     def  run_calc(self, draw_grid):
#         response = self.astar.run_calc()
#         if draw_grid:
#             self.update_show_grid()
#             self.draw_grid()
#         return response

#     def grid_path(self):
#         for col in range(self.columns):
#             for row in range(self.rows):
#                 self.show_grid[col][row] = " "
#         for path in self.astar.path:
#             self.show_grid[path.y][path.x] = "$"


#     def update_show_grid(self):
#         end_y = self.end_yx[0]
#         end_x = self.end_yx[1]
#         for set in self.astar.open_set:
#             self.show_grid[set.y][set.x] = "@"
#         for set in self.astar.closed_set:
#             self.show_grid[set.y][set.x] = "*"
#         self.show_grid[end_y][end_x] = "X"

#     def draw_grid(self):
#         print("-----------------------------")
#         for row in self.show_grid:
#             print(row)





