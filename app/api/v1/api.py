from fastapi import APIRouter

from app.api.v1.endpoint import auth, user, todo

router = APIRouter()
router.include_router(auth.router, prefix="", tags=["OAuth2"])
router.include_router(user.router, prefix="/users", tags=["User"])
router.include_router(todo.router, prefix="/todos", tags=["Todo"])
