#!/usr/bin/env python3
"""well create a class to implement mru."""
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """created the new class."""

    def __init__(self):
        """we will do attribute initialisation."""

        super().__init__()
        self.cache_data = OrderedDict

    def put(self, key, item):
        """we will load values into the key."""

        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key, _ = self.cache_data.popitem(last=True)
            print(f"DISCARD: {mru_key}")
        self.cache_data[key] = item

    def get(self, key):
        """retreive an item and mark it as most recently ised."""

        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
