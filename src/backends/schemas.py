from pydantic import BaseModel
from typing import List

# 입력 모델
class QueryRequest(BaseModel):
    query: str

# 출력 모델
class QueryResponse(BaseModel):
    context: List[str]
    answer: str

