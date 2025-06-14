from langchain.chains.summarize import load_summarize_chain
from langchain.docstore.document import Document
from groq_config import get_groq_llm

def summarize_text(input_text: str):
    llm = get_groq_llm()
    docs = [Document(page_content=input_text)]
    chain = load_summarize_chain(llm, chain_type="stuff")
    summary = chain.run(docs)
    return summary
