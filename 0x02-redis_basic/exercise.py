#!/usr/bin/env python3
"""Writing strings to Redis"""
import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    """Cache class"""
    def __init__(self):
        """Instanciation"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Return uuid"""
        myuuid = str(uuid.uuid4())
        self._redis.set(myuuid, data)
        return myuuid

    def get(self, key: str, fn: Optional[Callable] = None) -> str:
        """used to convert the data back to the desired format."""
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, data: str) -> str:
        """get str"""
        return data.decode('utf-8', 'strict')

    def get_int(self, data: str) -> int:
        """get int"""
        return int(data)
