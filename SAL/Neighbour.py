from SAL.Primary import Primary

class Neighbour(Primary):
    __slots__ = ()

    def __getitem__(self, name):
        return Primary(self._main[name])

    def copy(self):
        return {n: self[n].copy() for n in self._main}