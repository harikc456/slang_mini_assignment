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

<img src="img\idf.PNG">

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
python upload_dir.py --input_dir F:\Datasets\aclImdb_v1\aclImdb\test\neg\
```
 <strong> Only files with .txt files will be uploaded </strong>