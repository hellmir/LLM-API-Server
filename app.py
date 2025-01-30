import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from routers import router

load_dotenv()
app = FastAPI(
    title="생성형 AI 서버 API",
    description="""
    \n ## 생성형 AI 서비스를 제공하는 서버 API입니다.
    \n ### 제공 모델
    \n <b>
    \n  - mistral
    \n  - llama
    \n  - clovax
    \n  - gemini
    \n  - gpt
    \n </b>
    """,
    version="2.1"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.environ.get("FRONTEND_URL")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
