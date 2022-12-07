from collections.abc import Mapping


class Primary(Mapping):
    __slots__ = ("_main",)

    def __getstate__(self):
        return {"_main": self._main}

    def __setstate__(self, state):
        self._main = state["_main"]

    def __init__(self, d):
        self._main = d

    def __len__(self):
        return len(self._main)

    def __iter__(self):
        return iter(self._main)

    def __getitem__(self, key):
        return self._main[key]

    def copy(self):
        return {n: self[n].copy() for n in self._main}

    def __str__(self):
        return str(self._main)

    def __repr__(self):
        return f"{self.__class__.__name__}({self._main!r})"