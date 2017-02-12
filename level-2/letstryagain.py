MOVES = [[-1,-2],[-2,-1],[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2]]

BOARD = [[0, 1, 2, 3, 4, 5, 6, 7],
        [ 8, 9,10,11,12,13,14,15],
        [16,17,18,19,20,21,22,23],
        [24,25,26,27,28,29,30,31],
        [32,33,34,35,36,37,38,39],
        [40,41,42,43,44,45,46,47],
        [48,49,50,51,52,53,54,55],
        [56,57,58,59,60,61,62,63]]


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


def calc_move(player_loc, move):
    return [(player_loc[0] + move[0]), (player_loc[1] + move[1])]


def player_on_destination(dest, player_loc):
    return dest == BOARD[player_loc[0]][player_loc[1]]


def player_move(player_loc, dest, places_been, moves, move_num):
    print(places_been)
    if player_on_destination(dest, player_loc):
        return len(places_been)
    if move_num >= len(moves):
        return False
    while move_num < 8:        
        move_location = calc_move(player_loc, moves[move_num])
        if move_valid(move_location, places_been):
            places_been.append(player_loc)
            response =  player_move(move_location, dest, places_been, moves, 0)
            if response != False:
                return response
            else:
                move_num+= 1
                response = player_move(move_location, dest, places_been, moves, move_num)
        else:
            move_num+=1
            response = player_move(player_loc, dest, places_been, moves, move_num)
    return False




start_loc = [0,0]
dest = [0,1]
shortest_moves = 9999
places_been = []

for move in MOVES:
    response = player_move(start_loc, dest, places_been, MOVES, 0)
    print response
    if (response != False ) and (response < shortest_moves):
        shortest_moves = response

print shortest_moves




