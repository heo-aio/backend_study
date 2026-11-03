from fastapi import FastAPI
from starlette.requests import Request

app = FastAPI()

@app.get("/")
def main():
    return {"message": "FastAPI 공부 메인 페이지"}

# 경로 매개변수 -> URL경로 자체가 값
# http://127.0.0.1:8000/users/10
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

# 쿼리 매개변수 -> ? 뒤에 key = value
# /search?keyword=apple&limit=10
@app.get("/search")
def search(keyword: str, limit: int = 10):
    return {"keyword" : keyword, "limit" : limit}

@app.get("/books/{book_id}")
def get_book(book_id: int, detail: bool = False):
    result = {"book_id" : book_id}
    if detail:
        result["detail"] = detail
    return result

@app.get("/setInfo") # 이게 path
def setInfo(req: Request):
    print(f"host : {req.client.host} : {req.client.port}")
    print(f"path:{req.url.path}") # domain : port 뒤에 오는 주소
    # /setInfo?userName=허정모&gender=male&hobby=coding&hobby=게임&hobby=야구보기
    name = req.query_params.get("userName")
    gender = req.query_params.get("gender")
    hobby = req.query_params.getlist("hobby") # 여러개일 때 list로 받기
    print(f"name : {name}")
    print(f"gender : {gender}")
    print(f"hobby : {hobby}")
    return {"msg":"OK"}


