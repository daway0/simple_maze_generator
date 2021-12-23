from PIL import Image, ImageFont, ImageDraw
from grid import Grid
from rect import Rectangle
from unionfind import UnionFind
from numpy import random

""" import sys
sys.stdout = open('output.txt', 'w') """


class Game():
    def __init__(self, grid_row, grid_col, rectangle, start_cell, end_cell):

        # Atts
        self.__start = start_cell
        self.__end = end_cell
        self.__grid = Grid(grid_row, grid_col)
        self.__grid.build()
        self.__rectangle = rectangle
        self.whiteboard = None
        self.__init_inside_wall = (grid_row-1)*grid_col + (grid_col-1)*grid_row
        self.inside_wall = self.__init_inside_wall
        self.cell_union = UnionFind()
        self.remove_edge_wall()
        self.cell_union.union(start_cell, -1)  # virtual start
        self.cell_union.union(end_cell, -2)  # virtual end
        self.last_wall = None

    def remove_edge_wall(self):
        start_row, start_col = self.__grid.expand_coordinate(self.__start)
        end_row, end_col = self.__grid.expand_coordinate(self.__end)
        x, y = self.__find_edge_wall(start_row, start_col)
        self.__grid.grid_list()[x][y] = 0
        x, y = self.__find_edge_wall(end_row, end_col)
        self.__grid.grid_list()[x][y] = 0

    def __find_edge_wall(self, index_row, index_col):
        if index_row == 1:
            return (index_row-1, index_col)
        elif index_row == len(self.__grid.grid_list())-2:
            return (index_row+1, index_col)
        elif index_col == 1:
            return (index_row, index_col-1)
        elif index_col == len(self.__grid.grid_list()[0])-2:
            return (index_row, index_col+1)

    def build_whiteboard(self, wb_color='white'):
        self.__grid_row, self.__grid_col = self.__grid.size()
        self.rect_width, self.rect_height = self.__rectangle.size()
        if self.rect_width < self.rect_height:  # width always > height
            self.rect_width, self.rect_height = self.rect_height, self.rect_width
        # whiteboard : wb

        wb_width = self.rect_width * self.__grid_col + self.rect_height
        wb_height = self.rect_width * self.__grid_row + self.rect_height
        whiteboard = Image.new('RGB', (wb_width, wb_height), color=wb_color)
        self.whiteboard = whiteboard
        return whiteboard

    def draw_maze(self):

        # whiteboard : wb
        wb_width = self.whiteboard.size[0]
        wb_height = self.whiteboard.size[1]
        grid = self.__grid.grid_list()

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i % 2 == 0 and j % 2 == 1:  # horizontal
                    if not (grid[i][j] == 'w'):  # no wall
                        if grid[i][j] == -3:
                            rect_last = Rectangle(
                                self.rect_width, self.rect_height, 'red')
                            print('hello1')
                            x = (self.rect_height/2) + (j)/2 * \
                                ((wb_width-self.rect_height) /
                                 ((len(grid[i])-1)/2))
                            y = (self.rect_width/2) + (i-1)/2 * \
                                ((wb_height-self.rect_height) / ((len(grid)-1)/2))

                            rect_last.draw((x, y), self.whiteboard)
                        continue

                    x = (self.rect_width/2) + (j-1)/2 * \
                        (wb_width / ((len(grid[i])-1)/2))
                    y = (self.rect_height/2) + (i)/2 * \
                        ((wb_height-self.rect_height) / ((len(grid)-1)/2))
                    self.__rectangle.draw((x, y), self.whiteboard)

        self.__rectangle.swap_height_width()

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i % 2 == 1 and j % 2 == 0:  # vertical
                    if not (grid[i][j] == 'w'):  # no wall
                        if grid[i][j] == -3:
                            rect_last = Rectangle(
                                self.rect_height, self.rect_width, 'red')
                            print('hello')
                            x = (self.rect_height/2) + (j)/2 * \
                                ((wb_width-self.rect_height) /
                                 ((len(grid[i])-1)/2))
                            y = (self.rect_width/2) + (i-1)/2 * \
                                ((wb_height-self.rect_height) / ((len(grid)-1)/2))

                            rect_last.draw((x, y), self.whiteboard)
                        continue

                    x = (self.rect_height/2) + (j)/2 * \
                        ((wb_width-self.rect_height) / ((len(grid[i])-1)/2))
                    y = (self.rect_width/2) + (i-1)/2 * \
                        ((wb_height-self.rect_height) / ((len(grid)-1)/2))

                    self.__rectangle.draw((x, y), self.whiteboard)
                # PRINT E id kamelan ru hava va cheshmi set shode, (baraye debug e union find)
                elif i % 2 == 1 and j % 2 == 1:
                    # +1/3 self.width uptional e
                    x = (self.rect_height/2) + (j)/2 * \
                        ((wb_width-self.rect_height) /
                         ((len(grid[i])-1)/2))-0.3*self.rect_width
                    y = (self.rect_width/2) + (i-1)/2 * \
                        ((wb_height-self.rect_height) /
                         ((len(grid)-1)/2)) - 0.3*self.rect_width
                    # self.__print_id(str(grid[i][j]), x, y)

    def __print_id(self, id, x_axis, y_axis):  # id is string
        draw = ImageDraw.Draw(self.whiteboard)
        font = ImageFont.truetype(font="arial.ttf", size=self.rect_width - 10)
        draw.text((x_axis, y_axis), id, (255, 255, 255), font=font)

    def remove_wall_uniform(self, percentage=0):  # wall remove percentage
        grid = self.__grid.grid_list()
        # while (self.inside_wall / self.__init_inside_wall)*100 > (100-percentage):
        while not(self.cell_union.find(-1, -2)):

            row = int(random.uniform(1, len(grid)-1, None))
            col = int(random.uniform(1, len(grid[0])-1, None))
            self.__remove_wall(row, col)
        self.__grid.grid_list()[row][col] = -3  # last_wall

        # print (f'{row} {col}')

    def __remove_wall(self, row, col):
        grid = self.__grid.grid_list()
        if grid[row][col] != 'w':
            return False

        # difficulaity
        if self.__grid.cell_wall_counter(row, col)[0] <= 2 or self.__grid.cell_wall_counter(row, col)[1] <= 2:
            print("False")
            return False
        print("===>True")
        self.union_cells(row, col)
        grid[row][col] = 0
        self.inside_wall -= 1

    def union_cells(self, wall_row, wall_col):
        # check horizontal or vertical

        grid = self.__grid.grid_list()  # fcking expose
        if wall_row % 2 == 0:  # horizontal wall
            self.cell_union.union(grid[wall_row-1][wall_col],
                                  grid[wall_row+1][wall_col])
        elif wall_row % 2 == 1:  # vertical wall
            self.cell_union.union(grid[wall_row][wall_col-1],
                                  grid[wall_row][wall_col+1])


rect = Rectangle(20, 2, '#555555')
game = Game(20, 20, rect, 21, 380)
game.build_whiteboard('black')
game.remove_wall_uniform(50)
game.draw_maze()
game.whiteboard.show()
game.whiteboard.save('./asar_honary.png')
