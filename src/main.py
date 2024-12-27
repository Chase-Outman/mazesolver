from window import Window
from line import Line
from point import Point
from cell import Cell
from maze import Maze

def main():
    num_rows = 16
    num_cols = 16
    x_size = 25
    y_size = 25
    win = Window((num_rows * y_size) + 20, (num_cols * x_size) + 20)

    maze = Maze(10, 10 , num_rows, num_cols, x_size, y_size, win)
    maze.solve()
    win.wait_for_close()

main()