#!/usr/bin/env python3
'''
insert
'''


def insert_school(mongo_collection, **kwargs):
    '''
    function that lists
    '''
    return mongo_collection.insert_one(kwargs).inserted_id
