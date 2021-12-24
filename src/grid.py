class Grid ():

    # 2*1 grid structure          0   1  2
    #    ___                      __ ___ __
    #   |_1_|   EXPAND TO      0 |__|_w_|__|
    #   |_2_|   w: wall        1 |_w|_1_|_w|
    #                          2 |__|_w_|__|
    #                          3 |_w|_2_|_w|
    #                          4 |__|_w_|__|
    # wall based grid
    #
    def __init__(self, row, col):
        self.__row = row
        self.__col = col
        # ex: expanded
        self.__ex_row = row*2 + 1
        self.__ex_col = col*2 + 1
        self.__grid_data = []
        self.__horizontal_wall = []
        self.__build_horizontal_wall()
        self.__vertical_wall = []
        self.__build_vertical_wall()

    def __build_horizontal_wall(self):

        for i in range(self.__ex_row):
            if i % 2 == 0:
                self.__horizontal_wall.append(' ')
            else:
                self.__horizontal_wall.append('w')

    def __build_vertical_wall(self):

        for i in range(self.__ex_row):
            if i % 2 == 0:
                self.__vertical_wall.append('w')
            else:
                self.__vertical_wall.append(' ')

    def __id_implementation(self):
        id = 0
        for i in range(1, self.__ex_col, 2):
            for j in range(1, self.__ex_row, 2):
                id += 1
                self.__grid_data[i][j] = id

    def build(self):

        for i in range(self.__ex_col):
            if i % 2 == 0:

                self.__grid_data.append(
                    self.__horizontal_wall.copy())  # append horizontal
            else:

                self.__grid_data.append(
                    self.__vertical_wall.copy())  # append vertical

        self.__id_implementation()

    def display(self):

        for i in range(self.__ex_col):
            display_row = ''
            for j in range(self.__ex_row):
                display_row += f'{str(self.__grid_data[i][j]):<3}'
            print(display_row)

    def size(self):
        return (self.__col, self.__row)

    def grid_list(self):  # expose structure !!
        return self.__grid_data

    def expand_coordinate(self, index):  # expose structure !!
        for i in range(self.__ex_col):
            for j in range(self.__ex_row):
                if self.__grid_data[i][j] == index:
                    return (i, j)

    def cell_wall_counter(self, wall_row, wall_col):  # kind a expose !!
        if wall_row % 2 == 1 and wall_col % 2 == 0:  # vertical
            counter1 = self.__count_wall(wall_row, wall_col-1)
            counter2 = self.__count_wall(wall_row, wall_col+1)
        if wall_row % 2 == 0 and wall_col % 2 == 1:  # horizontal
            counter1 = self.__count_wall(wall_row+1, wall_col)
            counter2 = self.__count_wall(wall_row-1, wall_col)
        return (counter1, counter2)

    def __count_wall(self, i, j):
        counter = 0
        if self.__grid_data[i+1][j] == 'w':
            counter += 1
        if self.__grid_data[i-1][j] == 'w':
            counter += 1
        if self.__grid_data[i][j+1] == 'w':
            counter += 1
        if self.__grid_data[i][j-1] == 'w':
            counter += 1
        return counter

# Grid() input validation will be check in Game() in game.py
# 
# how it works:
#
#
# grid = Grid(6, 3)
# grid.build()
# grid.display()
