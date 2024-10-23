#!/usr/bin/env python3
'''
task0 yes task0
'''
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


class Cache:
    '''
    task0
    '''
    def __init__(self):
        '''constructor'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''doc odc doc'''
        keyy = str(uuid.uuid4)
        self._redis.set(keyy, data)
        return keyy
