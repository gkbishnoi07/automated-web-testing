from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from playwright_tests.test_site import test_site

app = FastAPI()

# Add CORS middleware
origins = [
    "https://automated-web-testing.netlify.app",
    # Add other allowed origins if any, or use "*" to allow all (not recommended for production)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # or ["*"] to allow all origins
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
