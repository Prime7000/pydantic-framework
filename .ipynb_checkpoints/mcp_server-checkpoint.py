from fastmcp import FastMCP

# Create the FastMCP server
mcp = FastMCP("MathToolServer",
             port=8200)

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract b from a"""
    return a - b

@mcp.tool()
def odd_numbers(n: int) -> list[int]:
    """Return all odd numbers up to n, inclusive"""
    return [i for i in range(1, n + 1) if i % 2 != 0]

if __name__ == "__main__":
    mcp.run()  # Or use run_async() in async contexts
