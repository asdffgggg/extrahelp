import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fasthtml.common import *

app = FastAPI()
app.mount("/static", StaticFiles(directory="."))


@app.get("/")
async def root():
    conteant = Html(
        Head(
            Link(rel="stylesheet", href="static/stile.css"),
            Title("ExtraHelp"),
        ),
        Body(
            Div(
                H1("ExtraHelp"),
                H3("Helping teens volunteer!"),
                A("Get Started ➙", href = "https://www.nytimes.com/games/wordle/index.html?eafs_enabled=false"),
                id="content",
            )
        ),
    )
    return HTMLResponse(to_xml(conteant))


if __name__ == "__main__":
    uvicorn.run(
        "maine:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )
