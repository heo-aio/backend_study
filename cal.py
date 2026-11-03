from fastapi import FastAPI
from starlette.responses import RedirectResponse
from starlette.staticfiles import StaticFiles

app = FastAPI()

app.mount("/view", StaticFiles(directory="view"))

@app.get("/")
def main():
    # redirect : 특정 주소로 이동
    return RedirectResponse("./view/cal_index.html")

@app.get("/calc")
def calc(val1: int, oper: str, val2: int):
    print(f"{val1} {oper} {val2} = ??")
    result = 0

    if oper == "+":
        result = val1 + val2
    elif oper == "-":
        result = val1 - val2
    elif oper == "*":
        result = val1 * val2
    else:
        if val2 == 0:
            result = "0으로 나눌 수 없음"
        else:
            result = val1 / val2

    return {"result": result}

