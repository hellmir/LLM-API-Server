from langchain_core.prompts import PromptTemplate

from llm_picker import get_llm

LINE_BREAK = "\n"
TEMPLATE_HEADER = "Given the {variables} I want you to create:" + LINE_BREAK
TEMPLATE_FOOTER = LINE_BREAK + "Answer in KOREAN"


def generate_response(llm_type: str, template_content: str, variables: str):
    prompt = PromptTemplate(
        input_variables=["variables"],
        template=TEMPLATE_HEADER + template_content + TEMPLATE_FOOTER
    )
    llm = get_llm(llm_type)
    chain = prompt | llm

    for chunk in chain.stream({"variables": variables}):
        if hasattr(chunk, "content"):
            yield chunk.content
        else:
            yield str(chunk)
