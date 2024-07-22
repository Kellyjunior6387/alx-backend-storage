#!/usr/bin/env python3
"""Module to create a Cache class"""
import redis
from typing import Union, Callable, Optional
import uuid


class Cache:
    """Cache class
    """
    def __init__(self):
        """Initilaise redis instance
        """
        self.__redis = redis.Redis()
        self.__redis.flushdb()

    def store(self, data: Union[str, int, bytes, float]) -> str:
        """Store the data input in a redis instance
        """
        key = str(uuid.uuid4())
        self.__redis.mset({key: data})
        return key

    def get(self, key: str, fn: Optional[Callable] =
            None) -> Union[str, int, bytes, float]:
        value = self.__redis.get(key)
        if value is None:
            return None
        if fn:
            return fn(value)
        return value

    def get_int(self, key: str) -> Optional[int]:
        return self.get(key, fn=int)

    def get_str(self, key: str) -> Optional[str]:
        return self.get(key, fn=lambda x: x.decode('utf-8'))
