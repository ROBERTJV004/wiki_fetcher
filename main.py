from typing import Optional
from fastapi import FastAPI, HTTPException
from wiki_fetcher import fetch_summary

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "Wiki Fetcher API",
        "endpoints": {
            "/summary": "Get Wikipedia summary for a keyword. Usage: /summary?keyword=bitcoin"
        }
    }

@app.get("/summary")
def get_summary(keyword: Optional[str] = None):
    if keyword is None or not keyword.strip():
        raise HTTPException(
            status_code=400,
            detail="You must provide a keyword. Example: /summary?keyword=bitcoin"
        )

    summary = fetch_summary(keyword)

    if summary == "No summary found.":
        raise HTTPException(
            status_code=404,
            detail=f"No summary available for '{keyword}'."
        )

    return {
        "keyword": keyword,
        "summary": summary
    }
