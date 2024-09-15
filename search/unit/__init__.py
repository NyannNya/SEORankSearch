from google.oauth2 import service_account
from config import Config

credentials = service_account.Credentials.from_service_account_file(
    Config.GOOGLE_APPLICATION_CREDENTIALS,
    scopes = ['https://www.googleapis.com/auth/cse']
    )
google_search_engine_id = Config.GOOGLE_CX