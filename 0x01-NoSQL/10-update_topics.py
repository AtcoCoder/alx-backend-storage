#!/usr/bin/env python3
""" 10-update_topics module"""


def  update_topics(mongo_collection, name, topics):
    """update_topics(mongo_collection, name, topics)
    updates mongo_collection with name: name with topics: 'topics'
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})