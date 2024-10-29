#!/usr/bin/env python3
"""a catching system with no limit"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """You must use self.cache_data"""

    def put(self, key, item):
        """Assign to the dictionary the value of the key"""

        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Return the value in self.cache_daya linked to key"""

        return self.cache_data.get(key, None)
