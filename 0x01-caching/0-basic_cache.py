#! /usr/bin/env python3
"""BasicCache class module"""
from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """inherits from BaseCaching and is a caching system"""
    def put(self, key, item):
        """adds a memory block to the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """gets a memory block from cache by key"""
        return self.cache_data.get(key, None)
