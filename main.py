import os
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pydantic_ai import Agent, ModelSettings
from pydantic_ai.models.google import GoogleModel
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

# Setup for serving the HTML file
templates = Jinja2Templates(directory="templates")

# --- DATA MODELS ---
class TripActivity(BaseModel):
    activity: str
    time_of_day: str
    estimated_cost: str

class DailyPlan(BaseModel):
    day: int
    activities: list[TripActivity]

class TripPlan(BaseModel):
    destination: str
    total_estimated_budget: str
    itinerary: list[DailyPlan]
    travel_tips: str

# --- AGENT ---
model = GoogleModel('gemini-2.5-flash') 
trip_agent = Agent(model=model, output_type=TripPlan)

# --- ROUTES ---

# 1. This serves your index.html at the main URL
@app.get("/", response_class=HTMLResponse)
async def serve_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# 2. Your API endpoint
@app.get("/plan")
async def plan_trip(source: str, destination: str, days: int):
    try:
        prompt = f"Plan a {days} day trip from {source} to {destination}."
        result = await trip_agent.run(prompt)
        return result.output
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    # Use PORT env variable for Render
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)