import math

class pylist:
    def __init__(self):
        self._data = []
        self._size = 0
        self._allocated = 0
    
    def __len__(self):
        return self._size
    
    def _resize(self):
        new_capacity = math.ceil((self._allocated * 125/100) + 4)
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
        self._allocated = new_capacity

    
    def append(self, x):
        if self._allocated == self._size:
            self._resize()
        self._data[self._size] = x
        self._size += 1   

    def __getitem__(self, key):
        if key < 0 and (abs(key)<= self._size):
            key = key + self._size
            return self._data[key]
        elif key <= (self._size - 1):
            return self._data[key]
        else:
            raise IndexError("Index out of bound")
