#!/usr/bin/env python3
"""Writing strings to Redis"""
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """count calls"""
    method_key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        self._redis.incr(method_key)
        return method(self, *args, **kwds)
    return wrapper


class Cache:
    """Cache class"""
    def __init__(self):
        """Instanciation"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
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
