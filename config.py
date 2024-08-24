import os

class Config:
    SERPAPI_KEY = os.getenv('SERPAPI', 'YOUR_API_KEY')
