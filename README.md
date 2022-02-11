# build-tree

The test tasks with an interesting algorithm by creation tree structure

Write a function that builds a tree using a list of id pairs (parent id, descendant id), where None is the id of the root node.

Input data:
```
source = [
    (None, 'a'),
    (None, 'b'),
    (None, 'c'),
    ('a', 'a1'),
    ('a', 'a2'),
    ('a2', 'a21'),
    ('a2', 'a22'),
    ('b', 'b1'),
    ('b1', 'b11'),
    ('b11', 'b111'),
    ('b', 'b2'),
    ('c', 'c1'),
]

expected = {
    'a': {'a1': {}, 'a2': {'a21': {}, 'a22': {}}},
    'b': {'b1': {'b11': {'b111': {}}}, 'b2': {}},
    'c': {'c1': {}},
}

assert to_tree(source) == expected
```
