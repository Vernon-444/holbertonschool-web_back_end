#!/usr/bin/env python3
"""1-fifo_cache inhearits a
caching class from a base class"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """fifo ordered caching"""

    def put(self, key, item):
        """Store to cache"""
        if not key or not item:
            return
        self.cache_data[key] = item

        if len(self.cache_data) > self.MAX_ITEMS:
            first = next(iter(self.cache_data))
            self.cache_data.pop(first)
            print('DISCARD: ' + first)

    def get(self, key):
        """get value from cache"""
        if not key or key not in self.cache_data:
            return None
        return self.cache_data[key]
