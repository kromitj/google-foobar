import math

cols = 8
rows = 8
cell_num = 0
grid = [[0 for x in range(cols)] for y in range(rows)]


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
	
	def calc_neighbor(self, move):
		return [(self.y + move[0]), (self.x + move[1])]

	def x_valid(self, x_move):
		return x_move >= 0 and x_move < rows

	def y_valid(self, y_move):
		return y_move >= 0 and y_move < cols


	def move_valid(self, move):
		y_move = move[0]
		x_move = move[1]
		return self.y_valid(y_move) and self.x_valid(x_move)
	
	def find_valid_neighbors(self, grid):
		for move in self.moves :
			calc_neighbor = self.calc_neighbor(move)
			if self.move_valid(calc_neighbor):
				self.add_neighbor(grid, calc_neighbor)


	def add_neighbor(self, grid, calc_neighbor):
			self.neighbors.append(grid[calc_neighbor[0]][calc_neighbor[1]])

	def calc_heuristic(self, neighbor):
		return math.sqrt( ( (self.y - neighbor.y)**2 + (self.x - neighbor.y)**2) )

	def show(self):
		return self.val



for col in range(cols):
	for row in range(rows):
		grid[col][row] = Cell(row, col ,cell_num)
		cell_num+=1

for col in range(cols):
	for row in range(rows):
		grid[col][row].find_valid_neighbors(grid)

open_set = []
closed_set = []
start = grid[2][3]
end = grid[4][4]
show_grid = [["_" for x in range(cols)] for y in range(rows)]
open_set.append(start)

def update_grid(grid, open, closed):
	for set in open:
		grid[set.y][set.x] = "^"
	for set in closed:
		grid[set.y][set.x] = "="

def draw_grid(grid):
	for row in show_grid:
		print(row)

def draw():
	if len(open_set) > 0:
		lowest_index = 0
		for i in range(len(open_set)):
			if open_set[i] == end:
				print("you handed on the square")
				return False
			if open_set[i].f < open_set[lowest_index].f:
				lowest_index = i
		current = open_set[lowest_index]
		if open_set[lowest_index] == end:
			print("you handed on the square")
			return False
		modify_set(open_set, "remove", current)
		modify_set(closed_set, "add", current)
		neighbors = current.neighbors
		for neighbor in neighbors:

			if neighbor not in closed_set:
				temp_g = current.g +1
				if neighbor in open_set:
					if temp_g < neighbor.g:
						neighbor.g = temp_g
				else:
					neighbor.g = temp_g	
					open_set.append(neighbor)
				# calc heuristic
				neighbor.h = current.calc_heuristic(neighbor)
				neighbor.f = neighbor.g + neighbor.h


		update_grid(show_grid, open_set, closed_set)
		draw_grid(show_grid)
		return True

		






	else:
		print("no solution")

def modify_set(set, action, value):
	if action == "add":
		set.append(value)
	else:
		set.remove(value)

status = True
while status == True:
	status = draw()
	user = raw_input("type in enter")

# modify_set(open_set, "add", start)
# draw()
