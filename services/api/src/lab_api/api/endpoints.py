import os

from fastapi import APIRouter, Query, Request

from .schemas import HealthResponse

router = APIRouter()


@router.get(path="/health")
async def health() -> HealthResponse:
    return HealthResponse(status="ok")


@router.get(path="/crash")
async def crash() -> None:
    os._exit(1)


@router.get(path="/leak")
async def leak(request: Request, mb: int = Query(default=50, gt=0, le=500)) -> dict[str, int]:
    chunk = b"x" * ( mb * 1024 * 1024)
    request.state.global_list.append(chunk)
    total = sum(len(c) for c in request.state.global_list) // (1024 * 1024)
    return {"chunks": len(request.state.global_list), "total_mb": total}
