# src/utils/db.py
import os
from sqlalchemy import create_engine
from github import Github
from dotenv import load_dotenv

load_dotenv()

def get_engine():
    return create_engine(os.getenv("DATABASE_URL"))

def get_github_client():
    return Github(os.getenv("GITHUB_TOKEN"))