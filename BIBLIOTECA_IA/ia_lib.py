def get_llm(self, model_name, temperature):
    from langchain_community.chat_models import ChatOllama
    from langchain_openai import ChatOpenAI
    from langchain_google_genai import ChatGoogleGenerativeAI
    from langchain_community.llms import NLPCloud

    if model_name == "gemini-1.5-flash":
        return ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=temperature)
    elif model_name == "gemini-1.5-pro":
        return ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=temperature)
    elif model_name == "gemini-pro":
        return ChatGoogleGenerativeAI(model="gemini-pro", temperature=temperature)
    elif model_name == "gpt-3.5-turbo":
        return ChatOpenAI(model="gpt-3.5-turbo", temperature=temperature)
    elif model_name == "gpt-4o-mini":
        return ChatOpenAI(model="gpt-4o-mini", temperature=temperature)
    elif model_name == "gpt-4o":
        return ChatOpenAI(model="gpt-4o", temperature=temperature)
    elif model_name == "llama3":
        return ChatOllama(model="llama3", temperature=temperature)
    elif model_name == "llama3.1:8b":
        return ChatOllama(model="llama3.1:8b", temperature=temperature)
    elif model_name == "default_nlpcloud":
        return NLPCloud()


def get_embeddings(self, embeddings_name, model):
    from langchain_openai import OpenAIEmbeddings
    from langchain_google_genai import GoogleGenerativeAIEmbeddings

    # Definir as instâncias de embedding
    google_embeddings = GoogleGenerativeAIEmbeddings(model=model)
    openai_embeddings = OpenAIEmbeddings(model=model)
    if embeddings_name == "Google":
        return google_embeddings
    elif embeddings_name == "Openai":
        return openai_embeddings