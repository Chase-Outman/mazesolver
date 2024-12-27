import time
import random
from cell import Cell

class Maze():
    def __init__(
            self,
            x1, 
            y1, 
            num_rows,
            num_cols,
            cell_size_x, 
            cell_size_y, 
            win=None
            ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

    def _reset_cells_visited(self):
        for r in range(self.num_rows):
            for c in range(self.num_cols):
                self._cells[r][c].visited = False

    def solve(self):
        return self._solve_r(0,0)

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self.num_rows-1 and j == self.num_cols-1:
            return True
        
        for d in range(4):
            #0 up
            #1 right
            #2 down
            #3 left
            if d == 0 and i-1 >= 0 and not self._cells[i][j].top_wall and not self._cells[i-1][j].visited:
                self._cells[i][j].draw_move(self._cells[i-1][j])
                if self._solve_r(i-1, j):
                    return True
                self._cells[i][j].draw_move(self._cells[i-1][j], True)

            if d == 1 and j+1 <= self.num_cols-1 and not self._cells[i][j].right_wall and not self._cells[i][j+1].visited:
                self._cells[i][j].draw_move(self._cells[i][j+1])
                if self._solve_r(i, j+1):
                    return True
                self._cells[i][j].draw_move(self._cells[i][j+1], True)    

            if d == 2 and i+1 <= self.num_rows-1 and not self._cells[i][j].bottom_wall and not self._cells[i+1][j].visited:
                self._cells[i][j].draw_move(self._cells[i+1][j])
                if self._solve_r(i+1, j):
                    return True
                self._cells[i][j].draw_move(self._cells[i+1][j], True)      

            if d == 3 and j-1 >= 0 and not self._cells[i][j].left_wall and not self._cells[i][j-1].visited:
                self._cells[i][j].draw_move(self._cells[i][j-1])
                if self._solve_r(i, j-1):
                    return True
                self._cells[i][j].draw_move(self._cells[i][j-1], True)        


        return False


    def _break_entrance_and_exit(self):
        self._cells[0][0].top_wall = False
        self._draw_cell(0,0)
        self._cells[self.num_rows-1][self.num_cols-1].bottom_wall = False
        self._draw_cell(self.num_rows-1, self.num_cols-1)

    def _create_cells(self):
        for row in range(self.num_rows):
            cells_row = []
            for col in range(self.num_cols):
                cells_row.append(Cell(self.win))
            self._cells.append(cells_row)

        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        self.x1 + (i * self.cell_size_x)

        top_left_x = self.x1 + (j * self.cell_size_x)
        top_left_y = self.y1 + (i * self.cell_size_y)
        bottom_right_x = top_left_x + self.cell_size_x
        bottom_right_y = top_left_y + self.cell_size_y

        cell = self._cells[i][j]
        cell.draw(top_left_x, top_left_y, bottom_right_x, bottom_right_y)
        self._animate()

    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.05)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            temp = []
            
            temp.append((i, j-1))
            temp.append((i-1, j))
            temp.append((i, j+1))
            temp.append((i+1, j))         
            

            for r, c in temp:                
                if not (r < 0 or c < 0 or r > self.num_rows-1 or c > self.num_cols-1):       
                    if not (self._cells[r][c].visited):
                        to_visit.append((r, c))                                         

            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            
            ran_dir = random.randrange(len(to_visit))
            r,c = to_visit[ran_dir]
            
            if r > i:
                self._cells[i][j].bottom_wall = False
                self._cells[r][c].top_wall = False
            if r < i:
                self._cells[i][j].top_wall = False
                self._cells[r][c].bottom_wall = False     

            if c > j:
                self._cells[i][j].right_wall = False
                self._cells[r][c].left_wall = False  
            if c < j:
                self._cells[i][j].left_wall = False
                self._cells[r][c].right_wall = False  

            self._break_walls_r(r, c)




            

                        

    
    
        