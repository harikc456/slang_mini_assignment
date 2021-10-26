from fastapi import Depends, FastAPI
import uvicorn
from routers import file_upload, tfidf_api


app = FastAPI()
app.include_router(file_upload.router)
app.include_router(tfidf_api.router)

@app.get("/")
async def root():
    return {"message": "Slang Mini Assignment"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)