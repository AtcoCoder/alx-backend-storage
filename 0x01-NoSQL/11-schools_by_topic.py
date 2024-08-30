#!/usr/bin/env python3
""" 11-schools_by_topic """


def schools_by_topic(mongo_collection, topic):
    """schools_by_topic(mongo_collection, topic)
    mongo_collection: pymongo collection object
    topic: (string) will be topic searched
    returns the list of school having a specific topic seared
    """
    topic_schools = []
    for doc in mongo_collection.find({"topics": topic}):
        topic_schools.append(doc)
    return topic_schools