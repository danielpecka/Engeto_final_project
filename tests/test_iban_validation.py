# test_iban_validation.py
from playwright.sync_api import Page
from locators.iban_page_locators import (
    IBAN_INPUT_LOCATOR,
    TEST_BUTTON_LOCATOR,
    BANK_CODE_LOCATOR,
    GENERATED_SWIFT_LOCATOR,
)
from utils.scrape_iban_and_swift import (
    scrape_iban_and_swift,
    extract_iban,
    extract_swift,
)

# from utils.wait import wait_after_step <- uncomment the import if you wish to insert waits into the code, do that by adding a line "wait_after_step()"


def test_iban_and_swift_code(page: Page):
    # Step 1: Scrape IBAN and SWIFT from Engeto page
    scraped_codes = scrape_iban_and_swift()  # Scrape IBAN and SWIFT

    iban = extract_iban(scraped_codes)  # Extract IBAN
    original_swift = extract_swift(scraped_codes)  # Extract SWIFT

    # Step 2: Open IBAN Validation tool and validate IBAN
    page.goto(
        "https://www.cnb.cz/cs/platebni-styk/iban/kalkulator-iban-ceska-republika/"
    )

    # Fill IBAN
    for iban_input_locator in IBAN_INPUT_LOCATOR:
        iban_input_element = page.locator(iban_input_locator).first
        if iban_input_element.is_visible():
            iban_input_element.fill(iban)
            break

    # Click "Test" button
    for test_button_locator in TEST_BUTTON_LOCATOR:
        test_button = page.locator(test_button_locator).first
        if test_button.is_visible():
            test_button.click()
            break

    # Step 3: Extract bank code and generated SWIFT from the result
    bank_code = None
    generated_swift = None

    # Use input_value() to get the text that behaves like user input (instead of inner_text())
    for bank_code_locator in BANK_CODE_LOCATOR:
        bank_code_element = page.locator(bank_code_locator).first
        if bank_code_element.is_visible():
            bank_code = (
                bank_code_element.input_value()
            )  # Extract the value from the input field
            break

    for generated_swift_locator in GENERATED_SWIFT_LOCATOR:
        generated_swift_element = page.locator(generated_swift_locator).first
        if generated_swift_element.is_visible():
            generated_swift = (
                generated_swift_element.input_value()
            )  # Extract the value from the input field
            break

    # Step 4: Assertions
    assert iban, "IBAN not found on the page"
    assert original_swift, "SWIFT code not found on the page"
    assert bank_code, "Bank code not found in IBAN validation result"
    assert generated_swift, "SWIFT code not found in IBAN validation result"

    # Subtest 1: Compare the original SWIFT code with the generated one
    assert original_swift == generated_swift, "SWIFT code mismatch!"

    # Subtest 2: Verify bank code and swift code from `bank_codes.txt`
    with open("tests/bank_codes.txt", "r", encoding="utf-8") as f:
        bank_data = f.readlines()

    found_match = False
    for line in bank_data:
        bank_code_file, bank_name, swift_code_file = line.strip().split(";")
        if bank_code == bank_code_file and generated_swift == swift_code_file:
            found_match = True
            print(f"\n---------> Bank of Engeto: {bank_name}")
            break

    assert found_match, "Bank code and SWIFT code do not match the list."
