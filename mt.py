import requests
from bs4 import BeautifulSoup

Facebook mobile contact page URL
url = "(link unavailable)"

Send HTTP GET request
response = requests.get(url)

Parse HTML response using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

Find specific elements on the page
For example, lets find all contact names
contact_names = soup.find_all('div', {'class': '_39g5'})

Print contact names
for name in contact_names:
    print(name.text.strip())
