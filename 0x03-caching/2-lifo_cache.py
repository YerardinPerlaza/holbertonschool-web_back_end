#!/usr/bin/python3
"""create a class lifocache"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """Lifo caching system"""
    def __init__(self):
        """Initialize"""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """assign to the self-cache_data the item value for the key"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            discard = self.all_keys.pop()
            print("DISCARD: {}".format(discard))
            del self.cache_data[discard]

            self.all_keys.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data to key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
