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
        with open(file_name,'wb+') as f:
            f.write(file.file.read())
            f.close()

    return {"filenames": [file.filename for file in files]}