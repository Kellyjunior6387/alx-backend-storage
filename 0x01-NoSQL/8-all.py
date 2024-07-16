#!/usr/bin/env bash
"""A script to list all documents"""
def list_all(mongo_collection):
    """
    Function to list all document from a Pymongo object
    """
    my_list = []
    for document in mongo_collection.find():
        my_list.append(document)
    return my_list
