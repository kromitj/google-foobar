moves = [[-1,-2],[-2,-1],[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2]]

class FindShortest_path:
    def __init__(columns, rows, start_pos_val,end_pos_val, moves):
        self.columns = columns
        self.rows = rows
        self.grid = self.generate_grid(columns, rows)
        self.start_pos_yx = self.val_to_yx_cord(start_pos_val)
        self.end_pos_yx = self.val_to_yx_cord(end_pos_val)
        self.moves = moves # don't thin kthis is needed
        self.shortest_path = 9999
        self.enum_moves(self.start_pos, [])


    def enum_moves(current_pos, path_taken):
        if on_destination(current_pos):
            path_length = len(path_taken)
            if path_length < self.shortest_path
                self.shortest_path = path_length
        for move in self.moves:
            prospective_move = calc_move(current, move)
            if move_is_valid(prospective_move):
                new_move = prospective_move
                path_taken.append(current_pos)
                enum_moves(new_move, path_taken)
        return True

    def generate_grid(self, columns, rows):
        grid = []
        cell_num = 0
        for col in range(self.columns):
            grid.append([])
            for row in range(self.rows):
                grid[col][row] = cell_num
                cell_num+=1
        return grid

    def in_boundry(self, move):
        return (y_in_bounds(move[0]) and x_in_bounds(move[1]))

    def move_is_valid(self, move, path_taken):
        if self.havent_been(move, path_taken):
            if self.in_boundry(move):
                return True
        return False

    def on_destination(self, current_pos):
        current_pos == self.end_pos

    def val_to_yx_cord(self, val):
        for col in range(self.columns):
            for row in range(self.rows):
                if self.grid[col][row] == val:
                    return [col, row]

    def x_in_bounds(self, x_cord):
        return (x_cord > 0 and x_cord < self.rows)

    def y_in_bounds(self, y_cord):
        return (y_cord > 0 and y_cord < self.columns)



# example
board = FindShortest_path(8,8,0,1, moves)
return board.shortest_path






for col in 