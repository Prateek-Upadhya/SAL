class DiDegreeView:

    def __init__(self, G, nbunch=None, weight=None):
        self._graph = G
        self._succ = G._succ if hasattr(G, "_succ") else G._adj
        self._pred = G._pred if hasattr(G, "_pred") else G._adj
        self._nodes = self._succ if nbunch is None else list(G.nbunch_iter(nbunch))
        self._weight = weight

    def __call__(self, nbunch=None, weight=None):
        if nbunch is None:
            if weight == self._weight:
                return self
            return self.__class__(self._graph, None, weight)
        try:
            if nbunch in self._nodes:
                if weight == self._weight:
                    return self[nbunch]
                return self.__class__(self._graph, None, weight)[nbunch]
        except TypeError:
            pass
        return self.__class__(self._graph, nbunch, weight)

    def __getitem__(self, n):
        weight = self._weight
        succs = self._succ[n]
        preds = self._pred[n]
        if weight is None:
            return len(succs) + len(preds)
        return sum(dd.get(weight, 1) for dd in succs.values()) + sum(
            dd.get(weight, 1) for dd in preds.values()
        )

    def __iter__(self):
        weight = self._weight
        if weight is None:
            for n in self._nodes:
                succs = self._succ[n]
                preds = self._pred[n]
                yield (n, len(succs) + len(preds))
        else:
            for n in self._nodes:
                succs = self._succ[n]
                preds = self._pred[n]
                deg = sum(dd.get(weight, 1) for dd in succs.values()) + sum(
                    dd.get(weight, 1) for dd in preds.values()
                )
                yield (n, deg)

    def __len__(self):
        return len(self._nodes)

    def __str__(self):
        return str(list(self))

    def __repr__(self):
        return f"{self.__class__.__name__}({dict(self)})"


class Degree(DiDegreeView):
    def __getitem__(self, n):
        weight = self._weight
        nbrs = self._succ[n]
        if weight is None:
            return len(nbrs) + (n in nbrs)
        return sum(dd.get(weight, 1) for dd in nbrs.values()) + (
            n in nbrs and nbrs[n].get(weight, 1)
        )

    def __iter__(self):
        weight = self._weight
        if weight is None:
            for n in self._nodes:
                nbrs = self._succ[n]
                yield (n, len(nbrs) + (n in nbrs))
        else:
            for n in self._nodes:
                nbrs = self._succ[n]
                deg = sum(dd.get(weight, 1) for dd in nbrs.values()) + (
                    n in nbrs and nbrs[n].get(weight, 1)
                )
                yield (n, deg)
