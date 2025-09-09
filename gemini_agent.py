from pydantic_ai import Agent
from pydantic_ai.models.google import GoogleModel
from pydantic_ai.providers.google import GoogleProvider
from pydantic_ai.mcp import MCPServerStdio, MCPServerSSE
from dotenv import load_dotenv
import os


load_dotenv(dotenv_path="C:/Users/PC/Desktop/research/pydantic-framework/.env")
key = os.getenv('GOOGLE_API_KEY')

# Configure LLM
provider = GoogleProvider(api_key=key)
model = GoogleModel("gemini-2.0-flash", provider=provider)

# Choose a toolset transport:
# For subprocess stdio:
# stdio_tools = MCPServerStdio(
#     "python", args=["mcp_server.py"], timeout=10
# )

stdio_tools = MCPServerStdio(
    r"C:\Users\PC\Desktop\lunafire_x\lisa_pa_mcp\.venv\Scripts\python.exe",  # Full path to Python in your venv
    args=[r"C:\Users\PC\Desktop\lunafire_x\lisa_pa_mcp\basic_mcp.py"], 
    timeout=10,
    cwd=r"C:\Users\PC\Desktop\research\pydantic-framework"  # Working directory should be a folder, not a .py file
)

# Or for HTTP/SSE:
# sse_tools = MCPServerSSE("http://localhost:8000/mcp")

agent = Agent(
    model,
    toolsets=[stdio_tools],  # or [sse_tools] depending on how server runs
    system_prompt="You are a math assistant. Use the available tools to answer correctly."
)

async def main():
    async with agent:
        prompt = '''
            what is 50*300
        '''
        res1 = await agent.run(prompt)
        print(res1.output)

import asyncio
asyncio.run(main())
