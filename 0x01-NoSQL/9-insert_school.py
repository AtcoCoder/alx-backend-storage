#!/usr/bin/env python3
""" 9-insert_school module """


def insert_school(mongo_collection, **kwargs):
    """insert_school(mongo_collection, **kwargs) inserts a new document in a collection
    returns the new _id of the inserted document
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id