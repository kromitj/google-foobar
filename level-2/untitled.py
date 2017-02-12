
MOVES = [[-1,-2],[-2,-1],[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2]]

BOARD = [[0, 1, 2, 3, 4, 5, 6, 7],
        [ 8, 9,10,11,12,13,14,15],
        [16,17,18,19,20,21,22,23],
        [24,25,26,27,28,29,30,31],
        [32,33,34,35,36,37,38,39],
        [40,41,42,43,44,45,46,47],
        [48,49,50,51,52,53,54,55],
        [56,57,58,59,60,61,62,63]]

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
      if ((new_x >= 0 and new_x < len(BOARD[0]) and (new_y >= 0 and new_y < len(BOARD))):
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

      closed,append(apen[lowestIndex])
      if (opened[lowestIndex][1] == end_xy[1]) && (opened[lowestIndex][0] == end_xy[0]):
        return closed
      opened.pop(lowest_index)
      current_node = closed[-1]
      for len(moves):
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







