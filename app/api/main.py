from fastapi import FastAPI, Response, Request

from api.routers.products import router as product_router

from api.handlers import exception_handler


app = FastAPI()


app.include_router(product_router)

exception_handler(app=app)

@app.get("/")
def get_root(request: Request):
    return Response(status_code=200, content="I AM OK")