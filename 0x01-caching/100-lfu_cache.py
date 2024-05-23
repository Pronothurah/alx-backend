#!/usr/bin/env python3
""" LFUCache module """
from base_caching import BaseCaching
LRUCache = __import__('3-lru_cache').LRUCache


class LFUCache(LRUCache):
    """inherits from LRUCache and follows the LFU
    (Least Frequently Used) caching algorithm"""

    def __init__(self):
        """ Initialize the class """
        super().__init__()
        self.usage_frequency = {}
        self.usage_order = {}

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.usage_frequency[key] += 1
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the least frequently used key
                min_freq = min(self.usage_frequency.values())
                lfu_keys = [k for k, v in self.usage_frequency.items() if v == min_freq]

                if len(lfu_keys) > 1:
                    # Find the least recently used key among the least frequently used keys
                    lru_key = min(lfu_keys, key=lambda k: self.usage_order[k])
                else:
                    lru_key = lfu_keys[0]

                del self.cache_data[lru_key]
                del self.usage_frequency[lru_key]
                del self.usage_order[lru_key]
                print(f"DISCARD: {lru_key}")

            self.cache_data[key] = item
            self.usage_frequency[key] = 1

        # Update the order of usage for LRU tie-breaking
        self.usage_order[key] = self._current_time()

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None

        self.usage_frequency[key] += 1
        self.usage_order[key] = self._current_time()
        return self.cache_data[key]

    def _current_time(self):
        """ Return the current time in milliseconds to ensure unique ordering """
        from time import time
        return int(time() * 1000)
