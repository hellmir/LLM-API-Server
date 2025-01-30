from langchain_community.chat_models import ChatClovaX
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI

DEFAULT_MODEL = ChatClovaX(model="HCX-003", disable_streaming=False)


def get_llm(llm_type: str):
    if llm_type == "llama":
        return ChatOllama(model="llama3.2", disable_streaming=False)
    elif llm_type == "chatgpt":
        return ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo", streaming=True)
    elif llm_type == "gemini":
        return ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",
            temperature=0,
            max_output_tokens=200
        )
    elif llm_type == "clovax":
        return ChatClovaX(model="HCX-003", disable_streaming=False)  # 기본 모델을 변경하더라도 함수가 변경에 닫혀 있도록 하기 위해 중복 설정
    else:
        return DEFAULT_MODEL
