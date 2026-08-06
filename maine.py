from fastapi import FastAPI 
from fasthtml.common import *
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return to_xml(Html(
        Head(Title("ExtraHelp")),
        Body(
            P("but not you")
        )
    ))


if __name__ == "__main__":
    uvicorn.run(
        "maine:app",
        host = "127.0.0.1",
        port = 8000,
        reload = True,
    )
