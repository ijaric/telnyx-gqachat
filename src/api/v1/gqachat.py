from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException, Query

from models.gqachat import Reply
from services.gqachat import GQAService, get_qga_service

router = APIRouter()


@router.get("/", response_model=Reply, summary="Get an answer on a question")
async def get_answer(
    gqa_service: GQAService = Depends(get_qga_service),
    question: str = Query(),
) -> Reply:
    """
    Get an answer on a question using ChatGPT and Telnyx's documentation

    - **question**: Question
    """

    answer = await gqa_service.get_answer(
        question=question,
    )

    if not answer:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="nothing was found"
        )

    return Reply(**answer)
