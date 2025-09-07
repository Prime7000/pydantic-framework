from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerStdio
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.ollama import OllamaProvider


ollama_model = OpenAIChatModel(
    model_name='qwen3:0.6b',
    provider=OllamaProvider(base_url='http://localhost:11434/v1'),
)

# Choose a toolset transport:
# For subprocess stdio:
stdio_tools = MCPServerStdio(
    "python", args=["mcp_server.py"], timeout=10
)

# Or for HTTP/SSE:
# sse_tools = MCPServerSSE("http://localhost:8000/mcp")

agent = Agent(
    ollama_model,
    toolsets=[stdio_tools],  # or [sse_tools] depending on how server runs
    system_prompt="You are a math assistant. Use the available tools to answer correctly."
)

async def main():
    async with agent:
        res1 = await agent.run("Add 5 and 7")
        print("Add →", res1.output)

        res2 = await agent.run("Subtract 3 from 15")
        print("Subtract →", res2.output)

        res3 = await agent.run("List odd numbers up to 9")
        print("Odd Numbers →", res3.output)

import asyncio
asyncio.run(main())
