## open_set =  op_set
## closed_set = cl_set
## start_loc = start_location

import cell

class AStar(object):

    def __init__(self, start_loc, destination_loc, grid):
        self.path = []
        self.open_set = []
        self.closed_set = []
        self.grid = grid
        self.start_loc = self.set_start_loc(start_loc)
        self.destination_loc = self.set_end_loc(destination_loc)
        self.lowest_f_val_idx = -1
        self.current_set = ""
        self.open_set.append(self.start_loc)

    def run_calc(self):
        if self.op_set_not_empty():
            self.set_lowest_f_val_idx(0)               
            self.check_for_lowest_f_val()
            self.set_current_set()
            if self.current_on_destination() == True:
                self.find_path()
                return len(self.path)-1
            self.transfer_current_to_closed()
            neighbors = self.currents_neighbors()
            self.neighbor_logic(neighbors)
            return True
        else:
            return False

    def assign_current_set(self):
        self.current_set = open_set[self.lowest_f_val_idx]
        
    def cell_has_new_lower_g_val(self, set_cell, comparision_val):
        return (comparision_val < set_cell.g)

    def check_for_lowest_f_val(self):
        for idx, set in enumerate(self.open_set):
            if set.f < self.open_set[self.lowest_f_val_idx].f:
                self.set_lowest_f_val_idx(idx)
                
    def current_on_destination(self):
        return self.open_set[self.lowest_f_val_idx]== self.destination_loc
        
    def currents_neighbors(self):
        return self.current_set.neighbors

    def find_path(self):
        temp = self.current_set
        self.path.append(temp)
        while temp.previous:
            self.path.append(temp.previous)
            temp = temp.previous

    def neighbor_in_op_set(self, neigbor):
        return (neigbor in self.open_set)
            
    def neighbor_logic(self, neighbors):
        for neighbor in neighbors:
            if self.neighbor_not_in_cl_set(neighbor):
                self.set_neighbor_values(neighbor)

    def neighbor_not_in_cl_set(self, neighbor):
        return (neighbor not in self.closed_set)
        
    def op_set_not_empty(self):
        return (len(self.open_set) > 0)
        
    def set_cell_g_val(self, cell, value):
        cell.g = value

    def set_current_set(self):
        self.current_set = self.open_set[self.lowest_f_val_idx]

    def reset_lowest_f_val_idx(self):
        self.lowest_f_val_idx = 0


    def set_lowest_f_val_idx(self, value):
        self.lowest_f_val_idx = value

    def set_neighbor_f_val(self,neighbor):
        neighbor.f = neighbor.g + neighbor.h

    def set_neighbor_g_val(self, neighbor):
        temp_g = self.current_set.g+1
        if self.neighbor_in_op_set(neighbor):
            if self.cell_has_new_lower_g_val(neighbor, temp_g):
                self.set_cell_g_val(neighbor, temp_g)
        else:
            self.set_cell_g_val(neighbor, temp_g)
            self.open_set.append(neighbor)

    def set_neighbor_h_val(self,neighbor):
        dist = self.current_set.calc_heuristic(neighbor)
        neighbor.h = dist    

    def set_neighbor_previous(self, neighbor):
        neighbor.previous = self.current_set

    def set_neighbor_values(self, neighbor):
        self.set_neighbor_g_val(neighbor)
        self.set_neighbor_h_val(neighbor)
        self.set_neighbor_f_val(neighbor)
        self.set_neighbor_previous(neighbor)

    def set_end_loc(self, end_yx):
        y = end_yx[0]
        x = end_yx[1]
        return self.grid[y][x]       

    def set_start_loc(self, start_yx):
        y = start_yx[0]
        x = start_yx[1]
        return self.grid[y][x]


    def transfer_current_to_closed(self):
        self.closed_set.append(self.current_set)
        self.open_set.remove(self.current_set)





