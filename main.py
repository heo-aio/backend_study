from fastapi import FastAPI

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

