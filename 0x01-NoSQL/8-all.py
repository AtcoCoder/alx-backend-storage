#!/usr/bin/env python3
"""8-all module"""


def list_all(mongo_collection):
    """list_all(mongo_collection) list all documents in collenct mongo
    returns an empty list if no document in the collections
    """
    all_docs= []
    for doc in mongo_collection.find():
        all_docs.append(doc)
    print(all_docs)
    return all_docs