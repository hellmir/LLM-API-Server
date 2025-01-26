import os

from dotenv import load_dotenv
from fastapi import APIRouter
from fastapi import HTTPException
from pydantic import BaseModel

from services import generate_response

router = APIRouter()


class LLMRequest(BaseModel):
    llm_type: str
    template: str
    variables: str
    secret_key: str


@router.post("/")
def invoke_llm(request: LLMRequest):
    load_dotenv()
    if request.secret_key != os.environ["SECRET_KEY"]:
        raise HTTPException(status_code=401, detail="[인증 실패] Secret Key가 일치하지 않습니다. 확인 후 다시 시도해 주세요.")

    return {"response": generate_response(request.llm_type, request.template, request.variables)}
