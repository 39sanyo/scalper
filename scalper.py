from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.window import WindowTypes
import argparse
import time




print("-----------------------------------------")
print(" Welcome to santi's VolksUSA 'Scalper'! ")
print("-----------------------------------------")
url = input("[*]Please enter url: ")
max_retries_input = input("\n[*]Please enter amount of tries: ")
print("-----------------------------------------")

# Add the desired user-agent string as an argument
#custom_user_agent ="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
#chrome_options.add_argument(f"{custom_user_agent}")

driver = webdriver.Firefox()

# Initializing chrome web driver

# go into login page of website and login
driver.get("https://volksusa.store/account/login?error=login_required")

def main():

    #captcha wait
    seconds = 50
    print("[*]Please login and solve the CAPTCHA Manually.")
    print("[*]We suggest you use 'Shop' to login")
    while seconds > 0:
        print(f"\r[*]The script will resume in {seconds} seconds", end="")
        time.sleep(1)  # Wait for 30 seconds
        seconds -= 1

    # switch tab then go to doll
    driver.switch_to.new_window(WindowTypes.TAB)
    driver.get(url)
    print(f"\ncurrent URL in new tab: {url}")
    
    print(f"Page title before click: {driver.title}")

    locate()
    locate_output = locate()
    check_out(locate_output)
    pay()


def locate():
    max_retries = int(max_retries_input)
    for attempt in range(max_retries):
        try:
            #locating element
            add_to_cart_element = WebDriverWait(driver, 0).until(EC.visibility_of_element_located((By.CLASS_NAME, 'atc-button--text')))
            print("[*]Add to cart element found! Proceeding...")
            add_to_cart_element.click()
            return True
        except TimeoutException:
            print(f"[*]Add to cart element not found on attempt {attempt + 1}. Refreshing page...")
            driver.refresh()
            if attempt == max_retries - 1:
                print("[*]Max Retries reached. Add to cart element was not found. :(")
                driver.quit
                return False
    

def check_out(x):
        if x == True:
            print("true")
            #check out
            checkout_element = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.NAME, 'checkout')))
            checkout_element.click()
            return True
        else:
            print("false")
            return False


def pay():
    pay_element = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.ID, 'checkout-pay-button-section')))
    pay_element.click()


if __name__ == '__main__':
    # parser = argparse.ArgumentParser(description="A program to scalp dolls" )
    # parser.add_argument('url', type=str, help="url of the doll")
    # args = parser.parse_args()
    main()
