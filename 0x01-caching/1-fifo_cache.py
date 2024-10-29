#!/usr/bin/env python3
"""Create a class FIFOCache that inherits from BaseCaching"""
from base_caching import BaseCaching


def FIFOCache(BaseCaching):
    """You can overload def __init__(self)."""

    def __init__(self):
        """overload but dont forget to call parent init."""

        super().__init__()
        self.keys_order = []

    def put(self, key, item):
        """Must assign to the dictionary self.cache_data the item ."""

        if key is None or item is None:
            return
        # add or update cache with the new_data
        self.cache_data[key] = item
        # if key is already in the order_list remove it to update its position
        if key in self.keys_order:
            self.keys_order.remove(key)
        # add key to the end of order list
        self.keys_order.append(key)
        # check if we exceed the maximum cache size
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # FIFO remove first item first
            oldest_key = self.keys_order.pop(0)
            del self.cache_data[oldest_key]
            print(f"DISCARD: {oldest_key}")

    def get(self, key):
        """Get an item by key"""

        return self.cache_data.get(key, None)
