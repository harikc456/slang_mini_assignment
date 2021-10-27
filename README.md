# Slang Mini Assignment
 Mini Assignment from Slang Labs

## Files

<table>
<tr>
<td> main.py </td>
<td> start point for both tfidf and uploading APIs </td>
</tr>

<tr>
<td> search.py </td>
<td> Ranks the documents according to their tf-idf score with respect to the search query </td>
</tr>

<tr>
<td> upload_dir.py </td>
<td> takes directory path as input and uploads all the files in the directory  </td>
</tr>

<tr>
<td> tfidf_test.py </td>
<td> unitest cases for checking Tfidf search </td>
</tr>


<tr>
<td> routers\file_upload.py </td>
<td> API for uploading multiple files </td>
</tr>

<tr>
<td> routers\tfidf.py </td>
<td> Native Implementation of tf-idf </td>
</tr>

<tr>
<td> routers\tfidf_api.py </td>
<td> API for ranking documents with respect to the search query</td>
</tr>
</table>

## TF-IDF Implementation

The formulas used for the native implementation of tf-idf

<img src="img\term_frequency.PNG">

t is the term, d is the document
	
<img src="img\idf.PNG">

N is the number of documents, n_t is the number of documents where term t appears in the corpus to avoid division by zero, n_t is set as 1 by default

## How to run the scripts
 
To start the API, use the following 

```
python main.py
```

The API runs on `127.0.0.1` at port `8080`

The documentation of the API can be accessed at `http://127.0.0.1:8080/docs`

After running `main.py` to perform search, open a new terminal and run the `search.py` by `python search.py` command

For running the test cases, Run the `tfidf_test.py` using the `python tfidf_test.py` command

For uploading multiple files use the `upload_dir.py`, a input path is to be passed as a commandline argument

### Format
```
python upload_dir.py --input_dir INPUT PATH
```
### Example
```
python upload_dir.py --input_dir C:\Users\HARIKRISHNAN\Documents\GitHub\slang_mini_assignment\test_uploads\
```

## Notes about uploads

 Only files with .txt files will be uploaded  <br>
 When using `search.py` after a `upload_dir.py` execution, there will be a time lag as the tfidf scores has to be recomputed.<br> 
 A hard limit of 500 files per upload has been set
