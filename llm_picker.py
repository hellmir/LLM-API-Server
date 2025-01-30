import llm_generator

DEFAULT_MODEL = None


def get_llm(llm_type: str):
    set_default_model()

    if llm_type == "clovax":
        return llm_generator.generate_chat_clova_x()
    elif llm_type == "gemini":
        return llm_generator.generate_chat_google_generative_ai()
    elif llm_type == "gpt":
        return llm_generator.generate_chat_open_ai()
    elif llm_type == "llama":  # 기본 모델을 변경하더라도 get_llm 함수가 변경에 닫혀 있도록 하기 위해 중복 설정
        return llm_generator.generate_samba_nova_cloud()
    else:
        return DEFAULT_MODEL


def set_default_model():
    global DEFAULT_MODEL
    DEFAULT_MODEL = llm_generator.generate_samba_nova_cloud()
