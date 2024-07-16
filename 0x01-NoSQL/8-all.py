#!/usr/bin/env python3
"""A script to list all documents"""


def list_all(mongo_collection):
    """
    Function to list all document from a Pymongo object
    """
    return list(mongo_collection.find())
