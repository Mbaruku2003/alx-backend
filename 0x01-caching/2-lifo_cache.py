#!/usr/bin/env python3
"""Discards last item put in cach LIFO."""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """class inherits from BaseCaching."""

    def __init__(self):
        """ initialistion."""

        super().__init__()
        self.keys_order = []

    def put(self, key, item):
        """discards the last item using Lifo algorythm."""

        if key is None and item is None:
            return
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key = self.keys_order.pop()
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")
        self.cache_data[key] = item
        if key in self.keys_order:
            self.keys_order.remove(key)
        self.keys_order.append(key)

    def get(self, key):
        """retreive an item fom a cache."""

        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
