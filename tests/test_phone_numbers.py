# test_phone_numbers.py
import re
from playwright.sync_api import Page
from locators.contact_page_locators import PHONE_LOCATORS


def test_phone_number_format(page: Page):
    page.goto("https://engeto.cz/kontakt/")

    all_numbers_passed = True
    for phone_locator in PHONE_LOCATORS:
        phone_elements = page.locator(phone_locator).all_inner_texts()

        for phone in phone_elements:
            if not re.match(r"^\+420\s\d{3}\s\d{3}\s\d{3}$", phone):
                print(f"❌ Invalid phone format: {phone}")
                all_numbers_passed = False

    # Print message confirming result
    if all_numbers_passed:
        print("\n---------> ✅ All phone numbers match the format '+420 xxx xxx xxx'")
    else:
        print("\n---------> ❌ Some phone numbers do not match the format.")
