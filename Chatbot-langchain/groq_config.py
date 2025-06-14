from langchain_groq import ChatGroq

def get_groq_llm():
    return ChatGroq(
        model_name="llama3-8b-8192",
        groq_api_key="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",
        temperature=0.5
    )
