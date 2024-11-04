from redis import Redis, RedisError
from typing import Any, Optional


class CacheManager:

    # def __init__(self):
    #     self.cache = Redis(host="redis", port=6379, db=1)
    def __init__(self, host: str = "localhost", port: int = 6379, db: int = 0):
        # Initializing cache connection
        self.cache = Redis(host=host, port=port, db=db)

    # def get_value(self, key: str):
    #     return self.cache.get(key)

    def add_value(self, key: str, value: Any, expire: Optional[int] = None) -> bool:
        """
        Adds a key, value to the cache.

        Args:
            key (str): Key for the value.
            value (Any): Value to be stored.
            expire (Optional[int]): Expiration time in seconds (optional).

        Returns:
            bool: True if process succeeded.
        """
        try:
            self.cache.set(key, value, ex=expire)
            return True
        except RedisError as ex:
            print(f"Error setting value in Redis: {ex}")
            return False

    def get_value(self, key: str) -> Optional[Any]:
        """
        Gets the value from cache given a key.

        Args:
            key (str): Key for the value.

        Returns:
            Optional[Any]: Stored value or None if it doesn't exist.
        """
        try:
            value = self.cache.get(key)
            return value.decode("utf-8") if value else None
        except RedisError as ex:
            print(f"Error getting value from Redis: {ex}")
            return None

    def remove_value(self, key: str) -> bool:
        """
        Removes a key from cache.

        Args:
            key (str): Key for the value.

        Returns:
            bool: True if operation succeeded.
        """
        try:
            return self.cache.delete(key) > 0
        except RedisError as ex:
            print(f"Error deleting value from Redis: {ex}")
            return False

    def exists(self, key: str) -> bool:
        """
        Verifies if a key exists.

        Args:
            key (str): Key for the value.

        Returns:
            bool: True if the key exists.
        """
        try:
            return self.cache.exists(key) == 1
        except RedisError as ex:
            print(f"Error checking existence of key in Redis: {ex}")
            return False

    def add_to_set(self, set_key: str, value: Any) -> bool:
        """
        Adds a value to a cached set.

        Args:
            set_key (str): Key for the set.
            value (Any): Value to be stored.

        Returns:
            bool: True if process succeeded.
        """
        try:
            self.cache.sadd(set_key, value)
            return True
        except RedisError as ex:
            print(f"Error setting value in Redis: {ex}")
            return False

    def remove_from_set(self, set_key: str, value: Any) -> bool:
        """Removes a value from a set."""
        try:
            return self.cache.srem(set_key, value) > 0
        except RedisError as ex:
            print(f"Error deleting value from Redis: {ex}")
            return False

    def exists_in_set(self, set_key: str, value: Any) -> bool:
        """Verifies if a value exists in a cached set."""
        # return self.redis_client.sismember(set_name, value)
        try:
            return self.cache.sismember(set_key, value)
        except RedisError as ex:
            print(f"Error checking existence of key in Redis: {ex}")
            return False

    def get_set(self, set_key):
        """Obtener todos los valores del set en Redis."""
        return self.cache.smembers(set_key)
