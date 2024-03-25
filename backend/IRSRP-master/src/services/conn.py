import os

from dotenv import load_dotenv
from pymongo import MongoClient

from src.services.logger import get_logger

logger = get_logger(__name__)



load_dotenv(".current.env")


def get_papers_collection():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING ="mongodb://alenmon2002:X9yqEcFplTqVBk7a@localhost:27017/?retryWrites=true&w=majority"
    client = MongoClient(CONNECTION_STRING)

    db = client.irsrp
    try:
        db.get_collection("papers")
    except Exception as _e:
        logger.info("Papers collection does not exist, creating one...")
        create_collection(db)

    return db.papers


def create_collection(db):
    db.create_collection("papers")
