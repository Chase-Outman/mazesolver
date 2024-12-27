from point import Point
from line import Line

class Cell():
    def __init__(self,window=None):
        self.left_wall = True
        self.right_wall = True
        self.top_wall = True
        self.bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = window
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2        
        if self.left_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(line, "white")     

        if self.right_wall:
            line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(line, "white")   

        if self.top_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(line)
        else:
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(line, "white")    

        if self.bottom_wall:
            line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(line, "white")            

    def draw_move(self, to_cell, undo=False):
        x_center_self = abs(self._x2 - self._x1) // 2 + self._x1
        y_center_self = abs(self._y2 - self._y1) // 2 + self._y1

        x_center_to_cell = abs(to_cell._x2 - to_cell._x1) // 2 + to_cell._x1
        y_center_to_cell = abs(to_cell._y2 - to_cell._y1) // 2 + to_cell._y1
        fill_color = ""
        if undo:
            fill_color = "gray"
        else:
            fill_color = "red"

        if self._win is None:
            return
        
        self._win.draw_line(Line(Point(x_center_self, y_center_self), Point(x_center_to_cell, y_center_to_cell)), fill_color)
        
        