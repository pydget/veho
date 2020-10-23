from pyspare import deco_matrix

from veho.matrix import transpose

rows = [
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3]
]

print(deco_matrix(rows))

print(deco_matrix(transpose(row for row in rows)))
