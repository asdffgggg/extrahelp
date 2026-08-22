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
            Input(name="dob", id="dob", type="date", cls="input"),
            P("Interests:"),
            *[
                Div(
                    Input(type="checkbox", name=interest, id=interest, cls="input"),
                    Label(interest, fr=interest),
                )
                for interest in interests
            ],
            Input(id="lat", name="lat", style="display:none", cls="input"),
            Input(id="lon", name="lon", style="display:none", cls="input"),
            Button("next", type="submit"),
            id="form",
            action="/stage2",
            method="POST",
        ),
        Script(src="/static/location.js"),
        Script(src="/static/submit.js"),
    )


goals = [
    "Better teamwork",
    "Improved Knowledge of subject",
    "Volunteering Hours",
    "Field Experience",
    "Networking",
    "I'm just a good person",
]


@app.post("/stage2")
async def stage2(request: Request):
    data = dict(await request.form())
    print(data)
    return page(
        Form(
            P("Goals:"),
            *[
                Div(
                    Input(type="checkbox", name=goal, id=goal, cls="input"),
                    Label(goal, fr=goal),
                )
                for goal in goals
            ],
            *[
                Input(value = value,id=key, name=key, style="display:none", cls="input")
                for key, value in data.items()
            ],
            Button("next", type="submit"),
            action="/prompt",
            method="POST",
            id="form",
        ),
        Script(src="/static/submit.js"),
    )


@app.post("/prompt")
async def prompt(request: Request):
    data = dict(await request.form())
    prompt = "user looking for places volunteer\n"
    prompt +=f"users date of birth is {data["dob"]}\n"
    prompt +=f"users location is {data["lat"]},{data["lon"]} \n"
    prompt +="user is interested in:"
    for interest in interests:
        if interest in data:
            prompt += f"{interest},"
    prompt +="users goals for this oppurtunity:"
    for goal in goals:
        if goal in data:
            prompt += f"{goal},"
    
    return page(prompt)


if __name__ == "__main__":
    uvicorn.run(
        "maine:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )

# id="form",
# Script(src="/static/submit.js"),
#  cls = "input"
