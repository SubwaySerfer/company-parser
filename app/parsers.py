from playwright.sync_api import sync_playwright

def parse_company_data(company_url: str) -> dict:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(company_url)
        
        company_name = page.query_selector('h1').inner_text()
        company_size = page.query_selector('.company-size').inner_text()
        industry = page.query_selector('.industry').inner_text()
        
        employees = []
        employee_elements = page.query_selector_all('.employee')
        for element in employee_elements:
            employees.append({
                'name': element.query_selector('.name').inner_text(),
                'position': element.query_selector('.position').inner_text()
            })
        
        browser.close()
        
        return {
            'name': company_name,
            'size': company_size,
            'industry': industry,
            'employees': employees
        }
