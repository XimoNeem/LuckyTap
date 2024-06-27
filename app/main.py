from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
import databaseHandler

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.on_event("startup")
def on_startup():
    databaseHandler.init_db()

@app.get("/")
async def read_root(request: Request):
    context = {
        "request": request,
        "stars": 666,
        "diamonds": 77777777,
        "name": 'Никита тест'
    }
    return templates.TemplateResponse("test.html", context)

@app.get("/game")
async def get_game(request: Request):
    return templates.TemplateResponse("game.html", {"request": request})

@app.get("/settings")
async def get_settings(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("settings.html", context)

@app.get("/wallet")
async def get_settings(request: Request):
    return templates.TemplateResponse("wallet.html", {"request": request})

@app.get("/mine")
async def get_settings(request: Request):
    return templates.TemplateResponse("mine.html", {"request": request})

@app.get("/friends")
async def get_settings(request: Request):
    return templates.TemplateResponse("friends.html", {"request": request})

@app.get("/earn")
async def get_settings(request: Request):
    return templates.TemplateResponse("earn.html", {"request": request})

@app.get("/airdrop")
async def get_settings(request: Request):
    return templates.TemplateResponse("airdrop.html", {"request": request})
# === API ===

@app.get("/api/clicks")
async def get_clicks():
    count = databaseHandler.get_click_count()
    return JSONResponse(content={"count": count})

@app.post("/api/clicks")
async def update_clicks():
    current_count = databaseHandler.get_click_count()
    new_count = current_count + 1
    databaseHandler.update_click_count(new_count)
    databaseHandler.set_name(1, 'Никита')
    return JSONResponse(content={"count": new_count})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
