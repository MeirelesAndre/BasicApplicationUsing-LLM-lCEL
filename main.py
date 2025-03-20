# IMPORTAÇÃO DAS BIBLIOTECAS
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv, find_dotenv
import os

# CARREGANDO AS VARIÁVEIS DE AMBIENTE
load_dotenv(find_dotenv())
groq_api_key = os.getenv("GROQ_API_KEY")

# CRIAR O MODELO GROQ
llm = ChatGroq(
    model="Gemma2-9b-It",  # MODELO DE LLM UTILIZADO
    groq_api_key=groq_api_key,  # CHAVE DE API DO GROQ
)

# PASSER DE SAÍDA: isso é necessário para que o sistema entenda a saída do modelo
parser = StrOutputParser()

# CRIAR PROMPT
generic_template = "Translate the following into {language}"

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", generic_template),
        ("user", "{text}")
    ]
)

# CHAIN
chain = prompt | llm | parser

# Executor
chain.invoke({'language': 'French', 'text': 'hello'})
