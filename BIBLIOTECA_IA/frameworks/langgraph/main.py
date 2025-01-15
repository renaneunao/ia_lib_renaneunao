import os
from BIBLIOTECA_IA.models.llms import get_llm
from BIBLIOTECA_IA.frameworks.langgraph.langgraph_agents.agent_file_manager import FileManagerAgent
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

# Define model parameters
model_name = "gpt-4o-mini"  # Model name
temperature = 0.7  # Model temperature
api_key = os.getenv('OPENAI_API_KEY')  # Get API key from environment

# Get the model
model = get_llm(model_name, temperature, api_key)

# Create the file manager agent with the obtained LLM
file_manager_agent = FileManagerAgent(model)

# Example request to create a file
try:
    response = file_manager_agent.handle_request(
        "create",
        "/BIBLIOTECA_IA/frameworks/langgraph",  # Working directory (can be changed as needed)
        messages=['Utilize a tool para criar o arquivo informado.'],  # Initial messages or context for the agent
        file_path="example.txt",
        content="Hello, world!"
    )
    print(response)
except Exception as e:
    print(f"Error processing request: {e}")