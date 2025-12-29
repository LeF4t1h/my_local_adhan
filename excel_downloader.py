from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import os
from config import DOWNLOAD_DIR, CHROMEDRIVER_PATH


def download_excel() -> None:
    """Uses Selenium to download the Excel file from the diyanet website."""

    print("Downloading Excel file...")

    # Set download folder
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)

    chrome_options = Options()
    chrome_options.add_experimental_option(
        "prefs",
        {
            "download.default_directory": DOWNLOAD_DIR,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True,
        },
    )
    chrome_options.add_argument("--headless=new")

    # Path to chromedriver
    service = Service(CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Open the website
    driver.get(
        "https://namazvakitleri.diyanet.gov.tr/de-DE/10919/gebetszeit-fur-bensheim"
    )

    # Wait for the table and button to load
    time.sleep(1)  # adjust based on your page load

    # Find the 'jährliche Gebetszeiten' button and click it
    tab_button = driver.find_element(
        By.XPATH, "//*[contains(text(), 'jährliche Gebetszeiten')]"
    )
    tab_button.click()

    # Find the 'Excel' button and click it
    excel_button = driver.find_element(By.XPATH, "//*[contains(text(), 'Excel')]")
    excel_button.click()

    # Wait for download to finish
    time.sleep(1)

    driver.quit()
    print(f"Excel file should be downloaded to: {DOWNLOAD_DIR}")
