from fastapi import FastAPI

# Create FastAPI instance
app = FastAPI(
    title="Meeting Memory Hub",
    description="AI-Powered Meeting Memory Hub API",
    version="0.1.0"
)

# Root route (health check)
@app.get("/")
def read_root():
    return {"message": "🚀 Meeting Memory Hub backend is running!"}
