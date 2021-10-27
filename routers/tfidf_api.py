from routers.tfidf import Tfidf
import os
import json
from fastapi import APIRouter

router = APIRouter()
upload_dir = os.getcwd()+"/uploads/"
docs = os.listdir(upload_dir)
print("Calculating Tfidf scores")
tfidf = Tfidf(docs)

@router.get("/tfidf/{input_query}")
async def tfidf_search(input_query: str):

	global tfidf, docs
	upload_dir = os.getcwd()+"/uploads/"
	new_docs = os.listdir(upload_dir)
	if docs != new_docs:
		print("New files detected, Updating TF-IDF.....")
		tfidf = Tfidf(new_docs)
	rankings = tfidf.rank_docs(input_query)
	if isinstance(rankings[0], dict):
		return {'rankings' : rankings}
	return {"OOV" : rankings}