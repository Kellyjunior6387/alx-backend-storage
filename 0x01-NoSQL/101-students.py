#!/usr/bin/env python3
""" Python function that returns all students sorted by average score"""
from pymongo import MongoClient


def top_students(mongo_collection):
    """
     Python function that sorts students by average score
    :param mongo_collection : The pymongo collection object
    """
    pipeline = [
        {
            '$project': {
                'name': 1,
                'topics': 1,
                'averageScore': {'$avg': '$topics.score'}
            }
        },
        {
            '$sort': {'averageScore': -1}
        }
    ]
    return list(mongo_collection.aggregate(pipeline))
