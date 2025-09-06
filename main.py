from dotenv import load_dotenv
import os
from pydantic_ai import Agent
from pydantic_ai.models.google import GoogleModel
from pydantic_ai.providers.google import GoogleProvider

def main():
    load_dotenv(dotenv_path="C:/Users/PC/Desktop/research/pydantic-framework/.env")
    key = os.getenv('GOOGLE_API_KEY')
    print(key)
    
    # Create provider with API key
    provider = GoogleProvider(api_key=key)
    
    # Initialize Gemini model
    model = GoogleModel("gemini-2.0-flash", provider=provider)
    
    # Create agent
    agent = Agent(model)
    
    # Example usage
    result = agent.run_sync('What is a noun?')
    print(result.output)



if __name__ == "__main__":
    main()
