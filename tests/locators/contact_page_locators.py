# locators/contact_page_locators.py
# Locators for the contact page as lists
PHONE_LOCATORS = [
    "//html[1]/body[1]/main[1]/div[3]/div[1]/div[1]/div[1]/a[1]",  # Trying XPath as selector for phone number 1
    "//html[1]/body[1]/main[1]/div[3]/div[2]/div[1]/div[1]/a[1]",  # And for phone number 2
]

EMAIL_LOCATORS = ['a[href^="mailto:"]']  # CSS selector for all emails on the page
