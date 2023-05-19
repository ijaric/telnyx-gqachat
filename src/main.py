import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from api.v1 import gqachat

app = FastAPI(
    title="Telnyx GQA Chat bot read-only API",
    description="Answer questions using ChatGPT and documentation",
    docs_url="/api/openapi",
    openapi_url="/api/openapi.json",
    default_response_class=ORJSONResponse,
)


app.include_router(gqachat.router, prefix="/api/v1/gqachat", tags=["gqachat"])

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
    )
