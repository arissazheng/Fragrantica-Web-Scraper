import sys
import os

# Add the Web Scraping Files directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'Web Scraping Files'))

from scrape_fragrantica import init_browser

def test_browser():
    try:
        print("Initializing browser...")
        browser = init_browser()
        print("Browser initialized successfully!")
        
        print("Visiting test website...")
        browser.visit("https://www.google.com")
        print("Successfully visited website!")
        
        print("Closing browser...")
        browser.quit()
        print("Browser closed successfully!")
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        raise

if __name__ == "__main__":
    test_browser() 