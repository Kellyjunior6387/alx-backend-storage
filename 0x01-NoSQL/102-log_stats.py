#!/usr/bin/env python3
"""Module to provide nginx logs stored in mongodb"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx
    # Total number of logs
    total = collection.count_documents({})
    # Number of logs for each HTTP method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_count = {method: collection.count_documents({"method": method})
                    for method in methods}
    # Number of logs with method GET and path /status
    status_check = collection.count_documents({"method": "GET",
                                               "path": "/status"})
    # Pipeleine to calculate the 10 most present IP's
    pipeline_ip = [
        {'$group': {'_id': '$ip', 'count': {"$sum": 1}}},
        {'$sort': {'count': -1}},
        {'$limit': 10}
    ]
    ips = list(collection.aggregate(pipeline_ip))
    print(f"{total} logs")
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {method_count[method]}")
    print(f"{status_check} status check")
    print('IPs:')
    for ip in ips:
        print("\t{}: {}".format(ip['_id'], ip['count']))
