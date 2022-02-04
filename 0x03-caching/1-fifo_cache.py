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
        if (key and item):
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            if len(self.keys) > self.MAX_ITEMS:
                out = self.keys.pop(0)
                del self.cache_data[out]
                print('DISCAR: {}'.format(out))

    def get(self, key):
        """return the value in self.cache_data to key"""
        if key and key in self.keys:
            return self.cache_data[key]
        return None
