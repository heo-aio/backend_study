import logging
import os
import shutil
import traceback
import uuid
from typing import List

from fastapi import FastAPI, UploadFile
from starlette.responses import RedirectResponse
from starlette.staticfiles import StaticFiles

app = FastAPI()

logging.basicConfig(
    level = logging.INFO,
    format = "%(levelname)s:      [%(name)s] %(message)s - %(asctime)s",
    datefmt = "%Y-%m-%d %H:%M:%S"
)

logger = logging.getLogger(__name__)
# logger.info("현재 모듈의 메시지")
# logging.info("root logger 메시지")
logger.info("logger test")

FILE_PATH = "./upload"

if not os.path.exists(FILE_PATH):
    os.mkdir(FILE_PATH)
    logger.info(f"{FILE_PATH} 생성")

app.mount("/view", StaticFiles(directory="view"))
app.mount("/images", StaticFiles(directory=FILE_PATH))

@app.get("/")
def main():
    return RedirectResponse("/view/upload.html")

@app.post("/upload")
def upload(files: List[UploadFile]):
    msg = "파일 업로드 실패"

    if not files or all(file.filename == "" for file in files):
        logger.warning("업로드된 파일이 없습니다.")
        return {"message" : "업로드할 파일을 1개이상 선택해주세요."}

    try:
        for file in files:
            logger.info(f"file name : {file.filename}")
            ori_filename = file.filename

            # 1. 파일명과 확장자 분리
            name, ext = os.path.splitext(ori_filename) # ext : 확장자
            logger.info(f"파일명 : {name}, 확장자 : {ext}")

            # 2. 파일명 변경 + 3. 바꾼 파일명과 확장자 합치기
            new_filename = f"{uuid.uuid4()}{ext}"
            logger.info(f"새 파일명 : {new_filename}")

            # 4. 파일 저장
            save_path = f"{FILE_PATH}/{new_filename}"
            with open(save_path, "wb") as file_object:
                # shutil : 파일과 폴더를 복사, 이동, 삭제하는 고수준 도구 모음
                shutil.copyfileobj(file.file, file_object)

            msg = "파일 업로드 완료"
    except Exception as e:
        logger.error(e)
        logger.error(traceback.format_exc())

    return {"message" : msg}

@app.get("/files")
def files():
    # os.listdir : 특정 경로 파일 리스트 가져올 수 있음
    file_list = os.listdir(FILE_PATH)
    logger.info(file_list)
    return {"올라와 있는 파일:" : file_list}

@app.get("/delete")
def delete(filename: str):
    path = f"{FILE_PATH}/{filename}"
    if os.path.exists(path):
        os.remove(path)
    return RedirectResponse("/view/file_list.html")


