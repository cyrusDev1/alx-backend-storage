#!/usr/bin/env python3
"""provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient
client = MongoClient(host="localhost", port=27017)
db = client.logs


def log_stats():
    """print logs stats"""
    print("{} logs".format(db.nginx.count_documents({})))
    print("Methods:")
    for i in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        print("\tmethod {}: {}".format(
            i, db.nginx.count_documents({"method": i})))
    print("{} status check".format(db.nginx.count_documents(
        {"method": "GET", "path": "/status"})))


if __name__ == "__main__":
    log_stats()
