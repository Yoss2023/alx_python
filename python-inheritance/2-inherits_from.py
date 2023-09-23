#!/usr/bin/python3
""" define a function to see if the object is an instance of a class that inherited (directly or indirectly) from the specified class """
def inherits_from(obj, a_class):

    """  Returns:
        bool: True if the object is an instance of a class derived (directly or indirectly) from 'a_class'; otherwise, False."""
    return issubclass(type(obj), a_class)
