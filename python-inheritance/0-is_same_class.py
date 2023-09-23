#!/usr/bin/python3

"""Define a function that Check if an object is exactly an instance of a specified class."""

def is_same_class(obj, a_class):


    """ it returns True if the object is exactly an instance of the specified class ; otherwise False"""

    return type(obj) is a_class

