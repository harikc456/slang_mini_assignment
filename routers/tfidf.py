import numpy as np
import math

upload_dir = "./uploads/"

class Tfidf():
    
    def __init__(self, docs):
        self.corpus_index = {i:doc for i,doc in enumerate(docs)}

        self.corpus = []
        for doc in docs:
            f = open(upload_dir + doc)
            self.corpus.append(f.read())
            f.close()

        self.vocab_index = {}
        self.idf_dict = {}
        words = self.create_vocab_index()
        self.calculate_idf(words)
        self.idf_vector = np.array([self.idf_dict[w] for w in words])
        self.term_freq = np.zeros((len(self.corpus), len(words)))
        self.term_frequency()
        self.tfidf_matrix = self.term_freq * self.idf_vector
        
    def create_vocab_index(self):
        self.vocab_index = {}
        for doc in self.corpus:
            for word in doc.split():
                self.vocab_index[word.lower()] = len(self.vocab_index)
        
        return list(self.vocab_index.keys())
    
    def calculate_idf(self, words):
        for word in words:
            count = 1
            for doc in self.corpus:
                if word in doc.lower().split():
                    count+=1
            self.idf_dict[word] = math.log(len(self.corpus)/ count)
            
    def term_frequency(self): 
        for idx,doc in enumerate(self.corpus):
            word_count_dict = {}
            count = 0
            for word in doc.split():
                try:
                    word_count_dict[word.lower()] += 1
                except:
                    word_count_dict[word.lower()] = 1
                count += 1
            for k,v in word_count_dict.items():
                col_idx = self.vocab_index[k]
                self.term_freq[idx][col_idx] = v/count
                
    def rank_docs(self, input_query):
        return_dict = []
        tfidf_scores = np.zeros(len(self.corpus))
        out_of_vocab_words = []
        for query in input_query.split():
            if query.lower() not in list(self.vocab_index.keys()):
                out_of_vocab_words.append(query)
                continue
            idx = self.vocab_index[query.lower()]
            tfidf_scores += self.tfidf_matrix[:,idx]
        if sum(tfidf_scores) == 0:
            return out_of_vocab_words
        ranked_idx = np.argsort(tfidf_scores)[::-1]
        for idx in ranked_idx:
            temp_dict = {}
            temp_dict['document_id'] = int(idx)
            temp_dict['document_name'] = self.corpus_index[idx]
            temp_dict['tfidf_score'] = float(tfidf_scores[idx])
            return_dict.append(temp_dict)
            #print(f"Document_id  : #{idx}  Document_name : {self.corpus_index[idx]} tfidf_score : {tfidf_scores[idx]}")
        return return_dict