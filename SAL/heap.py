from heapq import heappop, heappush
from itertools import count

__all__ = ["MinHeap", "BinaryHeap"]


class MinHeap:

    class _Item:
        __slots__ = ("key", "value")

        def __init__(self, key, value):
            self.key = key
            self.value = value

        def __repr__(self):
            return repr((self.key, self.value))

    def __init__(self):
        self._dict = {}


    def __nonzero__(self):
        return bool(self._dict)

    def __bool__(self):
        return bool(self._dict)

    def __len__(self):
        return len(self._dict)

    def __contains__(self, key):
        return key in self._dict

class BinaryHeap(MinHeap):
    def __init__(self):
        super().__init__()
        self._heap = []
        self._count = count()

    def min(self):
        dict = self._dict
        if not dict:
            raise SystemExit("heap is empty")
        heap = self._heap
        pop = heappop
        while True:
            value, _, key = heap[0]
            if key in dict and value == dict[key]:
                break
            pop(heap)
        return (key, value)

    def pop(self):
        dict = self._dict
        if not dict:
            raise SystemExit("heap is empty")
        heap = self._heap
        pop = heappop
        while True:
            value, _, key = heap[0]
            pop(heap)
            if key in dict and value == dict[key]:
                break
        del dict[key]
        return (key, value)

    def get(self, key, default=None):
        return self._dict.get(key, default)

    def insert(self, key, value, allow_increase=False):
        dict = self._dict
        if key in dict:
            old_value = dict[key]
            if value < old_value or (allow_increase and value > old_value):
                heappush(self._heap, (value, next(self._count), key))
                return value < old_value
            return False
        else:
            dict[key] = value
            heappush(self._heap, (value, next(self._count), key))
            return True