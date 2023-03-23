#!/usr/bin/env python3
"""returns all students sorted by average score"""


def top_students(mongo_collection):
    """returns all students sorted by average score"""
    lt = list(mongo_collection.find())
    average = []
    for student in lt:
        for topics in student.topics:
            average = i.topics
        average.append({"name": lt.name})
