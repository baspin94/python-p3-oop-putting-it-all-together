#!/usr/bin/env python3
""" import ipdb """

class Book:
    def __init__(self, title, page_count=0):
        self.title = title
        self._page_count = page_count

    def get_count(self):
        return self._page_count
    
    def set_count(self, page_count):
        if type(page_count) == int:
            self._page_count = page_count
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
            

    page_count = property(get_count, set_count)

""" ipdb.set_trace() """