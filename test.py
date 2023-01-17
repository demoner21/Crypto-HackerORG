from bs4 import BeautifulSoup
import requests

url = 'https://www.artsolar.pt/#sect-contactos'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

phones = []
emails = []

# Extract the phone numbers
phone_elements = soup.find_all('a', class_='tel')
for phone_element in phone_elements:
    phone = phone_element.text
    phones.append(phone)
    
# Extract the email address
email_elements = soup.find_all('a', class_='mail')
for email_element in email_elements:
    email = email_element.text
    emails.append(email)
    
print(phones)
print(emails)
