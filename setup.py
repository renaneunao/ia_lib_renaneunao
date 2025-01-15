from setuptools import setup, find_packages
import os

# Caminho do README.md para o long_description
readme_path = os.path.join(os.path.dirname(__file__), "README.md")

# Lendo o conteúdo do README.md
with open(readme_path, "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="ia_lib_renaneunao",
    version="0.0.1",
    description="Biblioteca de IA desenvolvida por @renaneunao",
    long_description_content_type="text/markdown",
    author="@renaneunao",
    author_email="renan_vianna7@icloud.com",
    url="https://github.com/renaneunao/ia_lib_renaneunao",
    packages=find_packages(include=["BIBLIOTECA_IA", "BIBLIOTECA_IA.*"]),
    include_package_data=True,  # Inclui dados do MANIFEST.in
    install_requires=[
        "python-dotenv",
        "langchain",
        "langchain_community",
        "langchain_openai",
        "langchain_google_genai",
        "langgraph",
        "ipython",
        "faiss-cpu",
        "PyPDF2",
        "streamlit",
        "flask",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)