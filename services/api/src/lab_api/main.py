from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from typing import TypedDict

import uvicorn
from fastapi import FastAPI

from lab_api.api import router as api_router
from lab_api.core import settings


class State(TypedDict):
    global_list: list[bytes]


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[State, None]:
    global_list: list[bytes] = []
    yield {"global_list": global_list}
    global_list.clear()


app = FastAPI(lifespan=lifespan)
app.include_router(api_router)


def main() -> None:
    uvicorn.run(
        "lab_api.main:app",
        host=settings.run.host,
        port=settings.run.port,
    )


if __name__ == "__main__":
    main()
