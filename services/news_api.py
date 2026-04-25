import os
import requests
from typing import List, Dict, Optional
from datetime import datetime, timedelta
import logging

logger = logging.getLogger(__name__)

class NewsAPIService:
    def __init__(self):
        self.api_key = os.getenv("NEWS_API_KEY", "510da26ba488436b84b25e7178859f88")
        self.base_url = "https://newsapi.org/v2"

    def fetch_orthopedic_news(self, limit: int = 10) -> List[Dict]:
        """
        Fetch orthopedic and medical news from NewsAPI
        """
        try:
            # Calculate date 30 days ago for recent news
            from_date = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')

            # Search for orthopedic-related news with more specific terms
            query = '"orthopedic" OR "orthopaedics" OR "joint replacement" OR "knee surgery" OR "hip replacement" OR "sports medicine" OR "arthritis treatment" OR "spine surgery" OR "fracture care" OR "bone surgery"'

            params = {
                'q': query,
                'from': from_date,
                'sortBy': 'publishedAt',
                'language': 'en',
                'pageSize': limit * 2,  # Fetch more to allow for filtering
                'apiKey': self.api_key
            }

            response = requests.get(f"{self.base_url}/everything", params=params)
            response.raise_for_status()

            data = response.json()

            # Transform NewsAPI format to our article format
            articles = []
            for article in data.get('articles', []):
                # Skip articles without images or content
                if not article.get('urlToImage') or not article.get('content'):
                    continue

                # Filter for truly orthopedic-related content
                if not self._is_orthopedic_article(article):
                    continue

                transformed_article = {
                    'title': article.get('title', ''),
                    'description': article.get('description', '') or article.get('title', ''),
                    'content': article.get('content', ''),
                    'category': self._categorize_article(article.get('title', '') + ' ' + article.get('description', '')),
                    'author': article.get('author', 'Medical News') or 'Medical News',
                    'image': article.get('urlToImage', ''),  # Changed to 'image' to match static format
                    'date': self._format_date(article.get('publishedAt')),  # Changed to 'date'
                    'views': 0,  # NewsAPI doesn't provide views, set to 0
                    'likes': 0,  # NewsAPI doesn't provide likes, set to 0
                    'source_url': article.get('url', ''),
                    'source_name': article.get('source', {}).get('name', 'Medical News')
                }
                articles.append(transformed_article)

            logger.info(f"Successfully fetched {len(articles)} orthopedic news articles")
            return articles[:limit]  # Ensure we don't exceed the limit

        except Exception as e:
            logger.error(f"Error fetching orthopedic news: {str(e)}")
            return []

    def _is_orthopedic_article(self, article: dict) -> bool:
        """
        Check if an article is truly orthopedic-related
        """
        text = (article.get('title', '') + ' ' + article.get('description', '') + ' ' + article.get('content', '')).lower()

        # Must contain at least one orthopedic keyword
        orthopedic_keywords = [
            'orthopedic', 'orthopaedics', 'orthopedist', 'orthopedic surgery',
            'joint replacement', 'knee replacement', 'hip replacement', 'shoulder replacement',
            'arthroplasty', 'sports medicine', 'sports injury', 'acl', 'meniscus',
            'arthritis', 'osteoarthritis', 'rheumatoid arthritis', 'joint pain',
            'spine surgery', 'back surgery', 'herniated disc', 'scoliosis',
            'fracture', 'broken bone', 'bone surgery', 'trauma surgery',
            'pediatric orthopedic', 'bone marrow', 'cartilage', 'ligament',
            'tendon', 'musculoskeletal', 'orthosis', 'prosthesis'
        ]

        # Must NOT contain irrelevant keywords
        irrelevant_keywords = [
            'storage wars', 'reality tv', 'celebrity', 'entertainment',
            'politics', 'election', 'government', 'crime', 'accident',
            'weather', 'sports team', 'football', 'basketball', 'baseball'
        ]

        has_orthopedic = any(keyword in text for keyword in orthopedic_keywords)
        has_irrelevant = any(keyword in text for keyword in irrelevant_keywords)

        return has_orthopedic and not has_irrelevant

    def _categorize_article(self, text: str) -> str:
        """
        Categorize article based on content keywords
        """
        text_lower = text.lower()

        if any(word in text_lower for word in ['knee', 'hip', 'joint replacement', 'arthroplasty']):
            return 'Joint Health'
        elif any(word in text_lower for word in ['sports', 'athlete', 'injury prevention', 'acl', 'meniscus']):
            return 'Sports Medicine'
        elif any(word in text_lower for word in ['arthritis', 'rheumatoid', 'osteoarthritis']):
            return 'Arthritis'
        elif any(word in text_lower for word in ['spine', 'back', 'scoliosis', 'herniated disc']):
            return 'Spine Health'
        elif any(word in text_lower for word in ['fracture', 'broken bone', 'trauma']):
            return 'Trauma Care'
        elif any(word in text_lower for word in ['pediatric', 'children', 'adolescent']):
            return 'Pediatric Orthopedics'
        else:
            return 'Orthopedic News'

    def _format_date(self, published_at: str) -> str:
        """
        Format the publishedAt date to match the static article format
        """
        try:
            if published_at:
                dt = datetime.fromisoformat(published_at.replace('Z', '+00:00'))
                return dt.strftime('%B %d, %Y')
            else:
                return datetime.now().strftime('%B %d, %Y')
        except:
            return datetime.now().strftime('%B %d, %Y')

# Global instance
news_service = NewsAPIService()