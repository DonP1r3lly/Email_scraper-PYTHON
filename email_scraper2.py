import re
from bs4 import BeautifulSoup

def scrape_emails(file):
    try:
        with open(file, 'r') as f:
            content = f.read()

        soup = BeautifulSoup(content, 'html.parser')

        
        email_regex = r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-zA-Z0-9-.]+"
        emails = re.findall(email_regex, str(soup))

        print(emails)

    except Exception as e:
        print(f"An error occurred: {e}")

file = input("Enter the name of the HTML file: ")
scrape_emails(file)
