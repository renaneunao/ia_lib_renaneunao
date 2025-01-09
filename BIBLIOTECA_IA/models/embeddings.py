def get_embeddings(embeddings_name, model, api_key):
    """
    Função que retorna uma instância de embedding específica, baseada no nome do embedding fornecido.

    A função permite que você escolha entre dois provedores de embeddings: Google e OpenAI, além de permitir a seleção do modelo específico de cada serviço.

    Parâmetros:
    -----------
    embeddings_name : str
        O nome do provedor de embeddings que você deseja usar. As opções válidas são:
        - "Google": Para usar embeddings fornecidos pela Google Generative AI.
        - "Openai": Para usar embeddings fornecidos pela OpenAI.

    model : str
        O nome do modelo a ser usado para gerar os embeddings. Modelos válidos dependem do provedor selecionado:
        - Para o provedor Google, pode ser "models/embedding-001".
        - Para o provedor OpenAI, pode ser um dos seguintes:
            - "text-embedding-3-small"
            - "text-embedding-3-large"
            - "text-embedding-ada-002"

    api_key : str
        A chave de API necessária para autenticação com os provedores de embeddings (Google ou OpenAI).
        Este parâmetro é necessário para obter acesso aos serviços de embeddings dos provedores.

    Retorno:
    --------
    embeddings : Embeddings
        Uma instância de embeddings correspondente ao provedor e modelo escolhido:
        - GoogleGenerativeAIEmbeddings (para Google).
        - OpenAIEmbeddings (para OpenAI).

    Exceções:
    ----------
    ValueError:
        Se o nome do provedor de embeddings (`embeddings_name`) não for "Google" ou "Openai".
    KeyError:
        Se o modelo selecionado não for válido para o provedor correspondente.

    Exemplos:
    ---------
    >>> embeddings = get_embeddings("Google", "models/embedding-001", "your_google_api_key")
    >>> print(embeddings)  # Google embeddings com o modelo "embedding-001"

    >>> embeddings = get_embeddings("Openai", "text-embedding-ada-002", "your_openai_api_key")
    >>> print(embeddings)  # OpenAI embeddings com o modelo "text-embedding-ada-002"
    """
    from langchain_openai import OpenAIEmbeddings
    from langchain_google_genai import GoogleGenerativeAIEmbeddings

    # Definir as instâncias de embedding
    google_embeddings = GoogleGenerativeAIEmbeddings(model=model, google_api_key=api_key)
    openai_embeddings = OpenAIEmbeddings(model=model, openai_api_key=api_key)

    if embeddings_name == "Google":
        return google_embeddings
    elif embeddings_name == "Openai":
        return openai_embeddings

    # Levanta erro caso o nome do provedor de embeddings não seja válido
    raise ValueError(f"Provedor de embeddings '{embeddings_name}' não reconhecido. Escolha entre 'Google' ou 'Openai'.")
