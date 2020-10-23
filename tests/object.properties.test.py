from math import sqrt

from foba.objects import Point
from pyspare import deco

from veho.object import entries, keys, values, to_dict

o = Point(3, 4, 'a')


class SlotPoint:
    __slots__ = 'x', 'y', 'tag'

    def __init__(self, x, y, tag):
        self.x = x
        self.y = y
        self.tag = tag

    @property
    def distance(self):
        return sqrt(self.x ** 2 + self.y ** 2)


candidates = {
    'point': Point(3, 4, 'a'),
    'dict_point': {'x': 3, 'y': 4, 'tag': 'b'},
    'slot_point': SlotPoint(6, 8, 'c'),
    'vector': ['a', 'b', 'c'],
    'string': 'shakes',
    'number': 127,
}

for name, o in candidates.items():
    print(name)
    print(type(o))
    # print('dir', deco(dir(o)))
    # if hasattr(o, '__dict__') or hasattr(o, '__slots__'): print('vars', deco_dict(vars(o)))
    # if hasattr(o, '__dict__'): print('__dict__', deco_dict(o.__dict__))
    # if hasattr(o, '__slots__'): print('__slots__', deco_dict({s: getattr(o, s) for s in o.__slots__}))
    # print('inspect.getmembers', deco_entries(inspect.getmembers(o)))
    print(deco(to_dict(o)))
    print()
