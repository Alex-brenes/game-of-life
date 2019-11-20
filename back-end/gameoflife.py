# gameoflife.py
# Author: José Alexander Brenes Brenes
# Description: ......

from array import *

class GameOfLife:
    def __init__(self, size = 10):
        self.__size = size
        self.__array = [i[:] for i in [[0] * size] * size]
