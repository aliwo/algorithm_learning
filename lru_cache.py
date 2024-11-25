from collections import OrderedDict
from typing import Any


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: str | int, default: Any = None) -> Any:
        if key not in self.cache:
            return default
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

    def set(self, key: str | int, value: Any) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


if __name__ == "__main__":
    cache = LRUCache(2)
    cache.set("a", 1)
    cache.set(1, "hihi")
    assert cache.get("a") == 1
    assert cache.get("b") == None
    assert cache.get(1) == "hihi"
    print("All tests passed")