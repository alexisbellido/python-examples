import time

class Store:

    _store = {}
    VALUE   = 0
    EXPIRES = 1

    @classmethod
    def get(cls, key):
        """
        Get the value for a key, assuming it hasn't expired.
        """
        try:
            if cls._store[key][cls.EXPIRES] > time.time():
                return cls._store[key][cls.VALUE]
            else:
                del cls._store[key] # Delete the item if it has expired
                return None
        except KeyError:
            return None

    @classmethod
    def set(cls, key, value, duration=3600):
        """
        Store or update value for a key with an expiry duration in seconds.
        """
        try:
            expires = time.time() + duration
        except TypeError:
            raise TypeError("Duration must be numeric")

        cls._store[key] = (value, expires)
        return cls.get(key)

    @classmethod
    def clean(cls):
        """Remove all expired items from the cache"""
        for key in cls._store.keys():
            print(key)
            # cls.get(key) # Attempting to fetch an expired item deletes it


    @classmethod
    def purge(cls):
        """Remove all items from the cache"""
        cls._store = {}
