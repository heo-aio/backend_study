import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s:      [%(name)s] %(message)s - %(asctime)s]",
    datefmt="%Y-%m-%d %H:%M:%S",
)

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from starlette.staticfiles import StaticFiles

from ollama_router import router

app = FastAPI()

app.mount("/view", StaticFiles(directory="view"))

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"])


@app.get("/")
def main():
    return RedirectResponse("/view/ollama_index.html")

app.include_router(router=router)