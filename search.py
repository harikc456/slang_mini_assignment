import requests
import json
query = input("Enter your query : ")
response = requests.get("http://127.0.0.1:8080/tfidf/"+query)
response = json.loads(response.content)
if "OOV" in response.keys():
	oov_words = " ".join([word for word in response['OOV']])
	print("Unknown word(s) " + oov_words)
else:
	for res in response['rankings']:
		print(f"Document_id  : {res['document_id']}  Document_name : {res['document_name']} tfidf_score : {res['tfidf_score']}")