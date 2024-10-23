#!/usr/bin/env python3
'''
task0 yes task0
'''
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    '''counting Cache method calls'''

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        '''doc doc class'''
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


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

    def get(
            self,
            key: str,
            fn: Callable = None,
            ) -> Union[str, bytes, int, float]:
        '''
        from bytes to str
        '''
        vall = self._redis.get(key)
        return fn(vall) if fn is not None else vall

    def get_str(self, key: str) -> str:
        '''auto parameterizing'''
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        '''auto parameterizing'''
        return self.get(key, lambda x: int(x))
