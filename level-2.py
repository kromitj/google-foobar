[ 0, 1, 2, 3, 4, 5, 6, 7]
[ 8, 9,10,11,12,13,14,15]
[16,17,18,19,20,21,22,23]
[24,25,26,27,28,29,30,31]
[32,33,34,35,36,37,38,39]
[40,41,42,43,44,45,46,47]
[48,49,50,51,52,53,54,55]
[56,57,58,59,60,61,62,63]


# Moves: [x, y]
     
[[ 0, 1, 2, 3, 4, 5, 6, 7],
[ 8, 9,10,11,12,13,14,15],
[16,17,18,19,20,21,22,23],
[24,25,26,27,28,29,30,31],
[32,33,34,35,36,37,38,39],
[40,41,42,43,44,45,46,47],
[48,49,50,51,52,53,54,55],
[56,57,58,59,60,61,62,63]]


def answer(src, dest):
    # your code here


def find_value(board, value):
    for row in board:
        for el in row:
            if el == value:
                return [board.index(row), row.index(el)] 

MOVES = [[-2,-1],[-1, -2],[1, -2],[2, -1],[2, 1],[1, 2],[-1, 2],[-2, 1]]

def move_valid(player_loc, move): 
    #move = [-2,-1]
    #playerloc = [2, 4]
    return x_valid(move[0], player_loc[1]) and y_valid(move[1], player_loc[0])
    
def x_valid(x_move, player_loc_x):
# -2, 4
return (player_loc_x + x_move) >= 0



def y_valid(y_move, player_loc_y):
    # -1, 2
    return (player_loc_y + y_move) >= 0 



def player_move(player_loc, move, dest)
    if move_valid(player_loc, move):
        player_loc = move_player(player_loc, move)
        if player_on_destination(dest, player_loc):

end

def move_player(player_loc, move):
    return [(b[0]+a[1]), (b[1]+a[0])]


def player_on_destination(dest, player_loc):
    return dest == BOARD[player_loc[0]][player_loc[1]]






