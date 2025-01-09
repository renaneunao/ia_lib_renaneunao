def get_llm(model_name, temperature, api_key):
    """
    Função que retorna um modelo de linguagem (LLM) específico com base no nome fornecido.

    Parâmetros:
    -----------
    model_name : str
        O nome do modelo que você deseja usar. As opções disponíveis são:
        - "gemini-1.5-flash": Modelo Gemini 1.5 Flash da Google Generative AI.
        - "gemini-1.5-pro": Modelo Gemini 1.5 Pro da Google Generative AI.
        - "gemini-pro": Modelo Gemini Pro da Google Generative AI.
        - "gpt-3.5-turbo": Modelo GPT-3.5 Turbo da OpenAI.
        - "gpt-4o-mini": Modelo GPT-4O Mini da OpenAI.
        - "gpt-4o": Modelo GPT-4O da OpenAI.
        - "llama3": Modelo LLaMA 3 da Ollama.
        - "llama3.1:8b": Modelo LLaMA 3.1 8b da Ollama.
        - "default_nlpcloud": Modelo NLP Cloud padrão.

    temperature : float
        Parâmetro que controla a aleatoriedade da resposta do modelo.
        Valores mais baixos (ex: 0.2) tornam o modelo mais determinístico, enquanto valores mais altos (ex: 0.8) aumentam a criatividade das respostas.

    api_key : str
        Chave de API para autenticação com os modelos da Google Generative AI ou OpenAI.
        Este parâmetro é necessário para os modelos que requerem autenticação, como Gemini e GPT.

    Retorno:
    --------
    model : LLM
        Um objeto de modelo de linguagem configurado de acordo com os parâmetros fornecidos.
        O modelo retornado pode ser um dos seguintes:
        - ChatGoogleGenerativeAI (para modelos da Google).
        - ChatOpenAI (para modelos da OpenAI).
        - ChatOllama (para modelos LLaMA da Ollama).
        - NLPCloud (para o modelo padrão do NLP Cloud).

    Exceções:
    ----------
    ValueError:
        Se o nome do modelo fornecido não for válido, uma exceção será levantada.

    Exemplos:
    ---------
    >>> model = get_llm("gpt-3.5-turbo", 0.7, "your_openai_api_key")
    >>> response = model("Qual é a capital da França?")
    >>> print(response)

    >>> model = get_llm("gemini-1.5-flash", 0.5, "your_google_api_key")
    >>> response = model("Como funciona a energia solar?")
    >>> print(response)
    """
    from langchain_community.chat_models import ChatOllama
    from langchain_openai import ChatOpenAI
    from langchain_google_genai import ChatGoogleGenerativeAI
    from langchain_community.llms import NLPCloud

    if model_name == "gemini-1.5-flash":
        return ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=temperature, google_api_key=api_key)
    elif model_name == "gemini-1.5-pro":
        return ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=temperature, google_api_key=api_key)
    elif model_name == "gemini-pro":
        return ChatGoogleGenerativeAI(model="gemini-pro", temperature=temperature, google_api_key=api_key)
    elif model_name == "gpt-3.5-turbo":
        return ChatOpenAI(model="gpt-3.5-turbo", temperature=temperature, openai_api_key=api_key)
    elif model_name == "gpt-4o-mini":
        return ChatOpenAI(model="gpt-4o-mini", temperature=temperature, openai_api_key=api_key)
    elif model_name == "gpt-4o":
        return ChatOpenAI(model="gpt-4o", temperature=temperature, openai_api_key=api_key)
    elif model_name == "llama3":
        return ChatOllama(model="llama3", temperature=temperature)
    elif model_name == "llama3.1:8b":
        return ChatOllama(model="llama3.1:8b", temperature=temperature)
    elif model_name == "default_nlpcloud":
        return NLPCloud()
    else:
        raise ValueError(f"Modelo '{model_name}' não reconhecido. Escolha entre os modelos válidos.")
