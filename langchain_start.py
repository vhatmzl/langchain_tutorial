from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# .env 파일에서 환경 변수를 로드합니다.
load_dotenv()

#환경 변수를 사용하여 API키를 불러옵니다.
openai_api_key = os.getenv("OPENAI_API_KEY")

lim = ChatOpenAI(openai_api_key=openai_api_key)

output = lim.invoke("2024년 청년 지원 정책에 대하여 알려줘")
# # client.chat.completions.create(...) 내용이랑 같다

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "너는 청년을 행복하게 하기 위한 정부정책 안내 컨설턴트야"),  # 시스템 기본 역할 내용
        ("user", "{input}")   #유저가 입력하는 내용
    ]
)
chain = prompt | lim
print(chain.invoke({"input":"2024년 청년 지원 정책에 대하여 알려줘"}))



#파싱하기
from langchain_core.output_parsers import StrOutputParser
output_parser = StrOutputParser()
chain = prompt | lim | output_parser
print(chain.invoke({"input":"2024년 청년 지원 정책에 대하여 알려줘"}))
