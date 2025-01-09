def get_pdf_text(document_path):
    """
    Função que extrai todo o texto de um arquivo PDF.

    Esta função utiliza a biblioteca PyPDF2 para ler o conteúdo de um arquivo PDF e extrair o texto de todas as páginas do documento. O texto extraído de cada página é concatenado para formar uma única string, que é retornada como resultado.

    Parâmetros:
    -----------
    document_path : str ou file-like object
        O arquivo PDF do qual o texto será extraído. Pode ser um caminho de arquivo em formato string ou um objeto file-like (como um arquivo aberto).

    Retorno:
    --------
    str
        O texto extraído do documento PDF. Se o documento contiver várias páginas, o texto será concatenado em uma única string.

    Exceções:
    ----------
    ValueError:
        Se o arquivo fornecido não for um arquivo PDF válido.

    Exemplos:
    ---------
    >>> document_path = "path/to/document.pdf"
    >>> text = get_pdf_text(document_path)
    >>> print(text)  # Exibe o texto extraído do PDF.
    """
    from PyPDF2 import PdfReader

    text = ""
    pdf_reader = PdfReader(document_path)
    for page in pdf_reader.pages:
        page_text = page.extract_text() or ""
        text += page_text

    return text


def get_chunks(text, chunk_size=3000, chunk_overlap=1000):
    """
    Função que divide o texto em chunks de tamanho fixo, com sobreposição entre eles.

    Esta função usa a classe `RecursiveCharacterTextSplitter` da biblioteca `langchain` para dividir um texto longo em partes menores (chunks). O tamanho de cada chunk e a sobreposição entre eles podem ser configurados através dos parâmetros da função. Isso é útil quando o texto é grande demais para ser processado de uma vez por modelos de linguagem ou embeddings.

    Parâmetros:
    -----------
    text : str
        O texto a ser dividido em chunks. Deve ser uma string contendo o conteúdo completo a ser processado.

    chunk_size : int, opcional
        O tamanho máximo de cada chunk (em número de caracteres). O valor padrão é 3000 caracteres.

    chunk_overlap : int, opcional
        A sobreposição entre os chunks, ou seja, o número de caracteres que serão repetidos no final de um chunk e no início do próximo. O valor padrão é 1000 caracteres.

    Retorno:
    --------
    list of str
        Uma lista de strings (chunks), onde cada string representa uma parte do texto original.
        O tamanho de cada chunk é limitado pelo parâmetro `chunk_size`, e a sobreposição entre os chunks é determinada pelo parâmetro `chunk_overlap`.

    Exceções:
    ----------
    ValueError:
        Se o texto fornecido for vazio ou não for uma string válida.

    Exemplos:
    ---------
    # Extrair o texto do PDF
        document_path = r"\Downloads\manual.pdf"
        pdf_text = text_utils.get_pdf_text(document_path)

        # Dividir o texto extraído em chunks
        chunks = text_utils.get_chunks(pdf_text, chunk_size=3000, chunk_overlap=1000)

        # Exibir os chunks divididos
        for i, chunk in enumerate(chunks):
            print(f"Chunk {i + 1}:")
            print(chunk)
            print("-" * 50)
    """
    from langchain.text_splitter import RecursiveCharacterTextSplitter

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return text_splitter.split_text(text)


def load_or_create_vector_store(text_chunks, embeddings, file_path=None, st=None, use_flask_session=None):
    import os
    from langchain_community.vectorstores import FAISS
    """
    Carrega ou cria um FAISS vector store, armazenando em diferentes lugares.

    Parameters:
    - text_chunks: Lista de strings de textos para vetorizar.
    - embeddings: O modelo de embedding a ser usado.
    - st: Se fornecido, usará o Streamlit para armazenar os vetores.
    - file_path: Caminho do arquivo para salvar/ler os vetores.
    - use_flask_session: Se True, armazenará na sessão do Flask.

    Returns:
    - vector_store: O vetor store FAISS.
    """

    # Tentativa de carregar do Streamlit
    if st:
        if 'vector_store' in st.session_state:
            vector_store = st.session_state['vector_store']
            return vector_store

    # Tentativa de carregar de arquivo
    if file_path and os.path.exists(file_path):
        vector_store = FAISS.load_local(file_path, embeddings)
        return vector_store

    # Caso não tenha sido carregado, cria o vetor
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)

    # Salva os vetores de volta ao Streamlit (se aplicável)
    if st:
        st.session_state['vector_store'] = vector_store

    # Salva em arquivo, se fornecido o caminho
    if file_path:
        vector_store.save_local(file_path)

    # Se estiver usando Flask, podemos armazenar na sessão
    if use_flask_session:
        use_flask_session['vector_store'] = vector_store

    return vector_store


def get_conversational_chain(model, prompt_template, chain_type):
    from langchain.chains.question_answering import load_qa_chain
    from langchain_core.prompts import PromptTemplate
    """
    Carrega uma cadeia de conversação para responder perguntas com base em documentos.

    Args:
        model (BaseLanguageModel): O modelo de linguagem que será usado na cadeia de conversação. Ele é responsável
        por gerar as respostas para as perguntas fornecidas com base nos documentos.

        prompt_template (str): O modelo de prompt a ser utilizado para formatar a pergunta e o contexto fornecidos.
        Esse template é responsável por estruturar a entrada do modelo de linguagem, garantindo que o contexto
        (documentos) e a pergunta sejam apresentados de maneira eficaz.

        chain_type (str): O tipo da cadeia de combinação de documentos a ser utilizada para a resposta da pergunta.
        Este parâmetro é crucial para determinar como os documentos serão combinados antes de passar para o modelo de
        linguagem. Ele pode ser um dos seguintes:
            - "stuff": Combina todos os documentos em um único bloco de texto e os fornece ao modelo de linguagem.
            Ideal para quando todos os documentos são necessários para gerar uma resposta coesa de uma vez.

            - "map_reduce": Processa os documentos separadamente em dois estágios. Primeiro, as partes dos documentos
            são processadas individualmente (map), e então um resumo ou combinação dos resultados é feito (reduce).
            Isso é útil quando os documentos são muito grandes ou numerosos e uma abordagem de "resumo" é necessária.

            - "map_rerank": Similar ao `map_reduce`, mas após o mapeamento dos documentos, eles são classificados
            novamente para determinar quais são mais relevantes para a pergunta antes de produzir a resposta final.
            Isso pode melhorar a qualidade da resposta ao dar mais peso aos documentos mais pertinentes.

            - "refine": Começa com uma resposta inicial e refina essa resposta à medida que mais documentos ou
            informações são processadas. Esse método é adequado quando é necessário aprimorar uma resposta parcial
            com base em novos dados ou insights.

    Returns:
        BaseCombineDocumentsChain: Uma cadeia configurada para responder perguntas com base nos documentos fornecidos, utilizando o modelo de linguagem, o template de prompt e o tipo de cadeia especificado.

    Exemplo:
        model = SomeLanguageModel()  # Exemplo de modelo de linguagem
        prompt_template = "Dada a informação: {context}, qual é a resposta para: {question}?"
        chain = get_conversational_chain(model, prompt_template, chain_type="stuff")
        resposta = chain.run(context=some_document_text, question="Qual é a capital da França?")
    """
    return load_qa_chain(
        model,
        chain_type=chain_type,
        prompt=PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    )
