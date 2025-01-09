from BIBLIOTECA_IA.models import llms

import os
from dotenv import load_dotenv
load_dotenv()

api_openai = os.getenv('OPENAI_API_KEY')
llm = llms.get_llm("gpt-4o-mini", 0.7, api_openai)

