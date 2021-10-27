from typing import List
import uvicorn
import os
from fastapi import FastAPI, File, UploadFile
from fastapi import APIRouter

router = APIRouter()

@router.post("/uploadfiles/")
async def create_upload_files(files: List[UploadFile] = File(...)):

    for file in files:
        file_name = os.getcwd()+"/uploads/"+file.filename.replace(" ", "-")
        if file_name.split(".")[-1] != 'txt':
            print("Not .txt file, skipping uploading the file")
            continue

        with open(file_name,'wb+') as f:
            f.write(file.file.read())

    return {"filenames": [file.filename for file in files]}