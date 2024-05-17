#!/usr/bin/env python3
'''
Updating the collection.
'''


def update_topics(mongo_collection, name, topics):
    '''
    function to update the collection.
    '''
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
