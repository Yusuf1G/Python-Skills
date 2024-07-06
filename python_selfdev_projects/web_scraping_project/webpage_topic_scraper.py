import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = 'https://www.py4e.com/lessons'  # Replace with the actual URL of the webpage

# Send a GET request to the webpage
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:  # If the request is a success
    page_content = response.text  # This attribute (response.text) returns the content of the response in Unicode format (text)
                                  # Remember response is the object returned by requests.get(url) which retrieves the webpage content.

    print(page_content)  # Print the HTML content to verify it has been retrieved correctly

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(page_content, 'html.parser')

    # Find all div elements with the class 'card'
    card_divs = soup.find_all('div', class_='card')

    # Iterate over each card div
    for card in card_divs:
        # Find the first nested <a> element within the div
        a_tag = card.find('a')
        
        # Check if the <a> element exists and extract its text
        if a_tag:
            link_text = a_tag.get_text()
            print(f'Text: {link_text}')
else:
    print('Failed to retrieve the webpage')  # Error handling if the request fails
    print(f'Status code: {response.status_code}')