#! /usr/bin/env python3
"""LIFO module"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """inherits from BaseCaching and follows the LIFO
    (Last-In-First-Out) caching algorithm"""

    def __init__(self):
        """initialise the class"""
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.stack.remove(key)
            self.cache_data[key] = item
            self.stack.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                last_key = self.stack.pop(-2)
                del self.cache_data[last_key]
                print(f"DISCARD: {last_key}")

    def get(self, key):
        """ Get an item in the cache by key"""
        return self.cache_data.get(key, None)
