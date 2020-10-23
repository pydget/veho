from pyspare import deco_vector
from texting import COSP

list_collection = {
    'countries': ['nigeria', 'india', 'nepal', 'pakistan', 'uzbekistan'],
    'alphabets': ['d', 's', 'y', 'a', 'e'],
    'numerics': [3, 1, 5, 7, 2],
}

for (k, v) in list_collection.items():
    print(k, deco_vector(v, delim=COSP))
    v.sort()
    print(k, deco_vector(v, delim=COSP))
    print()
