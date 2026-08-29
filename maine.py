import json

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
            A("ExtraHelp", cls="logo", href="/"),
            Div(
                *args,
                id="content",
            ),
        ),
    )
    return HTMLResponse(to_xml(conteant))


@app.get("/")
async def root():
    return page(
        H3("Helping teens volunteer!"),
        A(
            "Get Started ➙",
            cls="started",
            href="/stage1",
        ),
        H2("About ExtraHelp:"),
        P("""
ExtraHelp was made to help teens with extracurriculars, specifically volunteering opportunities. The main function of ExtraHelp will be finding volunteering opportuities near you that you will benefit from."""),
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
            Br(),
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
                Input(value=value, id=key, name=key, style="display:none", cls="input")
                for key, value in data.items()
            ],
            Br(),
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
    prompt += f"users date of birth is {data['dob']}\n"
    prompt += f"users location is {data['lat']},{data['lon']} \n"
    prompt += "user is interested in:"
    for interest in interests:
        if interest in data:
            prompt += f"{interest},"
    prompt += "\nusers goals for this oppurtunity:"
    for goal in goals:
        if goal in data:
            prompt += f"{goal},"
    prompt += "\n give response in json format. on success, give an object with a single key 'success'. the value of the success key should be an array of objects, each with keys (name, address, phone number, website, description).the description should be a sentance or two on why the opportunity fits for the user. on faliure, give a single key: error, with a value of why it went wrong. make sure the error message is user friendlyt and can be understood by the user with no coding experience, also feel free to error if there are no available oppurtunities because of the users age, or location. address the user in a second person manner and refer to yourself as 'we'."

    error = """"{"error":"We couldn't find a verified volunteer opportunity that is appropriate for you at age 6 and specifically matches technology or business. The City of Sacramento's youth volunteer programs generally start at age 12, while technology-focused opportunities such as Computers 4 Kids do not publish a minimum age that would confirm eligibility for a 6-year-old. We recommend looking for family-friendly community service activities where you can participate with a parent or guardian. "}"""

    success = """{"success":[{"name":"Sacramento Food Bank & Family Services","address":"1951 Bell Avenue, Sacramento, CA 95838","phone number":"(916) 456-1980","website":"https://www.sacramentofoodbank.org/volunteer","description":"This is a strong fit for an 11-year-old interested in helping people through food assistance. Volunteers ages 10–15 can participate when accompanied by an adult, and the organization provides structured volunteer shifts that can help build documented service hours."},{"name":"River City Food Bank","address":"1800 28th Street, Sacramento, CA 95816","phone number":"(916) 446-2627","website":"https://rivercityfoodbank.org/volunteer-your-time/","description":"River City Food Bank directly supports people experiencing food insecurity, making it a good aid-focused opportunity. Volunteers ages 10–14 may participate with adult supervision, so an 11-year-old can volunteer with a parent or other supervising adult."}]}"""

    jason = json.loads(success)

    if 'success' in jason:
        return page(
            *[
                Div(
                    H1(item['name']),
                    P(item['phone number']),
                    P(item['address']),
                    A(item['website'], href = item['website'], cls = 'glow'),
                    P(item['description']),
                    
                )
                for item in jason["success"]
            ]
        )

    print(prompt)
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
