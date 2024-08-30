#!/usr/bin/env python3
""" 12-log_stats """
from pymongo import MongoClient #type: ignore

client = MongoClient('mongodb://127.0.0.1:27017')
log_collection = client.logs.nginx
log_count = log_collection.count_documents({})

first_line = "{} logs".format(log_count)
second_line = "Method:"
get_requests = "\tmethod GET: {}".format(log_collection.count_documents({"method": "GET"}))
post_requests = "\tmethod POST: {}".format(log_collection.count_documents({"method": "POST"}))
put_requests = "\tmethod PUT: {}".format(log_collection.count_documents({"method": "PUT"}))
patch_requests = "\tmethod PATCH: {}".format(log_collection.count_documents({"method": "PATCH"}))
delete_requests = "\tmethod DELETE: {}".format(log_collection.count_documents({"method": "DELETE"}))
get_status = "{} status check".format(log_collection.count_documents({"method": "GET", "path": "/status"}))

print(f"""{first_line}
{second_line}
{get_requests}
{post_requests}
{put_requests}
{patch_requests}
{delete_requests}
{get_status}"""
)