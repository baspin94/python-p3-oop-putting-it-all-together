#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size = 0, condition="New"):
        self.brand = brand
        self._size = size
        self.condition = condition

    def get_size(self):
        return self._size

    def set_size(self, size):
        if type(size) == int:
            self._size = size
        else:
            print("size must be an integer.")

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")

    size = property(get_size, set_size)