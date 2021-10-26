from routers.tfidf import Tfidf
import os
import json
from fastapi import APIRouter

router = APIRouter()

@router.get("/tfidf/{input_query}")
async def tfidf_search(input_query: str):

	upload_dir = os.getcwd()+"/uploads/"
	docs = os.listdir(upload_dir)
	print("Calculating Tfidf scores")
	tfidf = Tfidf(docs)
	rankings = tfidf.rank_docs(input_query)
	return {'rankings' : rankings}