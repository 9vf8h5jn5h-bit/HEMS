from fastapi import FastAPI
from fastapi.responses import FileResponse
from pathlib import Path

app = FastAPI(title="HEMS")
BASE = Path(__file__).parent

@app.get("/")
def index():
    return FileResponse(BASE / "index.html")

@app.get("/api/solar")
def solar():
    return {
        "pv_kw": 3.94,
        "today_kwh": 14.29,
        "today_revenue": 2.86,
        "month_revenue": 58.87,
        "total_revenue": 1854.03
    }
