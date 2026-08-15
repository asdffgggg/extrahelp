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
            href="/stage1",
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


@app.get("/stage1")
async def stage1():
    return page(
        Form(
            Label("date of birth", fr="dob"),
            Input(name="dob", id="dob", type="date"),
            P("Interests:"),
            *[
                Div(
                    Input(type="checkbox", name=interest, id=interest),
                    Label(interest, fr=interest),
                )
                for interest in interests
            ],
            Input(id="lat", name="lat", style="display:none"),
            Input(id="lon", name="lon", style="display:none"),
            Button("next", type="submit"),
            action="/stage2",
            method="POST",
        ),
        Script(src="/static/location.js"),
    )

goals = ["Better teamwork"]

@app.post("/stage2")
async def stage2(request: Request):
    data = dict(await request.form())
    print(data)
    return page(
        Form(
            P("Goals:"),
            *[
                Div(
                    Input(type="checkbox", name=goal, id=goal),
                    Label(goal, fr=goal),
                )
                for goal in goals
            ],
            Button("next", type="submit"),
            action="/stage2",
            method="POST",
        )
    )


if __name__ == "__main__":
    uvicorn.run(
        "maine:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )
