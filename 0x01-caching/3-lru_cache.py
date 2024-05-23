#!/usr/bin/env python3
""" LRUCache module """
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """inherits from BaseCaching and follows the LRU
    (Least Recently Used) caching algorithm"""

    def __init__(self):
        """ Initialize the class """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.order.remove(key)
            self.cache_data[key] = item
            self.order.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                least_recent_key = self.order.pop(0)
                del self.cache_data[least_recent_key]
                print(f"DISCARD: {least_recent_key}")

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
