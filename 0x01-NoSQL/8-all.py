#!/usr/bin/env python3
'''Script for listing all
the document in the collection.
'''


def list_all(mongo_collection):
    '''
    returns the documents in a certain
    collection inhereted by mongo_collection.
    '''
    return mongo_collection.find()
