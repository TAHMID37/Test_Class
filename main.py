import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv("API_KEY")
databaseurl=os.getenv("database_url")

print(API_KEY)
print(databaseurl)
