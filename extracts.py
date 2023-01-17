import json
import requests
from bs4 import BeautifulSoup

def extract_and_save_to_json(url, filename):
    # Make an HTTP request to the website
    response = requests.get(url)

    # Parse the HTML response
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract all elements with 'data-testid'
    elements = soup.find_all(attrs={'data-testid': True})

    # Save the elements to a JSON file
    with open(filename, 'w') as outfile:
        json.dump(elements, outfile, default=str)

url = "https://www.olx.pt/myaccount/ep/ad/pt_631831701/?applicationId=deba65aa-6c6d-40e9-a3fa-ad8219605e41"
extract_and_save_to_json(url, "elements.json")
