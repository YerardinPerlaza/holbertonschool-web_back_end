#!/usr/bin/python3
"""Create a class BasicCache that inherits from BaseCaching"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """caching a system"""


    def put(self, key, item):
        """Assign to the dictionary self.cache_data the item and the key"""
        if (key and item):
            self.cache_data[key] = item


    def get(self, key):
        """return value in self.cache_data linked to key"""
        if key:
            for k in self.cache_data.keys():
                if key == k:
                    return self.cache_data.get(key)
        return None
        
