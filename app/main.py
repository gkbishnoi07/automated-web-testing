from fastapi import FastAPI, Query
from playwright_tests.test_site import test_site

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to TestTrack"}

@app.get("/test-url")
def test_url(target: str = Query(..., description="Website URL to test")):
    result = test_site(target)
    return result
