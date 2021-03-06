import os
import json
import unittest
from routers.tfidf import Tfidf

class TestingClass(unittest.TestCase):

    def __init__(self, *args, **kwargs):

        super(TestingClass, self).__init__(*args, **kwargs)
        upload_dir = os.getcwd()+"/test_uploads/"
        docs = os.listdir(upload_dir)
        self.tfidf = Tfidf(docs, upload_dir = "./test_uploads/")

    def test_tfidf1(self):
        query = "poor bad"
        res = self.tfidf.rank_docs(query)
        self.assertEqual(res[0]['document_id'], 6, "Should be 6")

    def test_tfidf2(self):
        query = "movie"
        res = self.tfidf.rank_docs(query)
        self.assertEqual(res[0]['document_id'], 23, "Should be 23")

    def test_tfidf3(self):
        query = "taste"
        res = self.tfidf.rank_docs(query)
        self.assertEqual(res[0], "taste")

if __name__ == '__main__':
    unittest.main()