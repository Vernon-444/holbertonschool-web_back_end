#!/usr/bin/env python3
"""2-lifo_cache inhearits a
caching class from a base class"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """a lifo cache example"""

    def put(self, key, item):
        """puts into cache, removes first key if cache is full"""
        if not key or not item:
            return

        if len(self.cache_data) == self.MAX_ITEMS:
            last = self.cache_data.popitem()[0]
            print('DISCARD: ' + last)
        self.cache_data[key] = item

    def get(self, key):
        """gets value from cache"""
        if not key or key not in self.cache_data:
            return None
        return self.cache_data[key]
