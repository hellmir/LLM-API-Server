from langchain_community.chat_models import ChatClovaX
from langchain_community.llms.sambanova import SambaNovaCloud
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI

DEFAULT_MODEL = SambaNovaCloud(
    model="Meta-Llama-3.3-70B-Instruct",
    max_tokens=1024,
    temperature=0.7,
    top_p=0.9,
    top_k=40
)


def get_llm(llm_type: str):
    if llm_type == "llama":  # 기본 모델을 변경하더라도 함수가 변경에 닫혀 있도록 하기 위해 중복 설정
        return SambaNovaCloud(
            model="Meta-Llama-3.3-70B-Instruct",
            max_tokens=1024,
            temperature=0.7,
            top_p=0.9,
            top_k=40
        )
    elif llm_type == "chatgpt":
        return ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo", streaming=True)
    elif llm_type == "gemini":
        return ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",
            temperature=0,
            max_output_tokens=200
        )
    elif llm_type == "clovax":
        return ChatClovaX(model="HCX-003", disable_streaming=False)
    else:
        return DEFAULT_MODEL
