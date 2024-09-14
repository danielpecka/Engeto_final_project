# run_tests.py
import pytest

def run_phone_number_tests():
    # Run phone number validation tests
    print("""
          =======================================================================
          Testování kontaktních údajů na stránce https://engeto.cz/kontakt/ [1/2]
          =======================================================================
          - Test proběhne za použití ovladače pro chromium a firefox

          Test 1: Ověř jestli formát telefonních čísel podpory odpovídá správnému formátu "+420 ččč ččč ččč"
          """)

    phone_number_tests_result = pytest.main(["tests/test_phone_numbers.py", "-v", "--tb=short", "-s"])  # Verbose mode with short traceback

    if phone_number_tests_result == 0:
        print("""
              --> Všechny testy telefonních čísel uspěli!
              ###########################################
             """)
    else:
        print("""
              --> Některé testy telefonních čísel selhali!
              ############################################
              """)

def run_email_tests():
    # Run email validation tests
    print("""
          =======================================================================
          Testování kontaktních údajů na stránce https://engeto.cz/kontakt/ [2/2]
          =======================================================================
          - Test proběhne za použití ovladače pro chromium a firefox

          Test 2: Ověř jestli je formát emailových adres správný a jestli je jedna z emailových adres "sales@engeto.com".
          """)

    email_tests_result = pytest.main(["tests/test_emails.py", "-v", "--tb=short", "-s"])  # Verbose mode with short traceback

    if email_tests_result == 0:
        print("""
              --> Všechny testy emailových adres uspěli!")
              ############################################
              """)
    else:
        print("""
              --> Některé testy emailových adres selhali!")
              #############################################
              """)

def run_iban_and_swift_tests():
    # Run IBAN and SWIFT code validation tests
    print("""
          ==========================================================================
          Testování reálnosti bankovních údajů na stránce https://engeto.cz/kontakt/
          ==========================================================================
          - Test proběhne za použití ovladače pro chromium a firefox

          - V rámci testu jsou nejdřív scrapovány fakturační údaje ze stránky https://engeto.cz/kontakt/ a je z nich vyparsován IBAN a SWIFT
          - IBAN je poté vložen do webu ČNB (https://www.cnb.cz/cs/platebni-styk/iban/kalkulator-iban-ceska-republika/) pro kalkulaci dalších údajů o bance: SWIFT(BIC) a kód banky
          - Vygenerovaný SWIFT(BIC) je srovnán se SWIFT(BIC) kódem na webu
          - Poté je SWIFT(BIC) spolu s kódem banky srovnán se seznamem kódů bank a jejich SWIFT(BIC) kódů pro ověření reálnosti údajů na webu ENGETO

          Test 3: Ověř jestli bankovní údaje na stránce https://engeto.cz/kontakt/ odpovídají reálné bance.
          """)

    iban_tests_result = pytest.main(["tests/test_iban_validation.py", "-v", "--tb=short", "-s"])  # Verbose mode with short traceback

    if iban_tests_result == 0:
        print("""
              --> Všechny testy bankovních údajů uspěli!")
              ############################################
              """)
    else:
        print("""
              --> Některé testy bankovních údajů selhali!")
              #############################################
              """)