import re
import requests
from bs4 import BeautifulSoup

#response= requests.get('http://localhost/test.html')
with open(r'C:\Users\YOUR_USER\Documents\index.html', 'r') as file:
    content=file.read()

# Parse the page content

#soup= BeautifulSoup(response.text, 'html.parser')
soup=BeautifulSoup(content, 'html.parser')

#Find emails in the page
email_regex= r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+"
emails= re.findall(email_regex, str(soup))

print(emails)