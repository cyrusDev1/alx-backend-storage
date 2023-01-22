#!/usr/bin/env python3
"""Writing strings to Redis"""
import redis
import uuid
from typing import Union


class Cache:
    """Cache class"""
    def __init__(self):
        """Instanciation"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, int, float, bytes]) -> str:
        """Return uuid"""
        myuuid = str(uuid.uuid4())
        self._redis.set(myuuid, data)
        return myuuid
