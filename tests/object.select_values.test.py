from foba.objects import Point

from veho.object import select_values

point = Point(3, 4, 'a')
id, x, y, username, other = select_values(point, 'id', 'x', 'y', 'username', 'other')
print(id, x, y, username, other)
