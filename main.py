#!/usr/bin/python3

class Number:
    """Class that represents a number in an arbitrary base"""

    
    def __init__(self):
        self.number_string = ""
        self.number_base = 0
        
    def __init__(self, number_string, number_base):
        self.number_string = number_string
        self.number_base = number_base
        
    