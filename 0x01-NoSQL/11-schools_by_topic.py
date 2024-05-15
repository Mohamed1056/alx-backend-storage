#!/usr/bin/env python3
'''
Script for finding some information
about a certain topic.
'''


def schools_by_topic(mongo_collection, topic):
    '''
    function to return a certain
    topic.
    '''
    return mongo_collection.find({"topic": topic})
