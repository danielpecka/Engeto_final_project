import re
from playwright.sync_api import Page
from locators.contact_page_locators import PHONE_LOCATORS, EMAIL_LOCATORS

def test_phone_number_format(page: Page):
    page.goto("https://engeto.cz/kontakt/")
    
    for phone_locator in PHONE_LOCATORS:
        phone_elements = page.locator(phone_locator).all_inner_texts()
        
        for phone in phone_elements:
            assert re.match(r"^\+420\s\d{3}\s\d{3}\s\d{3}$", phone), f"Invalid phone format: {phone}"

def test_email_format(page: Page):
    page.goto("https://engeto.cz/kontakt/")
    
    for email_locator in EMAIL_LOCATORS:
        email_elements = page.locator(email_locator).all_inner_texts()
        
        # Subtest A: Validate Email Format
        for email in email_elements:
            assert re.match(r"^[\w\.-]+@[\w\.-]+\.\w{2,}$", email), f"Invalid email format: {email}"
        
        # Subtest B: Verify Specific Email
        assert "sales@engeto.cz" in email_elements, "sales@engeto.cz not found on the page."
