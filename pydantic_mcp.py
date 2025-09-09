from mcp.server.fastmcp import FastMCP

mcp = FastMCP("MathToolServer", port=8000)

@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b

@mcp.tool()
def subtract(a: int, b: int) -> int:
    return a - b

@mcp.tool()
def odd_numbers(n: int) -> list[int]:
    return [i for i in range(1, n + 1, 2)]

if __name__ == "__main__":
    mcp.run_sse_async()
