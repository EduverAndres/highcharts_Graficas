from fastapi import FastAPI, Request, status
from fastapi.responses import FileResponse, JSONResponse
from fastapi.encoders import jsonable_encoder
from projects.ind_mantenimiento.routers import grafica_routes
import uvicorn
from fastapi_pagination import add_pagination
from fastapi.exceptions import RequestValidationError
from datetime import datetime
from pydantic_translations import Translator
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
#uvicorn app.main:app --reload
tr = Translator('es')

tags_metadata = [
    {
        "name": "Auth",
        "description": "Aquí coloco toda la documentación que yo quiera agregar.",
    },
    {
        "name": "Users",
        "description": "Aquí coloco toda la documentación que yo quiera agregar.",
    },
]

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)
app.mount("/index", StaticFiles(directory="projects/ind_mantenimiento/view", html=True), name="static")

@app.get("/grafica2")
async def wi():
    return FileResponse("projects/ind_mantenimiento/view/grafica2.html")

@app.get("/grafica3")
async def wi2():
    return FileResponse("projects/ind_mantenimiento/view/grafica3.html")

@app.get("/")
async def main():
    return RedirectResponse(url="/index")



@app.exception_handler(RequestValidationError)
def validation_expection_handler(request: Request, exc: RequestValidationError):
    ex = tr.translate_exception(exc)
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=jsonable_encoder({"status": 400, "success": False, "message": [str(result[1] if len(result := i["loc"]) > 0 and result else ["Error","Error"]) + " " + str(i["msg"]) for i in ex.errors()], "time": datetime.now(), "path": request.url.path}))

# app.include_router(auth.router, tags=['Auth'], prefix=f'/{settings.PATH_API}/auth')
# app.include_router(user.router, tags=['Users'], prefix=f'/{settings.PATH_API}/users')

app.include_router(grafica_routes.router, tags=["tablas"])


add_pagination(app)

@app.get('/api/healthchecker')
def root():
    return {'message': 'Hello World'}



if __name__ == "__main__":
    uvicorn.run("projects.ind_mantenimiento.main:app",port=8004,reload=True)