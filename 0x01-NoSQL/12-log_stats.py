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

    first_line = "{} logs".format(log_count)
    second_line = "Methods:"
    get_requests = "\tmethod GET: {}".format(get_count)
    post_requests = "\tmethod POST: {}".format(post_count)
    put_requests = "\tmethod PUT: {}".format(put_count)
    patch_requests = "\tmethod PATCH: {}".format(patch_count)
    delete_requests = "\tmethod DELETE: {}".format(delete_count)
    get_status = "{} status check".format(get_status)
    print("{}\n{}".format(first_line, second_line))
    request_counts = f"""{get_requests}
    {post_requests}
    {put_requests}
    {patch_requests}
    {delete_requests}"""
    print(request_counts)
    print(get_status)