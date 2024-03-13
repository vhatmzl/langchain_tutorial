from dotenv import load_dotenv
import os
from openai import OpenAI
from langchain_openai import ChatOpenAI

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
MODEL="gpt-3.5-turbo"
lim = ChatOpenAI(openai_api_key)

output = lim.invoke("2024년 청년 지원 정책에 대하여 알려줘")
# client.chat.completions.create(...) 내용이랑 같다