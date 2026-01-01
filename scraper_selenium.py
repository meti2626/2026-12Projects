from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def scrape_dynamic_example():
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)
    
    print("Initializing WebDriver...")
    # Note: Ensure you have the appropriate WebDriver installed (e.g., chromedriver)
    try:
        driver = webdriver.Chrome(options=chrome_options)
        
        url = 'https://example.com'
        print(f"Navigating to {url}...")
        driver.get(url)
        
        # Wait for dynamic content if necessary (simple sleep for demonstration)
        # Ideally use WebDriverWait for specific elements
        time.sleep(2)
        
        # Get page title
        print(f"Page Title: {driver.title}")
        
        # Find elements
        elements = driver.find_elements(By.TAG_NAME, 'div')
        print(f"Found {len(elements)} div elements")
        
        # Example: Extract text from the first h1 tag
        try:
            header = driver.find_element(By.TAG_NAME, 'h1')
            print(f"Header text: {header.text}")
        except:
            print("No h1 tag found")
            
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Clean up and close the browser
        if 'driver' in locals():
            driver.quit()
            print("WebDriver closed.")

if __name__ == "__main__":
    # Note: Requires 'selenium' package and a WebDriver (like chromedriver)
    # pip install selenium
    scrape_dynamic_example()
