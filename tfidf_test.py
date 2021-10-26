import os
import unittest
from routers.tfidf import Tfidf

class Tfidftest(unittest.TestCase):
        
    def test_tfidf1(self):
        upload_dir = os.getcwd()+"/uploads/"
        docs = os.listdir(upload_dir)
        tfidf = Tfidf(docs)
        query = "poor bad"
        res = tfidf.rank_docs(query)
        self.assertEqual(res[0]['document_id'], 6, "Should be 6")

    def test_tfidf2(self):
        upload_dir = os.getcwd()+"/uploads/"
        docs = os.listdir(upload_dir)
        tfidf = Tfidf(docs)
        query = "movie"
        res = tfidf.rank_docs(query)
        self.assertEqual(res[0]['document_id'], 23, "Should be 23")


if __name__ == '__main__':
    unittest.main()