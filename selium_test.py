from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def main():     
    driver = webdriver.Chrome() 


    retries = 5
    for x in range(retries):
        try: 
            driver.get("https://order.mandarake.co.jp/order/detailPage/item?itemCode=1305818110&ref=list&dispAdult=0&categoryCode=020104&lang=en")
            retries += 1
        finally:
            print(f"finished {x+1}")
        




if __name__ == '__main__':
    main()
