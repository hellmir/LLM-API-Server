import os
from typing import Dict, List, Optional

from dotenv import load_dotenv
from fastapi import APIRouter
from pydantic import BaseModel, Field

from global_exception_handler import throw_unauthorized_exception
from services import generate_response

router = APIRouter(prefix="/streaming")


class LLMRequest(BaseModel):
    llm_type: Optional[str] = Field(default=None, description="LLM 모델 유형(clovax, chatgpt, llama): 미입력 시 기본 모델 사용",
                                    examples=["mistral", "llama", "clovax", "gemini", "gpt"])
    template: str = Field(..., description="요청 프롬프트(요구사항)", examples=["레시피 추천해 줘"])
    options: Optional[Dict[str, List[str]]] = Field(
        default=None,
        description="요청 프롬프트에 적용할 조건들(선택사항)",
        examples=[
            {
                "재료": ["토마토", "밀가루", "양파"],
                "조리 도구": ["프라이팬", "오븐", "믹서기"],
                "조리 시간": ["30분"],
                "요리 유형": ["이탈리안"],
                "식사 유형": ["아침"]
            }
        ]
    )
    secret_key: str = Field(..., description="사용자 인증을 위한 비밀 키", examples=["abcde"])

    class Config:
        title = "LLM 서비스 요청 파라미터"


from fastapi.responses import StreamingResponse


@router.post(
    "",
    summary="LLM 스트리밍 서비스 이용",
    description="""
    다음 파라미터를 전송해 LLM 서비스를 이용할 수 있습니다. 응답은 토큰화하여 Stream 형태로 제공됩니다.
    \n- llm_type: LLM 모델 유형(미입력 시 기본 모델 사용)
    \n  - mistral
    \n  - llama
    \n  - clovax
    \n  - gemini
    \n  - gpt
    \n- template: 요청 프롬프트(요구사항)
    \n- options: 요청 프롬프트에 적용할 조건들(선택사항)
    \n  - Key: Array Value 형태로 전송
    \n- Secret Key: 사용자 인증을 위한 비밀 키
                """
)
def invoke_llm(request: LLMRequest):
    load_dotenv()
    if request.secret_key != os.environ.get("SECRET_KEY"):
        throw_unauthorized_exception()

    llm_type = request.llm_type if request.llm_type else ""
    options = request.options if request.options else {"Not necessary"}

    def response_generator():
        for chunk in generate_response(
                llm_type, request.template, options
        ):
            yield chunk

    return StreamingResponse(response_generator(), media_type="text/plain")


@router.post(
    "/sse",
    summary="LLM 스트리밍 SSE 서비스 이용",
    description="""
    다음 파라미터를 전송해 LLM 서비스를 이용할 수 있습니다. 응답은 최소 단위로 토큰화하여 SSE를 통한 Stream 형태로 제공됩니다.
    \n- llm_type: LLM 모델 유형(미입력 시 기본 모델 사용)
    \n  - mistral 
    \n  - llama
    \n  - clovax
    \n  - gemini
    \n  - gpt
    \n- template: 요청 프롬프트(요구사항)
    \n- options: 요청 프롬프트에 적용할 조건들(선택사항)
    \n  - Key: Array Value 형태로 전송
    \n- Secret Key: 사용자 인증을 위한 비밀 키
                """
)
def invoke_llm_sse(request: LLMRequest):
    load_dotenv()
    if request.secret_key != os.environ.get("SECRET_KEY"):
        throw_unauthorized_exception()

    llm_type = request.llm_type if request.llm_type else ""
    options = request.options if request.options else {"Not necessary"}

    def response_generator():
        for chunk in generate_response(
                llm_type, request.template, options
        ):
            yield f"data: {chunk}\n\n"

    return StreamingResponse(response_generator(), media_type="text/event-stream")
