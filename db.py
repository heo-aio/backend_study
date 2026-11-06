import logging

from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s:      [%(name)s] %(message)s - %(asctime)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/")
def main():
    return {"message" : "main page"}

@app.get("/db/connection")
def connection():
    msg = "DB 접속 실패"
    conn = None
    try:
        # 1. 접속 정보 (위치, 아이디, 비밀번호, 사용할 db)
        url = "mysql+pymysql://root:root@127.0.0.1:3306/mydb"
        # 2. 엔진 생성
        engine = create_engine(url)
        # 3. 세션생성
        session = sessionmaker(bind=engine)
        conn = session()
        msg = "DB 접속 완료"
    except Exception as e:
        logger.exception(e)
    finally:
        if conn is not None:
            conn.close()
    return {"message" : msg}