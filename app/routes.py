from fastapi import APIRouter, HTTPException
from .parsers import parse_company_data
from .models import Company
from .database import get_company, save_company

router = APIRouter()

@router.post("/parse")
def parse_company(company_url: str) -> dict:
    try:
        data = parse_company_data(company_url)
        save_company(data)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/company/{company_name}")
def get_company_data(company_name: str) -> Company:
    company = get_company(company_name)
    if company:
        return company
    else:
        raise HTTPException(status_code=404, detail="Company not found")
