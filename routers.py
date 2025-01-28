import os

from dotenv import load_dotenv
from fastapi import APIRouter
from pydantic import BaseModel, Field

from global_exception_handler import throw_unauthorized_exception
from services import generate_response

router = APIRouter(prefix="/streaming")


class LLMRequest(BaseModel):
    llm_type: str = Field(..., description="LLM 모델 유형(clovax, chatgpt, llama): 미입력 시 기본 모델 사용",
                          examples=["clovax", "llama", "chatgpt"])
    template: str = Field(..., description="요청 프롬프트(요구사항)", examples=["레시피 추천해 줘"])
    variables: str = Field(..., description="요청 프롬프트에 적용할 조건", examples=["토마토, 밀가루"])
    secret_key: str = Field(..., description="사용자 인증을 위한 비밀 키", examples=["abcde"])

    class Config:
        title = "LLM 서비스 요청 파라미터"


from fastapi.responses import StreamingResponse


@router.post(
    "",
    summary="LLM 스트리밍 서비스 이용",
    description="""
    다음 파라미터를 전송해 LLM 서비스를 이용할 수 있습니다. 응답은 토큰화하여 Stream 형태로 제공됩니다.
    \n- llm_type: LLM 모델 유형(clovax, chatgpt, llama): 미입력 시 기본 모델 사용
    \n- template: 요청 프롬프트(요구사항)
    \n- variables: 요청 프롬프트에 적용할 조건
    \n- Secret Key: 사용자 인증을 위한 비밀 키
                """
)
def invoke_llm(request: LLMRequest):
    load_dotenv()
    if request.secret_key != os.environ.get("SECRET_KEY"):
        throw_unauthorized_exception()

    def response_generator():
        for chunk in generate_response(
                request.llm_type, request.template, request.variables
        ):
            yield chunk

    return StreamingResponse(response_generator(), media_type="text/plain")


@router.post(
    "/sse",
    summary="LLM 스트리밍 SSE 서비스 이용",
    description="""
    다음 파라미터를 전송해 LLM 서비스를 이용할 수 있습니다. 응답은 최소 단위로 토큰화하여 SSE를 통한 Stream 형태로 제공됩니다.
    \n- llm_type: LLM 모델 유형(clovax, chatgpt, llama): 미입력 시 기본 모델 사용
    \n- template: 요청 프롬프트(요구사항)
    \n- variables: 요청 프롬프트에 적용할 조건
    \n- Secret Key: 사용자 인증을 위한 비밀 키
                """
)
def invoke_llm_sse(request: LLMRequest):
    load_dotenv()
    if request.secret_key != os.environ.get("SECRET_KEY"):
        throw_unauthorized_exception()

    def response_generator():
        for chunk in generate_response(
                request.llm_type, request.template, request.variables
        ):
            yield f"data: {chunk}\n\n"

    return StreamingResponse(response_generator(), media_type="text/event-stream")
