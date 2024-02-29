from dotenv import load_dotenv
import os

load_dotenv()

# Gemini

from langchain_google_genai import (ChatGoogleGenerativeAI, GoogleGenerativeAI)

llm = ChatGoogleGenerativeAI(model="gemini-pro",google_api_key=os.getenv("GOOGLE_API_KEY"),temperature=0.9)

llm_response  = llm.invoke("Give me the largest country in the world")

print(llm_response.content)