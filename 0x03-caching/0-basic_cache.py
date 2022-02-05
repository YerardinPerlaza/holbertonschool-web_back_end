#!/usr/bin/python3
"""Create a class BasicCache that inherits from BaseCaching"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """caching a system"""
    def put(self, key, item):
        """Assign to the dictionary self.cache_data the item and the key"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """return value in self.cache_data linked to key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
