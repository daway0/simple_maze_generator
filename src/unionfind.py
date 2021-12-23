class UnionFind():

    def __init__(self):
        self.data_list = []

    def __make_new_union(self, id1, id2):
        self.data_list.append([id1])  # initializing parent
        self.data_list[len(self.data_list)-1].append((id1, id2))
        # [[1, (1,6)], [2, (2,3)]]

    def union(self, id1, id2):
        if id1 == id2:
            print('id1 and id2 must be Unequal')
            return False

        if self.data_list == []:
            self.__make_new_union(id1, id2)
            return True

        # make new union
        flag = False
        for union in self.data_list:
            for i, j in union[1:]:
                if len(set([id1, id2, i, j])) < 4:
                    flag = True

        if not flag:
            self.__make_new_union(id1, id2)
            return

        # tekrari
        for union in self.data_list:
            for i, j in union[1:]:
                if len(set([id1, id2, i, j])) == 2:
                    print('tekrari ast!')
                    return

        self.__union_of_unions(id1, id2)
        # merge
        for index in range(len(self.data_list)):
            for i, j in self.data_list[index][1:]:
                if len(set([id1, id2, i, j])) == 3:
                    self.data_list[index].append((id1, id2))
                    return

    def __union_of_unions(self, id1, id2):
        id1_parent = self.__find(id1)
        id2_parent = self.__find(id2)
        if id1_parent == 'not found' or id2_parent == 'not found' or id1_parent == id2_parent:
            return

        for item in self.data_list[id2_parent[1]][1:]:
            self.data_list[id1_parent[1]].append(item)
        self.data_list.pop(id2_parent[1])

    def display_data_list(self):
        
        print(f'Unions: {self.data_list}')

    def __find(self, id):
        for union in self.data_list:
            for i, j in union[1:]:
                if len(set([i, j, id])) == 2:
                    return (union[0], self.data_list.index(union))
        return ('not found')

    def find(self, id1, id2):
        if self.__find(id1) == 'not found':
            return False
        elif self.__find(id1) == self.__find(id2):
            return True
        else:
            return False
    def say_hi(self):
        print ('hello')
""" 
data = UnionFind()
data.union(25, 18)
data.union(18, 1)
data.union(16, 44)
data.union(8, 44)


data.display_data_list()  """
