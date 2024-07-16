#!/usr/bin/env python3
from pymongo import MongoClient


def log_stats():
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
    # Display the results
    print(f"{total} logs")
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {method_count[method]}")
    print(f"{status_check} status check")


if __name__ == "__main__":
    log_stats()
