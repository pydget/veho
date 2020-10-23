from veho.entries.unwind import unwind

candidates = {
    'empty': [],
    'empty_2': [()],
    'empty_3': [(None,)],
    'simple': [(1, 2), (3, 4), (8, 9)],
}

for key, entries in candidates.items():
    print(key)
    print(unwind(entries))
