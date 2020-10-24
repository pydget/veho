from foba.matrices.matrix_numbers import matrix_collection
from pyspare import deco

from veho.matrix import transpose

name, matrix = matrix_collection.flop_shuffle()
print(name)
print(matrix)
print(deco([list(x) for x in zip(*matrix)]))
print(transpose(matrix))
