import time
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
            win
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
        self.win.redraw()
        time.sleep(0.05)
    
    
        