from langchain_core.prompts import PromptTemplate

from llm_picker import get_llm


def generate_response(llm_type: str, template: str, variables: str):
    prompt = PromptTemplate(
        input_variables=["variables"],
        template=template
    )
    llm = get_llm(llm_type)

    chain = prompt | llm

    return chain.invoke(input={"variables": variables})
