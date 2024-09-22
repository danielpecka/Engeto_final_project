# utils/scrape_iban_and_swift.py
import requests
from bs4 import BeautifulSoup
import re


# Function to scrape IBAN and SWIFT codes from a given URL
def scrape_iban_and_swift(url="https://engeto.cz/kontakt/"):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if request was successful
    if response.status_code != 200:
        raise Exception(f"Failed to retrieve page: {response.status_code}")

    # Parse the page content
    soup = BeautifulSoup(response.text, "html.parser")

    # Regular expression patterns for IBAN and SWIFT (BIC) codes
    iban_pattern = r"[A-Z]{2}\d{2}\d{20}"
    swift_pattern = r"[A-Z]{6}[A-Z0-9]{2,5}"

    # Store the results in a list of objects
    extracted_codes = []

    # Find all span elements with the class 'block-column-line'
    spans = soup.find_all("span", class_="block-column-line")

    # Loop through each span and extract the text
    for span in spans:
        # Get the entire text of the span
        full_text = span.get_text(separator=" ", strip=True)

        # Check for IBAN using regex
        iban_match = re.search(iban_pattern, full_text)
        if iban_match:
            iban = iban_match.group()
            extracted_codes.append({"type": "IBAN", "value": iban})

        # Check for SWIFT (BIC) code using regex
        swift_match = re.search(swift_pattern, full_text)
        if swift_match:
            swift = swift_match.group()
            extracted_codes.append({"type": "SWIFT", "value": swift})

    # Ensure that at least one IBAN and SWIFT code were found
    if not extracted_codes:
        raise Exception("No IBAN or SWIFT codes found on the page")

    return extracted_codes


# Function to extract IBAN from the scraped data
def extract_iban(codes):
    for code in codes:
        if code["type"] == "IBAN":
            return code["value"]
    raise Exception("IBAN not found in scraped data")


# Function to extract SWIFT from the scraped data
def extract_swift(codes):
    for code in codes:
        if code["type"] == "SWIFT":
            return code["value"]
    raise Exception("SWIFT code not found in scraped data")
