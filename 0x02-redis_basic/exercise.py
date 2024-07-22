#!/usr/bin/env python3
"""Module to create a Cache class"""
import redis
from typing import Union, Callable, Optional
import uuid
from functools import wraps


def count_calls(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = f"{method.__qualname__}:calls"
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """Cache class
    """
    def __init__(self):
        """Initilaise redis instance
        """
        self.__redis = redis.Redis()
        self.__redis.flushdb()

    @count_calls
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

    def get_call_count(self, method_name: str) -> int:
        return int(self._redis.get(f"{method_name}:calls") or 0)
