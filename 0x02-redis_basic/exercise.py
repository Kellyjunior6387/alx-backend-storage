#!/usr/bin/env python3
"""Module to create a Cache class"""
import redis
from typing import Union
import uuid


class Cache:
    """Cache class
    """
    def __init__(self):
        """Initilaise redis instance
        """
        self.__redis = redis.Redis()

    def store(self, data: Union[str, int, bytes, float]) -> str:
        """Store the data input in a redis instance
        """
        key = str(uuid.uuid4())
        self.__redis.mset({key: data})
        return key
