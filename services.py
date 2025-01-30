from langchain_core.prompts import PromptTemplate

from llm_picker import get_llm

LINE_BREAK = "\n"
TEMPLATE_HEADER = "Given the {options} I want you to create:" + LINE_BREAK
TEMPLATE_FOOTER = LINE_BREAK + "Answer in KOREAN"


def generate_response(llm_type: str, template_content: str, options: str):
    prompt = PromptTemplate(
        input_variables=["options"],
        template=TEMPLATE_HEADER + template_content + TEMPLATE_FOOTER
    )
    llm = get_llm(llm_type)
    chain = prompt | llm
    i = 0

    for chunk in chain.stream({"options": options}):
        if hasattr(chunk, "content"):
            i += 1
            print("chunk " + str(i) + ": ", chunk)
            yield chunk.content
        else:
            yield str(chunk)
