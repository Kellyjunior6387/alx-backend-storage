#!/usr/bin/env python3
"""Python function that inserts a new document in a collection
based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """
    Python function that inserts a new document in a collection
    """
    document = {}
    for key, value in kwargs.items():
        document[str(key)] = value
    result = mongo_collection.insert_one(document)
    return result.inserted_id
