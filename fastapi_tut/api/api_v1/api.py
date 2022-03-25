from fastapi import APIRouter

from fastapi_tut.api.api_v1.endpoints import quiz, login, teacher_quiz_crud

api_router = APIRouter()
api_router.include_router(login.router, prefix='/login', tags=['login'])
api_router.include_router(quiz.router, prefix='/teachers', tags=['Teachers']) #not sure sa prefix
