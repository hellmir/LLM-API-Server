from langchain_community.chat_models import ChatClovaX
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI

DEFAULT_MODEL = ChatOllama(model="llama3.2")


def get_llm(llm_type: str):
    if llm_type == "clovax":
        return ChatClovaX(model="HCX-003")
    elif llm_type == "chatgpt":
        return ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    elif llm_type == "llama":
        return ChatOllama(model="llama3.2")  # 기본 모델을 변경하더라도 함수가 변경에 닫혀 있도록 하기 위해 중복 설정
    else:
        return DEFAULT_MODEL
