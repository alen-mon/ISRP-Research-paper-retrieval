from typing import List, Optional
from pathlib import Path
import os

from fastapi import APIRouter
from pydantic import BaseModel

from src.model.lda import LDA
from src.services.conn import get_papers_collection
from src.services.fetch_papers import fetch_papers
from src.model.bert import BERT


class Paper(BaseModel):
    id: str
    pdf_url: Optional[str]
    title: str
    category: str
    authors: str
    published: Optional[str]


class SearchQueryResponse(BaseModel):
    results: List[Paper]


router = APIRouter()

papers_collection = get_papers_collection()
docs = fetch_papers(papers_collection)

# Load LDA model
lda_model = LDA(docs=docs)
try:
    lda_model.load_model()
except FileNotFoundError:
    print("LDA model file not found, generating one...")
    if docs:  # Check if documents are available
        lda_model.train_and_save()
    else:
        print("No documents available to train LDA model")

# Load BERT model
bert_model = BERT(docs=docs)

@router.get("/")
def index():
    return {
        "detail": "Welcome to IRSRP",
    }


@router.get("/search/lda", tags=["search_paper_lda"])
def query_lda(query: str):
    top_docs = lda_model.predict(query=query)
    results = [
        Paper(
            id=doc["id"],
            pdf_url=doc["pdf_url"],
            title=doc["title"],
            category=doc["category"],
            authors=", ".join(doc["authors"]),
            published=doc["published"],
        )
        for doc in top_docs
    ]
    return SearchQueryResponse(results=results)


@router.get("/search/bert", tags=["search_paper_bert"])
def query_bert(query: str):
    top_docs = bert_model.predict(query=query)
    results = [
        Paper(
            id=doc["id"],
            pdf_url=doc["pdf_url"],
            title=doc["title"],
            category=doc["category"],
            authors=", ".join(doc["authors"]),
            published=doc["published"],
        )
        for doc in top_docs
    ]
    return SearchQueryResponse(results=results)
