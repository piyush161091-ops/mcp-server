import subprocess
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("git-tools-server")

@mcp.tool()
def health() ->str:
    """Check if the server is healthy."""
    return "MCP server is running and healthy."

@mcp.tool()
def get_conflicted_files() -> list:
    """Returns a list of files that are currently in conflict."""
    try:
        result = subprocess.check_output(["git", "diff", "--name-only", "--diff-filter=U"])
        files = result.decode().splitlines()
        return files
    except Exception as e:
        return [str(e)]

@mcp.tool()
def read_file(file_path: str) -> str: 
    """Read the contents of a file."""
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        return str(e)
    
if __name__ =="__main__":
    mcp.run()