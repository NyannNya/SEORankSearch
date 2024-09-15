import os

class Config:
    GOOGLE_CX = os.getenv('GOOGLE_CX', '42edffe26ec224231')
    GOOGLE_APPLICATION_CREDENTIALS = os.getenv('GOOGLE_APPLICATION_CREDENTIALS', 'etc/secrets/google_api.json')    