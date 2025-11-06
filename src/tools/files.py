import os
import subprocess
from agents import function_tool


@function_tool
def get_file_tree():
    """Get the file tree of the codebase.
    
    Returns:
        The file tree of the codebase.
    """
    print("[get_file_tree] Getting file tree...")
    result = subprocess.run(["tree", "."], capture_output=True, text=True)
    return result.stdout

@function_tool
def read_file(path: str, start_line: int | None = None, end_line: int | None = None) -> str:
    """Read a file and return the content, optionally starting and ending at a specific line.
    
    Args:
        path: The path to the file to read, relative to the root of the codebase.
        start_line: The line to start reading from.
        end_line: The line to end reading at.

    Returns:
        The content of the file, optionally starting and ending at a specific line.
    """
    print(f"[read_file] Reading {path}...")
    if ".env" in path:
        return f"[Error] Sorry, {path} contains sensitive stuff..."

    full_path = os.path.join(os.getcwd(), path)

    with open(full_path, "r") as file:
        lines = file.readlines()

    if end_line is not None:
        lines = lines[:end_line+1]
    if start_line is not None:
        lines = lines[start_line:]

    return "\n".join(lines)