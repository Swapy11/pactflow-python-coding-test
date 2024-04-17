"""
Base routes for the API.

The routes in this module serve a very basic purpose, such as health checks and
version information.
"""

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from pypacter_api import get_version
from src.pypacter import detect_language

router = APIRouter()


@router.get("/health", tags=["health"])
async def health() -> JSONResponse:
    """
    Health check.

    Returns:
        A JSON response indicating the health of the API.
    """
    return JSONResponse(content={"status": "ok"})


@router.get("/version", tags=["version"])
async def version() -> JSONResponse:
    """
    Get the version of the API.

    Returns:
        A JSON response containing the version of the API.
    """
    return JSONResponse(content={"version": get_version()})


@router.post("/detect-language")
async def detect_language(request_body: Dict[str, str]) -> Dict[str, str]:
    """
    Endpoint to detect the programming language.

    Args:
        request_body (dict): JSON payload containing the "code_snippet".

    Returns:
        dict: A JSON response with the detected language.
    """
    try:
        code_snippet = request_body.get("code_snippet", "")
        detected_language = detect_language(code_snippet)

        return JSONResponse(content={"language": detected_language})

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error occurred: {str(e)}")
