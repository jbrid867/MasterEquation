import numpy as np
import numpy.random as npr
import scipy.stats as stats
from collections import deque
import copy


class PointError(ValueError):
    pass


class Point:
    def __init__(self, data, time=0.0):
        self.point = (data, time)
        self.value = data
        self.t = time
        self.next = None

    def __repr__(self):
        return repr(self.value)

    def __add__(self, other):
        try:
            return self.value+other.value
        except:
            return self.value+other
    def __iadd__(self, other):
        ## replace current with temp
        tmp1=Point(self.value,self.t)
        tmp1=self.next
        ## insert intermediary for step-like behavior
        tmp2=Point(self.value,self.t+other.t)
        tmp2.next=tmp1
        ## incremement and attach self
        self.value=self.value+other.value
        self.t=self.t+other.t
        self.next=tmp2
        return self
    def push_back(self,data,t):
        iadd(self, Point(data,t))
    def __radd__(self, other):
        return self.__add__(other)

    def __getitem__(self, key):
        if key == 't' or key == 'time' or key == 'Time' or key == 'T':
            return self.t
        if key == 'value' or key == 'val' or key == 'Val' or key == 'Value':
            return self.value

    def __setitem__(self, key, val):
        if key == 't' or key == 'time' or key == 'Time' or key == 'T' or key == 1:
            self.t = val
        if key == 'value' or key == 'val' or key == 'Val' or key == 'Value' or key == 0:
            self.value = val
    def __iter__(self):
        next_point=self.next
        while next_point is not None:
            yield next_point
            next_point=next_point.next
    def get_all(self):
        return [(i, i.t) for i in self]
class PointUpdate(Point):
    def __init__(self,data,t):
        super().__init__(data,t)
    def __getitem__(self, key):
        if key == 't' or key == 'time' or key == 'Time' or key == 'T':
            return self.t
        elif key == 'value' or key == 'val' or key == 'Val' or key == 'Value':
            return self.value
        elif key == 'key':
            return 'vt'
# class Population:
#     _ID = 0
#     _counter = 0
#     _archived = []

#     @classmethod
#     def archive(cls, population):
#         cls._archived.append(population)

#     @classmethod
#     def increment(cls):
#         cls._counter += 1
#         cls._ID += 1

#     def __init__(self, point=None):
#         self.head = point
#         self._ID = Population._ID
#         self._index = Population._counter
#         Population._ID_index_map[self._index] = self._ID
#         Population.increment()

#     def __iter__(self):
#         curr = self.head
#         while curr is not None:
#             yield curr
#             curr = curr.next
#     def get_ID(self):
#         return self._ID
#     def push_back(self, point):
#         try:
#             assert(isinstance(point, Point))
#             point.next = self.head
#             self.head = point
#         except:
#             try:
#                 tmp_next = Point(point[0], point[1])
#                 tmp_next.next = self.head
#                 self.head = point
#             except:
#                 print("input to push_back must be Point or container of two elements")
#                 raise PointError

#     def get_all(self):
#         return [(i, i.t) for i in self]

#     def __repr__(self):
#         return repr(self.head.value)

#     def __add__(self, other):
#         return self.head.__add__(other)

#     def __radd__(self, other):
#         return self.head.__add__(other)
#     def __getitem__(self, key):
#         if key == 't' or key == 'time' or key == 'Time' or key == 'T':
#             return self.head['t']
#         if key == 'value' or key == 'val' or key == 'Val' or key == 'Value':
#             return self.head['value']

#     def __setitem__(self, key, val):
#         cur_val=self.head['val']
#         cur_t=self.head['t']
#         try:
#             pnt1=Point(cur_val,cur_t+val[1])
#             pnt2=Point(cur_val+val[0],cur_t+val[1])
#             self.push_back(pnt1)
#             self.push_back(pnt2)
#         except:
#             if key == 't' or key == 'time' or key == 'Time' or key == 'T' or key == 1:
#                 newpnt=Point(cur_val,cur_t+val)
#                 self.push_back(newpnt)
#             elif key == 'value' or key == 'val' or key == 'Val' or key == 'Value' or key == 0:
#                 newpnt=Point(cur_val+val,cur_t)
#     def __iadd__(self, point):

class CompositionVector:
    def __init__(self, point=None):
        if point is not None:
            self.initialized=True
            try:
                self.state=np.array(point)
            except:
                print('gotta fit into a numpy array')
                raise
        else:
            self.initialized=False
    def add_variable(self,point):
        if not self.initialized:
            try:
                self.comp_vector=np.array(point)
                for i in self.comp_vector:
                    print(i.get_ID())
            except:
                print('gotta finnarray')
                raise
        else:
            self.state=np.append(self.state,point)
    def __iter__(self):
        return self
    def __next__(self):
        self.it=0
        while self.it<len(self.state):
            yield state[self.it]
            self.it+=1
def main():
    lst=[0,1,2,3,4,5]
    tlst=[0.0,0.1,0.2,0.3,0.4,0.5]
    points=[(i,j) for i,j in zip(lst,tlst)]
    state=CompositionVector(points)
    for i in state:
        print(i.get_all())

if __name__ == '__main__':
    main()
