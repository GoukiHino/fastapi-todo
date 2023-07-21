from fastapi import APIRouter

from app.api.v1.endpoints import login, user, todo

router = APIRouter()
router.include_router(login.router, tags=["login"])
router.include_router(user.router, prefix="/users", tags=["users"])
router.include_router(todo.router, prefix="/todos", tags=["todos"])
