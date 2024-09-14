# main.py
from run_tests import run_phone_number_tests, run_email_tests, run_iban_and_swift_tests

def main():
    print("""
          ##################################################
          # --> Initializing Test Suite for Engeto Website #
          ##################################################
          """)
    run_phone_number_tests()
    run_email_tests()
    run_iban_and_swift_tests()
    print("""
          #############################################
          # --> TESTING FINISHED! CHECK RESULTS ABOVE #
          #############################################
          """)

if __name__ == "__main__":
    main()