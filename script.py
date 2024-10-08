import requests
from bs4 import BeautifulSoup

def scrape_data():
    url = 'https://www.google.com'  # Replace with your target URL

    try:
        # Make a request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the title of the page
        title = soup.title.string if soup.title else 'No title found'
        
        # Open the file to save the scraped data
        with open('scraped_data.txt', 'w') as file:
            file.write(f"Title of the page: {title}\n\n")
            
            # Scrape all links on the page
            links = soup.find_all('a')
            for link in links:
                href = link.get('href')
                text = link.string.strip() if link.string else ''
                if href and text:  # Check if both href and text exist
                    file.write(f"Link text: {text}, URL: {href}\n")
        
        print("Data scraped successfully and saved to scraped_data.txt!")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")

def main():
    scrape_data()

if __name__ == '__main__':
    main()
