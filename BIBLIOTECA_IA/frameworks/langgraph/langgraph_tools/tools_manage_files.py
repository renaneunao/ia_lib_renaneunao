from typing import Annotated
from langchain.tools import tool
from pathlib import Path

# Função para criar um arquivo
@tool
def create_file(working_directory: Annotated[str, "Working directory to resolve file path."],
                file_path: Annotated[str, "Relative path to create the file."],
                content: Annotated[str, "Content of the file."]):
    """
    Creates a new file at the specified path (relative to the working directory) and writes the provided content into it.
    If the file already exists, it will be overwritten with the new content.

    Arguments:
    - working_directory (str): The directory where the file will be created.
    - file_path (str): The relative path (including file name) where the new file will be created.
    - content (str): The content that will be written inside the file.

    Example:
    create_file("/home/user", "example.txt", "Hello, world!")
    """
    path = Path(working_directory) / file_path  # Resolve full path
    # Verifica se o arquivo já existe e o reescreve se necessário
    path.write_text(content)
    return f"File created or overwritten at {path}"

# Função para modificar um arquivo
@tool
def modify_file(working_directory: Annotated[str, "Working directory to resolve file path."],
                file_path: Annotated[str, "Relative path to the file to modify."],
                content: Annotated[str, "New content to append."]):
    """
    Appends new content to an existing file specified by `file_path`.

    Arguments:
    - working_directory (str): The directory where the file is located.
    - file_path (str): The relative path to the file that needs to be modified.
    - content (str): The new content that will be appended to the file.

    Example:
    modify_file("/home/user", "example.txt", "\nNew line added!")
    """
    path = Path(working_directory) / file_path  # Resolve full path
    with path.open("a") as file:
        file.write(content)
    return f"Content appended to {file_path}"

# Função para excluir um arquivo
@tool
def delete_file(working_directory: Annotated[str, "Working directory to resolve file path."],
                file_path: Annotated[str, "Relative path to the file to delete."]):
    """
    Deletes a file at the specified `file_path`.

    Arguments:
    - working_directory (str): The directory where the file is located.
    - file_path (str): The relative path to the file that needs to be deleted.

    Example:
    delete_file("/home/user", "example.txt")
    """
    path = Path(working_directory) / file_path  # Resolve full path
    if path.exists():
        path.unlink()
        return f"File {file_path} deleted."
    else:
        return f"File {file_path} does not exist."

# Função para criar um diretório
@tool
def create_directory(working_directory: Annotated[str, "Working directory to resolve directory path."],
                     directory_path: Annotated[str, "Relative path of the directory to create."]):
    """
    Creates a directory at the specified `directory_path`. If any intermediate directories
    do not exist, they will be created as well.

    Arguments:
    - working_directory (str): The directory where the new directory will be created.
    - directory_path (str): The relative path where the new directory will be created.

    Example:
    create_directory("/home/user", "new_folder/sub_folder")
    """
    path = Path(working_directory) / directory_path  # Resolve full path
    path.mkdir(parents=True, exist_ok=True)
    return f"Directory {directory_path} created."

# Função para excluir um diretório
@tool
def delete_directory(working_directory: Annotated[str, "Working directory to resolve directory path."],
                     directory_path: Annotated[str, "Relative path of the directory to delete."]):
    """
    Deletes a directory at the specified `directory_path`, including all its files and subdirectories.

    Arguments:
    - working_directory (str): The directory where the target directory is located.
    - directory_path (str): The relative path to the directory to delete.

    Example:
    delete_directory("/home/user", "old_folder")
    """
    path = Path(working_directory) / directory_path  # Resolve full path
    if path.exists() and path.is_dir():
        for child in path.iterdir():
            if child.is_file():
                child.unlink()
            else:
                delete_directory(str(child))  # Recursively delete subdirectories
        path.rmdir()
        return f"Directory {directory_path} deleted."
    else:
        return f"Directory {directory_path} does not exist."
