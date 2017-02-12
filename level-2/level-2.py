
cols = 8
rows = 8
grid = [x[:] for x in [[Cell(0,0,0,cell_val)] * len(rows)] * len(cols)]
for col in range(cols):
    for row in range(rows):
        cell_val = (col+1)*row
        grid[i][j] = Cell(0,0,0,cell_val)

class Cell:
    def __init__(self,f, g, h, val):
        self.f = f
        self.g = g
        self.h = h
        self.val = val

open_set = []
closed_set = []
start = grid[][0,0]











MOVES = [[-1,-2],[-2,-1],[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2]]

BOARD = [[0, 1, 2, 3, 4, 5, 6, 7],
        [ 8, 9,10,11,12,13,14,15],
        [16,17,18,19,20,21,22,23],
        [24,25,26,27,28,29,30,31],
        [32,33,34,35,36,37,38,39],
        [40,41,42,43,44,45,46,47],
        [48,49,50,51,52,53,54,55],
        [56,57,58,59,60,61,62,63]]

# Moves: [x, y]
     
# BOARD = [[0 , 1, 2,3],
#          [4 , 5, 6,7],
#          [8 , 9,10,11],
#          [12,13,14,15]]



def find_value(board, value):
    for row in board:
        for el in row:
            if el == value:
                return [board.index(row), row.index(el)] 

# dest = 2
def move_valid(poss_move, places_been): 
    # [1,-1]
    return x_valid(poss_move[1]) and y_valid(poss_move[0]) and havnt_been_before(poss_move, places_been)

def havnt_been_before(poss_move, places_been):
    for place in places_been:
        if place == poss_move:
            return False
    return True
    
def x_valid(x_move):
    board_width = len(BOARD[0])
    return x_move >= 0 and x_move < board_width



def y_valid(y_move):
    board_height = len(BOARD)
    return y_move >= 0 and y_move < board_height

# def player_move(player_loc, moves, move_num, dest, places_been):
#     if move_num == len(moves):
#         return None
#     poss_move = calc_move(player_loc, moves[move_num])
#     if move_valid(poss_move, places_been): 
#         if player_on_destination(dest, poss_move):
#             places_been.append(player_loc)
#             return len(places_been)
#         else:
#             places_been.append(player_loc)
#             dest_found = player_move(poss_move, moves, 0, dest, places_been)
#             if dest_found:
#                 return dest_found
#             else:
#                 move_num+=1
#                 return player_move(player_loc, moves, move_num, dest, places_been)
#     else:
#         move_num+=1
#         return player_move(player_loc, moves, move_num, dest, places_been)



def player_move(player_loc, moves, move_num, dest, places_been):
    if move_num == len(moves):
        return None
    poss_move = calc_move(player_loc, moves[move_num])
    if move_valid(poss_move, places_been): 
        if player_on_destination(dest, poss_move):
            places_been.append(player_loc)
            return places_been
        else:
            places_been.append(player_loc)
            response = player_move(poss_move, moves, 0, dest, places_been)
            if response != None:
                return response 
    move_num+=1
    return player_move(player_loc, moves, move_num, dest, places_been)


def player_moves(player_loc, moves, move_num, dest, places_been):  
    last_move = moves[len(moves)-1]
    shortest = 10000000000000
    move_num = move_num
    for move in moves:
        result = player_move(player_loc, moves, move_num, dest, places_been)
        print(result)
        if (result < shortest) and result != None:
            shortest = result
        if move == last_move:
            return shortest   
        move_num+=1




def calc_move(player_loc, move):
    return [(player_loc[0] + move[0]), (player_loc[1] + move[1])]


def player_on_destination(dest, player_loc):
    return dest == BOARD[player_loc[0]][player_loc[1]]


# result = player_move([2,3], MOVES, 0, 39, [])
# print(result)


shortest_path = False


def find_path(player_loc, dest, places_been, shortest_path):
    if (move_valid(player_loc, places_been) == False): return False
    places_been.append(player_loc)
    print(places_been)
    if (player_on_destination(dest, player_loc)): return len(places_been)

    response = find_path(calc_move(player_loc, MOVES[0]),dest, places_been, shortest_path)
    if (response != False): 
        if shortest_path == False or response < shortest_path:
            shortest_path = response
            return shortest_path

    response = find_path(calc_move(player_loc, MOVES[1]),dest, places_been, shortest_path)  
    if (response != False): 
        if shortest_path == False or response < shortest_path:
            shortest_path = response
            return shortest_path
        

    response = find_path(calc_move(player_loc, MOVES[2]),dest, places_been, shortest_path)  
    if (response != False): 
        if shortest_path == False or response < shortest_path:
            shortest_path = response
            return shortest_path
        

    response = find_path(calc_move(player_loc, MOVES[3]),dest, places_been, shortest_path)  
    if (response != False): 
        if shortest_path == False or response < shortest_path:
            shortest_path = response
            return shortest_path
        

    response = find_path(calc_move(player_loc, MOVES[4]),dest, places_been, shortest_path)  
    if (response != False): 
        if shortest_path == False or response < shortest_path:
            shortest_path = response
            return shortest_path
        

    response = find_path(calc_move(player_loc, MOVES[5]),dest, places_been, shortest_path)  
    if (response != False): 
        if shortest_path == False or response < shortest_path:
            shortest_path = response
            return shortest_path
        

    response = find_path(calc_move(player_loc, MOVES[6]),dest, places_been, shortest_path) 
    if (response != False): 
        if shortest_path == False or response < shortest_path:
            shortest_path = response
            return shortest_path
        

    response = find_path(calc_move(player_loc, MOVES[7]),dest, places_been, shortest_path)  
    if (response != False): 
        if shortest_path == False or response < shortest_path:
            shortest_path = response
            return shortest_path


path = find_path([0,0], 5, [], shortest_path)
print(path)







# http://stackoverflow.com/questions/11101418/a-star-algorithm-for-chess-piece-pathfinding

  def a_star(board, moves, start_xy, end_xy):
    opened = []
    closed = []
    zero = []
    current_node = start_xy
    new_x = 0
    new_y = 0
    opened.append(current_node)
    for move in moves:
      new_x = current_node[1] + move[1]
      new_y = current_node[0] + move[0]
      if ((new_x >= 0) and (new_x < len(BOARD[0])) and ((new_y >= 0) and (new_y < len(BOARD)))):
        new_pos = [new_y, new_x]
        adjacent_node = [[new_pos], current_node, 1]
        opened.append(adjacent_node)
    closed.append(opened[0])
    opened.remove(current_node)
    while len(opened) > 0:
      lowest = 999
      lowest_index = 0 

      for i, openee in opened:
        if openee[2] < lowest:
          lowest = openee[2]
          lowest_index = i

      closed.append(apen[lowestIndex])
      if (opened[lowestIndex][1] == end_xy[1]) && (opened[lowestIndex][0] == end_xy[0]):
        return closed
      opened.pop(lowest_index)
      current_node = closed[-1]
      for move in moves:
        is_in_closed = False 
        is_in_opened = False 
        new_x = current_node[1][1]
        new_y = current_node[1][0]
        if ((new_x >= 0)and(new_x < len(BOARD[0]))) and ((new_y >= 0)and(new_y < len(BOARD))):
          new_pos = [new_y, new_x]
          adjacent_node = [[new_pos],[current_node], (current_node[2]+1)]
          opened.append(adjacent_node)
          for i, closee in closed:
            if ((closed[i][0][0] == adjacent_node[0][0]) and ((closed[i][0][1] == adjacent_node[0][1])):
              is_in_closed = True

          if is_in_closed == False:
            for i, openee in opened:
              if ((opened[i][1][1] == adjacent_node[1][0]) and (opened[i][1][0] == adjacent_node[1][1])):
                is_in_opened = true
                if (adjacent_node[2] + 1) < openee[2]:
                  openee.parent = adjacent_node # need to create parent funct
                  openee[2] = (adjacent_node[2] + openee[2])

          if is_in_opened:
            opened.append(adjacent_node)














