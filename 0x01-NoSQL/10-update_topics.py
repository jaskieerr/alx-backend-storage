#!/usr/bin/env python3
'''
update update
'''


def update_topics(mongo_collection, name, topics):
    '''
    python update
    '''
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
