class UnionFind():
    def __init__(self):
        self.__data = []
        # [[1, {1,2,3}],
        #  [5, {12,10,5}],
        #  [45, {45,6,9,7}]
        #
        # 1,5,45 are parents of unions

    def __make_new_union(self, id1, id2):
        self.__data.append([id1])  # appending parent

        union_set = set()
        union_set.add(id1)
        union_set.add(id2)

        last_union_index = len(self.__data)-1
        self.__data[last_union_index].append(union_set)

    def union(self, id1, id2):
        # first union
        if self.__data == []:
            self.__make_new_union(id1, id2)
            return True

        # id1 == id2
        if id1 == id2:
            return False

        self.__union_of_unions(id1, id2)
        # make new union,merge
        duplicate = 0
        for union in self.__data:
            for set_ in union[1:]:  # [1, {1,2,3,4}]
                if id1 in set_ or id2 in set_:
                    index = self.__data.index(union)
                    self.__data[index][1].add(id1)
                    self.__data[index][1].add(id2)
                    duplicate = 1
        if not duplicate:
            self.__make_new_union(id1, id2)
            return True

    def __union_of_unions(self, id1, id2):

        parent_1 = self.__find(id1)
        parent_2 = self.__find(id2)

        if not parent_1 or not parent_2 or parent_2==parent_1:
            return
        
        for item in self.__data[parent_2[1]][1:]:
          for id in item: 
            self.__data[parent_1[1]][1].add(id)
        self.__data.pop(parent_2[1])

    def display_data_list(self):
        print(f'Unions: {self.__data}')

    def __find(self, id):
        for union in self.__data:
            for set_ in union[1:]:
                if id in set_:
                    return (union[0], self.__data.index(union))
        return False

    def find(self, id1, id2):
        parent_1 = self.__find(id1)
        parent_2 = self.__find(id2)
        if not parent_1 or not parent_2:  # not found check
            return False
        if parent_1 == parent_2:
            return True

""" 
uf = UnionFind()   #1,2,3   4,5,6   7,8,9
uf.union(1, 2)
uf.union(3, 1)

uf.union(4, 5)
uf.union(5, 6)

uf.union(7, 8)
uf.union(7,9)

uf.union(8,8)
uf.union(7, 8)
uf.union(4, 5)
uf.union(4, 1)
uf.union(1, 4)
uf.union(1, 4)
uf.union(7, 4)
uf.display_data_list()
 """