# slang_mini_assignment
 Mini Assignment from Slang Labs

## Files

<table>
<tr>
<td> main.py </td>
<td> start point for both tfidf and uploading APIs </td>
</tr>
</table>

main.py  - start point for both tfidf and uploading APIs <br>
search.py - Ranks the documents according to their tf-idf score with respect to the search query <br>
upload_dir.py - takes directory path as input and uploads all the files in the directory <br>
tfidf_test.py - unitest cases for checking Tfidf search <br>
 
 
To start the API, use the following 

```
python main.py
```

The API runs on `127.0.0.1` at port `8080`

The documentation of the API can be accessed at `http://127.0.0.1:8080/docs`

After running `main.py` to perform search, open a new terminal and run the `search.py` by `python search.py` command

For running the test cases, Run the `tfidf_test.py` using the `python tfidf_test.py` command

For uploading multiple files use the `upload_dir.py`, a input path is to be passed as commandline argument

### Format
```
python upload_dir.py --input_dir INPUT PATH
```
### Example
```
python upload_dir.py --input_dir F:\Datasets\aclImdb_v1\aclImdb\test\neg\
```
