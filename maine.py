import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fasthtml.common import *

app = FastAPI()
app.mount("/static", StaticFiles(directory="."))


def page(*args):
    conteant = Html(
        Head(
            Link(rel="stylesheet", href="static/stile.css"),
            Title("ExtraHelp"),
        ),
        Body(
            Div(
                H1("ExtraHelp"),
                *args,
                id="content",
            )
        ),
    )
    return HTMLResponse(to_xml(conteant))


@app.get("/")
async def root():
    return page(
        H3("Helping teens volunteer!"),
        A(
            "Get Started ➙",
            href="/help",
        ),
    )


interests = [
    "politics",
    "medicine",
    "environment",
    "miscellaneous",
    "aid",
    "technology",
    "business",
]


@app.get("/help")
async def input():
    return page(
        Form(
            Label("date of birth", fr="dob"),
            Input(name="dob", id="dob", type="date"),
            *[
                Div(
                    Input(type="checkbox", name=interest, id=interest),
                    Label(interest, fr=interest),
                )
                for interest in interests
            ],
        ),
        Script(
            src = '/static/location.js' 
        ),
    )


if __name__ == "__main__":
    uvicorn.run(
        "maine:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )
