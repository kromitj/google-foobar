
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


result = player_move([2,3], MOVES, 0, 39, [])
print(result)



















