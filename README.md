# 🧠 ia_lib_renaneunao

Bem-vindo à **IA Lib**. Esta é uma biblioteca modular em Python com o propósito de empacotar aceleradores, conectores LLM, utilitários de embeddings e abordagens de geração orientada (RAG), concentrando as dependências e integrações mais comuns usadas no dia-a-dia para o desenvolvimento de robôs e agentes inteligentes.

## 🚀 Sobre o Pacote
O pacote foi customizado via `setuptools` de modo a provisionar as abstrações pesadas como um pacote de fácil setup e acoplamento em outros microserviços. Toda a lógica está injetada sob o diretório principal de classes `BIBLIOTECA_IA`.

> *Criado e mantido por [@renaneunao]*

## 🛠️ Tecnologias & Dependências Nativas (Stack)
A biblioteca faz abstrações sob demanda utilizando a melhor tecnologia de agentes linguísticos atualmente disponível:
- **LangChain & LangGraph**: Orquestração e chaining de modelos (comunidade, customizações locais e cloud baseadas em `OpenAI` e `Google GenAI`).
- **Memory & Embeddings**: FAISS-CPU embutido nas exigências de pacote para prover Vector Stores, além de conversores comnatividade em leitura de PDF (`PyPDF2`).
- **Interfaces Prototipadas Integradas**: Requerimentos nativos de `Streamlit` e `Flask` declarados no manifesto final.

## 📦 Como Usar em seus Projetos
Para acoplar os scripts nas suas soluções e usar os conectores e cadeias pré-forjadas no seu sistema basta clonar ou referenciar esse repositório pelo pip:

```bash
# Rodando a instalação através de um ambiente virtual
pip install git+https://github.com/renaneunao/ia_lib_renaneunao.git
```
Ou no seu diretório de repositório clornado:
```bash
pip install -e .
```
Importando nos seus módulos IA:
```python
from BIBLIOTECA_IA.seu_modulo_desejado import Utils
# Continue a codar rapidamente
```
