#!/usr/bin/env python3
"""Module to provide nginx logs stored in mongodb"""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient()
    logs = client.logs.nginx
    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("{} logs".format(logs.count_documents({})))
    print('Methods')
    for x in method:
        print(" method {}: {}".format(x, logs.count_documents({'method': x})))
    print("{} status check".format(logs.count_documents({'method': 'GET',
                                                        'path': '/status'}
                                                        )))
