import pytest

def run_tests():
    # Run phone number and email validation tests
    print("\n====================================================")
    print("🌟🌟 Running Contact Page Tests 🧑‍💻... 🌟🌟")
    print("====================================================")
    contact_tests_result = pytest.main(["tests/test_contact_page.py", "-v", "--tb=short"])  # Verbose mode with short traceback
    if contact_tests_result == 0:
        print("\n🎉🎉 ALL CONTACT PAGE TESTS PASSED! 🎉🎉")
    else:
        print("\n❌❌ SOME CONTACT PAGE TESTS FAILED! ❌❌")

    # Run IBAN and SWIFT code validation tests
    print("\n====================================================")
    print("🌟🌟 Running IBAN Validation Tests 💳... 🌟🌟")
    print("====================================================")
    iban_tests_result = pytest.main(["tests/test_iban_validation.py", "-v", "--tb=short"])  # Verbose mode with short traceback
    if iban_tests_result == 0:
        print("\n🎉🎉 ALL IBAN VALIDATION TESTS PASSED! 🎉🎉")
    else:
        print("\n❌❌ SOME IBAN VALIDATION TESTS FAILED! ❌❌")

if __name__ == "__main__":
    print("\n****************************************************")
    print("🚀🚀 Initializing Test Suite for Engeto Website 🔍🕵️‍♂️ ... 🚀🚀")
    print("****************************************************")
    run_tests()
    print("\n****************************************************")
    print("📊📊 TESTING COMPLETED! CHECK RESULTS ABOVE 📊📊")
    print("****************************************************")
