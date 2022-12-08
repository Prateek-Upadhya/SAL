from collections.abc import Mapping, Set

class NodeView(Mapping, Set):
    __slots__ = ("_nodes",)
    def __init__(self, graph):
        self._nodes = graph._node

    # Mapping methods
    def __len__(self):
        return len(self._nodes)

    def __iter__(self):
        return iter(self._nodes)

    def __getitem__(self, n):
        if isinstance(n, slice):
            raise Exception(
                f"{type(self).__name__} does not support slicing, "
            )
        return self._nodes[n]



   