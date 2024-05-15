#!/usr/bin/env python3
'''
Script for inserting new
documents in the collection.
'''


def insert_school(mongo_collection, **kwargs):
    '''
    function that will return
    __id of this document.
    '''
    new_documents = mongo_collection.insert_one(kwargs)
    return new_documents.inserted_id
