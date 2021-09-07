from pyspare import deco, deco_matrix

from veho.matrix.enumerate import iterate
from veho.columns import push_column, pop_column, shift_column, unshift_column

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

column = [10, 20, 30]

unshift_column(matrix, column)
print(deco_matrix(matrix))

column = shift_column(matrix)
print('column', deco(column))
print('matrix', deco_matrix(matrix))

push_column(matrix, column)
print(deco_matrix(matrix))

column = pop_column(matrix)
print('column', deco(column))
print('matrix', deco_matrix(matrix))
