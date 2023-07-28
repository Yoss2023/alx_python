#!/usr/bin/python3
if __name__ == "__main__":
    def raise_exception():
        raise TypeError("Exception has been raised")
raise_exception = __import__('4-raise_exception').raise_exception

try:
    raise_exception()
except TypeError as te:
    print(te)


