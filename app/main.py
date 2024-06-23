from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
import db

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.on_event("startup")
def on_startup():
    db.init_db()

@app.get("/")
async def read_root(request: Request):
    context = {
        "request": request,
        "stars": 666,
        "diamonds": 777,
        "name": 'Никита тест'
    }
    return templates.TemplateResponse("index.html", context)

@app.get("/game")
async def play_game(request: Request):
    return templates.TemplateResponse("game.html", {"request": request})

@app.get("/api/clicks")
async def get_clicks():
    count = db.get_click_count()
    return JSONResponse(content={"count": count})

@app.post("/api/clicks")
async def update_clicks():
    current_count = db.get_click_count()
    new_count = current_count + 1
    db.update_click_count(new_count)
    db.set_name(1, 'Никита')
    return JSONResponse(content={"count": new_count})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
