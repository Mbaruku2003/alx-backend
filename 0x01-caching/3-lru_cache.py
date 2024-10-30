#!/usr/bin/env python3
"""You must discard LRU algorythm."""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """defined the class."""

    def __init__(self):
        """define initialisations."""

        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """adds an item in the cache following LRU."""

        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {lru_key}")
        self.cache_data[key] = item

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        self.cache_data[key]
