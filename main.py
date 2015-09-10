#!/usr/bin/python3


class Number:
    """Class that represents a number in an arbitrary base"""
    
    class BaseError(Exception):
        def __init__(self, number, failed_char, base):
            self.value = [number, failed_char, base]
        
        def __str__(self):
            return repr(self.value)

    def insert_number(self, number, base):
        verify_number(number, base)
        self.number_string = number
        self.number_base = base
        
    def __init__(self):
        self.number_string = ""
        self.number_base = 0
        
    def __init__(self, number_string, number_base):
        
        
    def get_in_base(self, base):
        print("heheheh")
        
    def verify_number(self, number, base):
        for character in number:
            n = char_to_digit(character)
            if n >= base:
                raise BaseError(number, n, base)
    
    def char_to_digit(char):
        if char.isdigit():
            return int(ord(char)-ord("0"))
        else:
            return int(ord(char) + 10 - ord("a"))
            
