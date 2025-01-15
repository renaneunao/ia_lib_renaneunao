import operator
from typing import Annotated, Sequence
from typing_extensions import TypedDict
from langgraph.graph import END, START, StateGraph


class State(TypedDict):
    aggregate: Annotated[list, operator.add]
    command: str  # Comando inicial do usuário
    bugs_found: dict  # Ex.: {"flask_routes": True, "javascript": False}
    improvements_found: dict  # Ex.: {"flask_routes": True, "javascript": False}
    critical_errors_found: bool


class AgentAction:
    def __init__(self, description: str):
        self._description = description

    def __call__(self, state: State) -> State:
        print(f"Executing: {self._description} | State: {state['aggregate']}")
        return {"aggregate": state["aggregate"] + [self._description]}


# Tipos de arquivos
file_types = {
    "flask_routes": "Rotas Flask",
    "javascript": "JavaScript",
    "html": "HTML",
    "css": "CSS",
    "python_utils": "Utilitários Python",
}

# Construção do fluxo
builder = StateGraph(State)

# Start
builder.add_node("start", AgentAction("Recebe comando inicial do usuário"))
builder.add_edge(START, "start")

# Agente Idealizador
builder.add_node("ideator_agent", AgentAction("Define os requisitos do projeto"))
builder.add_edge("start", "ideator_agent")

# Agente Implementador
builder.add_node("implementer_agent", AgentAction("Implementa o projeto"))
builder.add_edge("ideator_agent", "implementer_agent")

# Agente Criador e Crítico Específicos para Flask Routes
creator_node = "flask_routes_creator"
builder.add_node(creator_node, AgentAction("Cria arquivo de Rotas Flask"))
builder.add_edge("implementer_agent", creator_node)

critic_node = "flask_routes_critic"
builder.add_node(critic_node, AgentAction("Verifica bugs no arquivo de Rotas Flask"))
builder.add_edge(creator_node, critic_node)

def flask_routes_critic_decision(state: State) -> Sequence[str]:
    return ["implementer_agent"] if state["bugs_found"].get("flask_routes", False) else ["flask_routes_improver"]

builder.add_conditional_edges(critic_node, flask_routes_critic_decision, ["implementer_agent", "flask_routes_improver"])

improver_node = "flask_routes_improver"
builder.add_node(improver_node, AgentAction("Procura melhorias no arquivo de Rotas Flask"))
builder.add_edge(critic_node, improver_node)

def flask_routes_improver_decision(state: State) -> Sequence[str]:
    return ["implementer_agent"] if state["improvements_found"].get("flask_routes", False) else ["implementer_agent"]

builder.add_conditional_edges(improver_node, flask_routes_improver_decision, ["implementer_agent", "implementer_agent"])

# Agente Criador e Crítico Específicos para JavaScript
creator_node_js = "javascript_creator"
builder.add_node(creator_node_js, AgentAction("Cria arquivo de JavaScript"))
builder.add_edge("implementer_agent", creator_node_js)

critic_node_js = "javascript_critic"
builder.add_node(critic_node_js, AgentAction("Verifica bugs no arquivo de JavaScript"))
builder.add_edge(creator_node_js, critic_node_js)

def javascript_critic_decision(state: State) -> Sequence[str]:
    return ["implementer_agent"] if state["bugs_found"].get("javascript", False) else ["javascript_improver"]

builder.add_conditional_edges(critic_node_js, javascript_critic_decision, ["implementer_agent", "javascript_improver"])

improver_node_js = "javascript_improver"
builder.add_node(improver_node_js, AgentAction("Procura melhorias no arquivo de JavaScript"))
builder.add_edge(critic_node_js, improver_node_js)

def javascript_improver_decision(state: State) -> Sequence[str]:
    return ["implementer_agent"] if state["improvements_found"].get("javascript", False) else ["implementer_agent"]

builder.add_conditional_edges(improver_node_js, javascript_improver_decision, ["implementer_agent", "implementer_agent"])

# Agente Criador e Crítico Específicos para HTML
creator_node_html = "html_creator"
builder.add_node(creator_node_html, AgentAction("Cria arquivo de HTML"))
builder.add_edge("implementer_agent", creator_node_html)

critic_node_html = "html_critic"
builder.add_node(critic_node_html, AgentAction("Verifica bugs no arquivo de HTML"))
builder.add_edge(creator_node_html, critic_node_html)

def html_critic_decision(state: State) -> Sequence[str]:
    return ["implementer_agent"] if state["bugs_found"].get("html", False) else ["html_improver"]

builder.add_conditional_edges(critic_node_html, html_critic_decision, ["implementer_agent", "html_improver"])

improver_node_html = "html_improver"
builder.add_node(improver_node_html, AgentAction("Procura melhorias no arquivo de HTML"))
builder.add_edge(critic_node_html, improver_node_html)

def html_improver_decision(state: State) -> Sequence[str]:
    return ["implementer_agent"] if state["improvements_found"].get("html", False) else ["implementer_agent"]

builder.add_conditional_edges(improver_node_html, html_improver_decision, ["implementer_agent", "implementer_agent"])

# Agente Criador e Crítico Específicos para CSS
creator_node_css = "css_creator"
builder.add_node(creator_node_css, AgentAction("Cria arquivo de CSS"))
builder.add_edge("implementer_agent", creator_node_css)

critic_node_css = "css_critic"
builder.add_node(critic_node_css, AgentAction("Verifica bugs no arquivo de CSS"))
builder.add_edge(creator_node_css, critic_node_css)

def css_critic_decision(state: State) -> Sequence[str]:
    return ["implementer_agent"] if state["bugs_found"].get("css", False) else ["css_improver"]

builder.add_conditional_edges(critic_node_css, css_critic_decision, ["implementer_agent", "css_improver"])

improver_node_css = "css_improver"
builder.add_node(improver_node_css, AgentAction("Procura melhorias no arquivo de CSS"))
builder.add_edge(critic_node_css, improver_node_css)

def css_improver_decision(state: State) -> Sequence[str]:
    return ["implementer_agent"] if state["improvements_found"].get("css", False) else ["implementer_agent"]

builder.add_conditional_edges(improver_node_css, css_improver_decision, ["implementer_agent", "implementer_agent"])

# Agente Criador e Crítico Específicos para Python Utils
creator_node_python = "python_utils_creator"
builder.add_node(creator_node_python, AgentAction("Cria arquivo de Utilitários Python"))
builder.add_edge("implementer_agent", creator_node_python)

critic_node_python = "python_utils_critic"
builder.add_node(critic_node_python, AgentAction("Verifica bugs no arquivo de Utilitários Python"))
builder.add_edge(creator_node_python, critic_node_python)

def python_utils_critic_decision(state: State) -> Sequence[str]:
    return ["implementer_agent"] if state["bugs_found"].get("python_utils", False) else ["python_utils_improver"]

builder.add_conditional_edges(critic_node_python, python_utils_critic_decision, ["implementer_agent", "python_utils_improver"])

improver_node_python = "python_utils_improver"
builder.add_node(improver_node_python, AgentAction("Procura melhorias no arquivo de Utilitários Python"))
builder.add_edge(critic_node_python, improver_node_python)

def python_utils_improver_decision(state: State) -> Sequence[str]:
    return ["implementer_agent"] if state["improvements_found"].get("python_utils", False) else ["implementer_agent"]

builder.add_conditional_edges(improver_node_python, python_utils_improver_decision, ["implementer_agent", "implementer_agent"])

# Consolidar após criação e revisão de arquivos
builder.add_node("all_files_done", AgentAction("Todos os arquivos criados e revisados"))
for file_type in file_types.keys():
    builder.add_edge(f"{file_type}_improver", "all_files_done")

# Agente Crítico do Projeto Inteiro
builder.add_node("project_critic", AgentAction("Avalia bugs no projeto completo"))
builder.add_edge("all_files_done", "project_critic")

# Condicional: Bugs no projeto inteiro?
def project_critic_decision(state: State) -> Sequence[str]:
    if state["critical_errors_found"]:
        return ["implementer_agent"]  # Volta para o implementador se houver erros críticos
    else:
        return ["project_improver"]  # Vai para o agente de melhorias no projeto

builder.add_conditional_edges("project_critic", project_critic_decision, ["implementer_agent", "project_improver"])

# Agente Melhorador do Projeto Inteiro
builder.add_node("project_improver", AgentAction("Procura melhorias no projeto completo"))
builder.add_edge("project_critic", "project_improver")

# Condicional: Melhorias encontradas no projeto inteiro?
def project_improver_decision(state: State) -> Sequence[str]:
    if state["improvements_found"]:  # Se melhorias foram encontradas
        return ["implementer_agent"]  # Volta para o implementador
    else:
        return ["debugger_agent"]  # Se não houver melhorias, vai para o agente de depuração

builder.add_conditional_edges("project_improver", project_improver_decision, ["implementer_agent", "debugger_agent"])

# Agente Depurador Final
builder.add_node("debugger_agent", AgentAction("Procura erros críticos finais"))
builder.add_edge("project_improver", "debugger_agent")

# Condicional: Erros críticos encontrados?
def final_debugger_decision(state: State) -> Sequence[str]:
    if state["critical_errors_found"]:  # Se erros críticos forem encontrados
        return ["implementer_agent"]  # Volta para o implementador
    else:
        return [END]  # Se não houver erros, o fluxo termina

builder.add_conditional_edges("debugger_agent", final_debugger_decision, ["implementer_agent", END])

# Compilando o grafo
graph = builder.compile()

# Gerando a visualização em PNG
png_data = graph.get_graph().draw_mermaid_png()
with open("flow_project_creator.png", "wb") as f:
    f.write(png_data)

# Exibindo diretamente no IPython
from IPython.display import display, Image
display(Image("flow_project_creator.png"))
