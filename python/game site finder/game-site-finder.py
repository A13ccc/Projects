import requests
from bs4 import BeautifulSoup
import re

# Prefilled base URL for the raw content
raw_base_url = "https://raw.githubusercontent.com/rooftopsnipers2/rooftopsnipers2.github.io/main/play/"

# GitHub API URL for the directory listing
api_url = "https://api.github.com/repos/rooftopsnipers2/rooftopsnipers2.github.io/contents/play"

# Get the list of files in the play directory
response = requests.get(api_url)

# Check if the request was successful
if response.status_code == 200:
    files = response.json()

    # Filter for HTML files
    html_files = [file['name'] for file in files if file['name'].endswith('.html')]

    for game_name in html_files:
        # Construct the full raw content URL for each game
        url = raw_base_url + game_name

        # Send a GET request to fetch the HTML content
        response = requests.get(url)

        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all iframe tags
            iframes = soup.find_all('iframe')

            # Loop through all iframe tags
            for iframe in iframes:
                src = iframe.get('src')
                if src and 'htmlxm' in src:
                    # Append the URL to a file with a newline
                    with open('output.txt', 'a') as file:
                        file.write(src + '\n')
                    print(f"Match found and added: {src}")
                    break  # Stop after the first match with 'htmlxm'

        else:
            print(f"Failed to fetch {game_name}. Status code: {response.status_code}")

else:
    print(f"Failed to retrieve directory listing. Status code: {response.status_code}")
