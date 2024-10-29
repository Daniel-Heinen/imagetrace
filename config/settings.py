"""Application settings"""
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://localhost/db")
SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")
DEBUG = os.getenv("DEBUG", "True") == "True"
# Modified 2024-03-25
# Modified 2024-10-29
