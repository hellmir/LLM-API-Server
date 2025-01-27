import uvicorn
from fastapi import FastAPI

from routers import router

app = FastAPI(
    title="생성형 AI 서버 API",
    description="생성형 AI 서비스를 제공하는 서버 API입니다.",
    version="1.0",
)

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
