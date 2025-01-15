from langchain_core.language_models.chat_models import BaseChatModel
from langgraph.prebuilt import create_react_agent
from BIBLIOTECA_IA.frameworks.langgraph.langgraph_tools.tools_manage_files import (
    create_file,
    modify_file,
    delete_file,
    create_directory,
    delete_directory
)


class FileManagerAgent:
    def __init__(self, llm: BaseChatModel):
        # Definindo as ferramentas que o agente usará
        self.tools = [
            create_file,
            modify_file,
            delete_file,
            create_directory,
            delete_directory
        ]

        # Criando o agente reativo com as ferramentas fornecidas
        self.agent = create_react_agent(llm, tools=self.tools)

    def handle_request(self, request: str, working_directory: str, messages: list, **params) -> str:
        """
        Chama o agente reativo para lidar com a solicitação de gerenciamento de arquivos.
        """
        # Verifica se todos os parâmetros necessários estão presentes
        if 'file_path' not in params or 'content' not in params:
            raise ValueError("Parâmetros 'file_path' e 'content' são necessários.")

        # Encaminha a solicitação para o agente reativo, que decidirá qual ferramenta usar
        return self.agent.invoke({
            "request": request,
            "working_directory": working_directory,
            "messages": messages,
            **params
        })