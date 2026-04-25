from fastapi import APIRouter, HTTPException
from typing import List, Dict
from services.news_api import news_service

router = APIRouter(prefix="/news", tags=["News"])

@router.get("/", response_model=List[Dict])
def get_orthopedic_news(limit: int = 9):
    """
    Fetch orthopedic news from NewsAPI
    """
    try:
        articles = news_service.fetch_orthopedic_news(limit=limit)
        if not articles:
            # Return empty list instead of error to allow fallback to static content
            return []
        return articles
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch news: {str(e)}")

@router.get("/health")
def check_news_api_health():
    """
    Check if NewsAPI is accessible
    """
    try:
        # Try to fetch just 1 article to test connectivity
        test_articles = news_service.fetch_orthopedic_news(limit=1)
        return {"status": "healthy", "articles_available": len(test_articles) > 0}
    except Exception as e:
        return {"status": "unhealthy", "error": str(e)}