import os

from fastapi import FastAPI

from fastapi.responses import FileResponse

from pathlib import Path

from elekeeper import SajClient

app = FastAPI(title="HEMS")

BASE = Path(__file__).parent

@app.get("/")

def index():

    return FileResponse(BASE / "index.html")

@app.get("/api/solar")

async def solar():

    user = os.environ.get("SAJ_USER")

    password = os.environ.get("SAJ_PASS")

    if not user or not password:

        return {

            "error": "SAJ_USER of SAJ_PASS ontbreekt"

        }

    try:

        async with SajClient() as client:

            await client.authenticate(user, password)

            overview = await client.get_plant_overview()

            return {

                "plant": overview.name,

                "pv_kw": round(overview.pv_power_w / 1000, 2),

            }

    except Exception as e:

        return {

            "error": str(e)

        }
