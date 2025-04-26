from fastapi import APIRouter
from apis.endpoint import  user, aiApiCall

api_router = APIRouter()

api_router.include_router(user.router, prefix="/user", tags=["user"])
api_router.include_router(aiApiCall.router, prefix="/ai", tags=["aiApiCall"])