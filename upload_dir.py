import os
import json
import argparse
import requests

parser = argparse.ArgumentParser("Directory Uploading")
parser.add_argument("--input_dir", type=str, help="The input directory")

args = parser.parse_args()
input_dir = args.input_dir

doc_list = os.listdir(input_dir)

files = []
for doc in doc_list:
    fp = open(input_dir + doc, "r")
    f = ("files", (doc, fp, "multipart/form-data"))
    fp.close()
    files.append(f)
r = requests.post('http://127.0.0.1:8080/uploadfiles/', files=files)
print(json.loads(r.content))