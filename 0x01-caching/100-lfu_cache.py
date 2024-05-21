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
        self.frequency = {}

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.frequency[key] += 1
            else:
                self.frequency[key] = 1

            # Call LRU put method to manage the cache and order list
            super().put(key, item)

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # Find the least frequently used items
                min_freq = min(self.frequency.values())
                lfu_keys = [k for k, v in self.frequency.items() if v == min_freq]

                if len(lfu_keys) > 1:
                    for k in self.order:
                        if k in lfu_keys:
                            lfu_key = k
                            break
                else:
                    lfu_key = lfu_keys[0]

                del self.cache_data[lfu_key]
                del self.frequency[lfu_key]
                self.order.remove(lfu_key)
                print(f"DISCARD: {lfu_key}")

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None
