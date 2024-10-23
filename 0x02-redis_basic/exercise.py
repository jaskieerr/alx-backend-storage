#!/usr/bin/env python3
'''redis is good'''

import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    '''counting Cahe methods calls'''

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        '''yadi yadi yada'''
        keyy = method.__qualname__
        self._redis.incr(keyy)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    '''storing callskinda'''
    input_k = method.__qualname__ + ":inputs"
    output-k = method.__qualname__ + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        '''yadi yadi yada'''
        self._redis.rpush(input_k, str(args))
        res = method(self, *args, **kwargs)
        self._redis.rpush(output-k, str(res))
        return res

    return wrapper


def replay(method: Callable) -> None:
    '''yadi yadi yada'''
    inpyt = "{}:inputs".format(method.__qualname__)
    outputu = "{}:outputs".format(method.__qualname__)

    ins = method.__self__._redis.lrange(inpyt, 0, -1)
    outs = method.__self__._redis.lrange(outputu, 0, -1)

    print("{} was called {} times:".format(method.__qualname__, len(ins)))
    for inp, out in zip(ins, outs):
        print(
            "{}(*{}) -> {}".format(
                method.__qualname__, inp.decode("utf-8"), out.decode("utf-8")
            )
        )


class Cache:
    '''task0'''

    def __init__(self):
        '''yadi yadi yada'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''storing yadi yadi yada'''
        keyx = str(uuid.uuid4())
        self._redis.set(keyx, data)
        return keyx

    def get(
        self, key: str, fn: Optional[Callable] = None
    ) -> Union[str, bytes, int, float]:
        '''yadi yadi yada'''
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        '''yadi yadi yada'''
        return self.get(key, fn=str)

    def get_int(self, key: str) -> int:
        '''yadi yadi yada'''
        return self.get(key, fn=int)
