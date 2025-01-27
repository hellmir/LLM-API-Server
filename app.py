import uvicorn
from fastapi import FastAPI

from routers import router

app = FastAPI(
    title="LLM 서버 API",
    description="LLM 서비스를 제공하는 서버 API입니다.",
    version="1.0",
)

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
