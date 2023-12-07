import requests
from bs4 import BeautifulSoup
import sys

# Function to fetch the title of a webpage from its URL
def get_page_title(url):
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        # get the H1 tag text
        title = soup.title.string.strip()
        return title
    except (requests.exceptions.RequestException, AttributeError):
        print(Exception)
        return ''
    

# Read the input text file with URLs
input_file = 'readurl.txt'  # Replace with your desired input file name
with open(input_file, 'r', encoding='utf-8') as file:
    urls = file.read().splitlines()

# Create a new text file for Markdown output
output_file = 'output.md'  # Replace with your desired output file name
with open(output_file, 'w', encoding='utf-8') as file:
    for url in urls:
        if title := get_page_title(url):
            markdown_link = f"[{title}]({url})"
            file.write(markdown_link + '\n\n')
        else:
            file.write(f"{url}\n\n")

print(f"Markdown file '{output_file}' generated successfully.")
