# test__emails.py
import re
from playwright.sync_api import Page
from locators.contact_page_locators import EMAIL_LOCATORS


def test_email_format(page: Page):
    page.goto("https://engeto.cz/kontakt/")

    all_emails_valid = True
    found_sales_email = False

    for email_locator in EMAIL_LOCATORS:
        email_elements = page.locator(email_locator).all_inner_texts()

        # Subtest A: Validate Email Format
        for email in email_elements:
            if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w{2,}$", email):
                print(f"❌ Invalid email format: {email}")
                all_emails_valid = False
            if email == "sales@engeto.com":
                found_sales_email = True

    # Print result messages
    if all_emails_valid:
        print("\n---------> ✅ All emails match the correct format.")
    else:
        print("\n---------> ❌ Some emails do not match the correct format.")

    if found_sales_email:
        print("---------> ✅ The email 'sales@engeto.com' was found.")
    else:
        print("---------> ❌ The email 'sales@engeto.com' was NOT found.")
