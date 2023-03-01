from fastapi import FastAPI, HTTPException
import sys

from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles

sys.path.append('app')
from Templates import Template

template: list[Template] = [
    Template(222, 'Template 1', "Template 1 description"),
    Template(333, 'Template 2', "Long Template 2 description"),
]

app = FastAPI()

app.mount("\app\pages", StaticFiles(directory="app/pages"), name="pages")


@app.get("/")
async def hello():
    return FileResponse('app/pages/index.html')


@app.get("/v2/templates")
async def get_docs():
    return template


@app.get("/v2/templates/{id}")
async def get_docs_by_id(id: int):
    result = [templ for templ in template if templ.id == id]
    return result[0] if len(result) > 0 else HTTPException(status_code=404, detail=f"Template {id} not found")
