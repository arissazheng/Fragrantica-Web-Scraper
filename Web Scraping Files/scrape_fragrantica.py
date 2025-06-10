from splinter import Browser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os

def init_browser():
    """
    Initialize the Chrome browser for web scraping
    Returns:
        Browser: A splinter Browser instance
    """
    try:
        # Set up Chrome options
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--window-size=1920,1080')
        
        # Get the Chrome driver path
        driver_path = ChromeDriverManager().install()
        
        # Use Splinter's executable_path argument
        executable_path = {"executable_path": driver_path}
        return Browser("chrome", **executable_path, headless=False)
    except Exception as e:
        print(f"Error initializing browser: {str(e)}")
        raise 