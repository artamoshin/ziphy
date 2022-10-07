from typing import List, Tuple, Dict

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


def to_tree(source: List[Tuple]) -> Dict:
    """
    Строит дерево по списку пар id (id родителя, id потомка),
    где None - id корневого узла.
    """
    def insert(tree, parent, node):
        if parent is None:
            tree[node] = {}
            return True
        if parent in tree:
            tree[parent][node] = {}
            return True
        for subtree in tree.values():
            if subtree and insert(subtree, parent, node):
                return True

    tree = {}
    for parent, node in source:
        if not insert(tree, parent, node):
            raise ValueError(f'wrong parent: {parent}')
    return tree


assert to_tree(source) == expected
