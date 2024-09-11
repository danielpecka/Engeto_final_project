from playwright.sync_api import Page
from locators.contact_page_locators import IBAN_LOCATOR, SWIFT_LOCATOR
from locators.iban_page_locators import IBAN_INPUT_LOCATOR, TEST_BUTTON_LOCATOR, BANK_CODE_LOCATOR, GENERATED_SWIFT_LOCATOR

def test_iban_and_swift_code(page: Page):
    # Step 1: Extract IBAN and SWIFT from Engeto page
    page.goto("https://engeto.cz/kontakt/")
    
    iban = None
    original_swift = None

    # Parse IBAN from full text (e.g., "IBAN: CZ8455000000000000439275")
    for iban_locator in IBAN_LOCATOR:
        iban_element = page.locator(iban_locator).first
        if iban_element.is_visible():
            iban_text = iban_element.inner_text()
            iban = iban_text.split(": ")[1]  # Split at ': ' and take the second part
            break

    # Parse SWIFT from full text (e.g., "SWIFT: RZBCCZPP")
    for swift_locator in SWIFT_LOCATOR:
        swift_element = page.locator(swift_locator).first
        if swift_element.is_visible():
            swift_text = swift_element.inner_text()
            original_swift = swift_text.split(": ")[1]  # Split at ': ' and take the second part
            break

    assert iban, "IBAN not found on the page"
    assert original_swift, "SWIFT code not found on the page"

    # Step 2: Open IBAN Validation tool and validate IBAN
    page.goto("https://www.cnb.cz/cs/platebni-styk/iban/kalkulator-iban-ceska-republika/")
    
    for iban_input_locator in IBAN_INPUT_LOCATOR:
        iban_input_element = page.locator(iban_input_locator).first
        if iban_input_element.is_visible():
            iban_input_element.fill(iban)
            break

    for test_button_locator in TEST_BUTTON_LOCATOR:
        test_button = page.locator(test_button_locator).first
        if test_button.is_visible():
            test_button.click()
            break

    # Step 3: Extract bank code and generated SWIFT from the result
    bank_code = None
    generated_swift = None

    for bank_code_locator in BANK_CODE_LOCATOR:
        bank_code_element = page.locator(bank_code_locator).first
        if bank_code_element.is_visible():
            bank_code = bank_code_element.inner_text()
            break

    for generated_swift_locator in GENERATED_SWIFT_LOCATOR:
        generated_swift_element = page.locator(generated_swift_locator).first
        if generated_swift_element.is_visible():
            generated_swift = generated_swift_element.inner_text()
            break

    assert bank_code, "Bank code not found in IBAN validation result"
    assert generated_swift, "SWIFT code not found in IBAN validation result"

    # Subtest 1: Compare the original SWIFT code with the generated one
    assert original_swift == generated_swift, "SWIFT code mismatch!"

    # Subtest 2: Verify bank code and swift code from `bank_codes.txt`
    with open("tests/bank_codes.txt", "r") as f:
        bank_data = f.readlines()

    found_match = False
    for line in bank_data:
        bank_code_file, bank_name, swift_code_file = line.strip().split(";")
        if bank_code == bank_code_file and generated_swift == swift_code_file:
            found_match = True
            print(f"Bank of Engeto: {bank_name}")
            break

    assert found_match, "Bank code and SWIFT code do not match the list."
