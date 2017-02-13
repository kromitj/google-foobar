import math


# globals
# these are going to go in a Board Class,exept path which
# will go in the AStar class
cols = 8
rows = 8
cell_num = 0
grid = [[0 for x in range(cols)] for y in range(rows)]
path = False


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
		# self.get_attrs = {"x": self.x, "y": self.y, "f: self.f, "g": self.g, "h": self.h, "val": self.val}
	
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


# global functions 
# should be put into a class
# i think Board class
def grid_path(paths, grid):
	for col in range(cols):
		for row in range(rows):
			grid[col][row] = " "
	for path in paths:
		grid[path.y][path.x] = "$"

def update_grid(grid, open, closed):
	for set in open:
		grid[set.y][set.x] = "@"
	for set in closed:
		grid[set.y][set.x] = "*"

def draw_grid(grid):
	for row in show_grid:
		print(row)
		
		

# setup
# these two for loop seed the grid array
# these could go into the Board class as well
for col in range(cols):
	for row in range(rows):
		grid[col][row] = Cell(row, col ,cell_num)
		cell_num+=1

for col in range(cols):
	for row in range(rows):
		grid[col][row].find_valid_neighbors(grid)

# these can go in a AStar class 
# Astar will hold data needed for the algorithm
# so , open_set, closed_set, start, end
# show grid will go in Board class
open_set = []
closed_set = []
start = grid[2][3]
end = grid[4][4]
show_grid = [[" " for x in range(cols)] for y in range(rows)]
open_set.append(start)

def draw():
	# This func will go into the AStar class

	print("_______________________________________")
	if len(open_set) > 0:
		lowest_f_val = 0
		for i in range(len(open_set)):
			if open_set[i].f < open_set[lowest_f_val].f:
				lowest_f_val = i
		current = open_set[lowest_f_val]
		if open_set[lowest_f_val] == end:
			path = []
			temp = current
			path.append(temp)
			while temp.previous:
				path.append(temp.previous)
				temp = temp.previous
			grid_path(path, show_grid)
			print("you handed on the squajhjghjghre")
			print("_________________________________")
			draw_grid(show_grid)

			return len(path)
		modify_set(open_set, "remove", current)
		modify_set(closed_set, "add", current)
		neighbors = current.neighbors
		for neighbor in neighbors:

			if neighbor not in closed_set:
				temp_g = current.g+1
				if neighbor in open_set:
					if temp_g < neighbor.g:
						neighbor.g = temp_g
				else:
					neighbor.g = temp_g	
					open_set.append(neighbor)
				neighbor.h = current.calc_heuristic(neighbor)
				neighbor.f = neighbor.g + neighbor.h
				neighbor.previous = current
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
print status-1



