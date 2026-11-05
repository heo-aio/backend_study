from typing import Dict, Any

from fastapi import APIRouter
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
from pydantic import BaseModel

router = APIRouter(prefix="/ask", tags=["ask"])

class Question(BaseModel):
    q: str

llm_model = ChatOllama(model="gemma4:e4b")

prompt = ChatPromptTemplate.from_messages([
    ("system", "당신은 사용자가 물어보는 질문에 친절히 답변해주는 IT분야 전문가입니다. 알기 쉽게 예시를 포함해 답을 해주세요."),
    ("human", "{topic}에 대해서 설명해주세요.")
])

chain = prompt | llm_model | StrOutputParser()

@router.post("/batch")
def get_answer(question: Question):
    answer = chain.invoke({"topic": question.q})
    return {"answer": answer}


