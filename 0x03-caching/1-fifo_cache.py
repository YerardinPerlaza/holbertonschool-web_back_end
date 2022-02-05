#!/usr/bin/python3
""" create a class fifocache"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """Fifo caching system"""
    def __init__(self):
        """Initialize"""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """assign to the self-cache_data the item value for the key"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            out = self.keys.pop(0)
            print('DISCAR: {}'.format(out))
            del self.cache_data[out]

        self.keys.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data to key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
