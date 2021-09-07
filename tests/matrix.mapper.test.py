from veho.matrix.enumerate import iterate

mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]


def fn(x, i, j): print(x, i, j)


iterate(mat, fn)
print(mat)
