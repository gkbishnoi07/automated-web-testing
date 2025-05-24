from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from playwright_tests import test_site

app = FastAPI()

# CORS settings for Netlify frontend
origins = [
    "https://automated-web-testing.netlify.app",
    # Add additional origins as needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Welcome to TestTrack"}

@app.get("/test-url")
def test_url(target: str = Query(..., description="Website URL to test")):
    result = test_site(target)
    return result
