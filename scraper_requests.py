import requests
from bs4 import BeautifulSoup

def scrape_example():
    # Target URL
    url = 'https://example.com'
    
    try:
        # Send HTTP GET request
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract the title
        title = soup.title.string if soup.title else "No title found"
        print(f"Page Title: {title}")
        
        # Example: Find all paragraph tags
        paragraphs = soup.find_all('p')
        print(f"\nFound {len(paragraphs)} paragraphs:")
        for i, p in enumerate(paragraphs, 1):
            print(f"{i}. {p.get_text()[:50]}...") # Print first 50 chars
            
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Note: Requires 'requests' and 'beautifulsoup4' packages
    # pip install requests beautifulsoup4
    scrape_example()
