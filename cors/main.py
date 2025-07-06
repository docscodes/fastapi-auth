from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware


app = FastAPI(title="fastapi-auth-cors")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    max_age=-1,  # disable caching
)


@app.get("/")
async def get():
    return {"detail": "GET response"}


@app.post("/")
async def post(request: Request):
    json = await request.json()
    return {"detail": "POST response", "input_payload": json}
