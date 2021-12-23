class Grid ():

    def __init__(self, x_row, y_col):
        self.m = y_col
        self.n = x_row
        self.__grid = []
        self.up_down_wall = []
        self.right_left_wall = []
        self.__make_right_left_wall()
        self.__make_up_down_wall()

    def __make_up_down_wall(self):

        for i in range(2*self.m+1):
            if i % 2 == 0:
                self.up_down_wall.append(' ')
            else:
                self.up_down_wall.append('w')

    def __make_right_left_wall(self):

        for i in range(2*self.m+1):
            if i % 2 == 0:
                self.right_left_wall.append('w')
            else:
                self.right_left_wall.append(' ')

    def __id_implementation(self):
        id = 0
        for i in range(1, 2*self.n+1, 2):
            for j in range(1, 2*self.m+1, 2):
                id += 1
                self.__grid[i][j] = id

    def build(self):

        for i in range(2*self.n+1):
            if i % 2 == 0:

                self.__grid.append(self.up_down_wall.copy())  # up down
            else:

                self.__grid.append(self.right_left_wall.copy())  # right left

        self.__id_implementation()

    def display(self):

        for i in range(2*self.n+1):
            display_row = ''
            for j in range(2*self.m+1):
                display_row += f'{str(self.__grid[i][j]):<3}'
            print(display_row)

    def size(self):
        return (self.n, self.m)

    def grid_list(self):
        return self.__grid

    def expand_coordinate(self, index):
        for i in range(2*self.n+1):
            for j in range(2*self.m+1):
                if self.__grid[i][j] == index:
                    return (i, j)

    def cell_wall_counter(self, wall_row, wall_col):
        if wall_row % 2 == 1 and wall_col % 2 == 0:  # vertical
            counter1 = self.count_wall(wall_row, wall_col-1)
            counter2 = self.count_wall(wall_row, wall_col+1)
        if wall_row % 2 == 0 and wall_col % 2 == 1:  # horizontal
            counter1 = self.count_wall(wall_row+1, wall_col)
            counter2 = self.count_wall(wall_row-1, wall_col)
        return (counter1, counter2)

    def count_wall(self, i, j):
        counter = 0
        if self.__grid[i+1][j] == 'w':
            counter += 1
        if self.__grid[i-1][j] == 'w':
            counter += 1
        if self.__grid[i][j+1] == 'w':
            counter += 1
        if self.__grid[i][j-1] == 'w':
            counter += 1
        return counter


""" grid1 = Grid(2, 2)
grid1.build()
grid1.display()
print(grid1.size())
print (grid1.expand_coordinate(4))
print(grid1.cell_wall_counter(2, 2)) """
# doroste in code fqt unjaii ke man zdm counter kone wall nist asln
