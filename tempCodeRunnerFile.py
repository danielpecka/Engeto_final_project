import requests
from bs4 import BeautifulSoup
import re

# URL of the page to scrape
url = 'https://engeto.cz/kontakt/'  # Replace with the actual URL

# Send a GET request to the URL
response = requests.get(url)

# Parse the page content
soup = BeautifulSoup(response.text, 'html.parser')

# Regular expression patterns for IBAN and SWIFT (BIC) codes
iban_pattern = r"^([A-Z]{2}[ \-]?[0-9]{2})(?=(?:[ \-]?[A-Z0-9]){9,30}$)((?:[ \-]?[A-Z0-9]{3,5}){2,7})([ \-]?[A-Z0-9]{1,3})?$"
swift_pattern = r"^[A-Z]{6}[0-9A-Z]{2}([0-9A-Z]{3})?$"

# Store the results in a list of objects
extracted_codes = []

# Find all span elements with the class 'block-column-line'
spans = soup.find_all('span', class_='block-column-line')

# Loop through each span and extract the text
for span in spans:
    # Get the entire text of the span
    full_text = span.get_text(separator=" ", strip=True)

    # Check for IBAN using regex
    iban_match = re.search(iban_pattern, full_text)
    if iban_match:
        iban = iban_match.group()
        extracted_codes.append({'type': 'IBAN', 'value': iban})

    # Check for SWIFT (BIC) code using regex
    swift_match = re.search(swift_pattern, full_text)
    if swift_match:
        swift = swift_match.group()
        extracted_codes.append({'type': 'SWIFT', 'value': swift})

# Print the extracted IBAN and SWIFT codes
for code in extracted_codes:
    print(f"{code['type']}: {code['value']}")
