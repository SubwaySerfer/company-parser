from pymongo import MongoClient
from .models import Company

client = MongoClient("mongodb://localhost:27017/")
db = client["company_parser"]
companies_collection = db["companies"]

def save_company(company_data: dict) -> None:
    companies_collection.update_one(
        {"name": company_data["name"]},
        {"$set": company_data},
        upsert=True
    )

def get_company(company_name: str) -> dict:
    return companies_collection.find_one({"name": company_name})
