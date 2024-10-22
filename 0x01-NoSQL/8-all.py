#!/usr/bin/env python3
'''
list all
'''


def list_all(mongo_collection):
    '''
    function that lists
    '''
    return list(mongo_collection.find())
