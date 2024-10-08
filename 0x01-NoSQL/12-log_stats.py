#!/usr/bin/env python3
""" 12-log_stats """
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    log_collection = client.logs.nginx
    get_status = {"method": "GET", "path": "/status"}
    log_count = log_collection.count_documents({})
    get_count = log_collection.count_documents({"method": "GET"})
    post_count = log_collection.count_documents({"method": "POST"})
    put_count = log_collection.count_documents({"method": "PUT"})
    patch_count = log_collection.count_documents({"method": "PATCH"})
    delete_count = log_collection.count_documents({"method": "DELETE"})
    get_status = log_collection.count_documents(get_status)

    print("{} logs\nMethods:".format(log_count))
    print("\tmethod GET: {}".format(get_count))
    print("\tmethod POST: {}".format(post_count))
    print("\tmethod PUT: {}".format(put_count))
    print("\tmethod PATCH: {}".format(patch_count))
    print("\tmethod DELETE: {}".format(delete_count))
    print("{} status check".format(get_status))