import logging
import os

from fastapi import FastAPI
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
def upload():
    pass
