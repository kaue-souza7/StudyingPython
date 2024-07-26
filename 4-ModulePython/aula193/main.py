from time import sleep
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Chrome Options
# https://peter.sh/experiments/chromium-command-line-switches/

# Doc Selenium
# https://selenium-python.readthedocs.io/locating-elements.html



ROOT_FOLDER = Path(__file__).parent
CHROMEDRIVER_EXEC = ROOT_FOLDER / 'drivers' / 'chromedriver.exe'


# chrome_options = webdriver.ChromeOptions() # add_options para adicionar uma opção 
# chrome_service = Service(executable_path=str(CHROMEDRIVER_EXEC))
# chrome_browser = webdriver.Chrome(
#     service= chrome_service,
#     options= chrome_options,
# )

def make_chrome_browser(*options: str ) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    # chrome_options.add_argument('--headless')
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)
    
    chrome_service = Service(
        executable_path=str(CHROMEDRIVER_EXEC),
    )

    browser = webdriver.Chrome(
        service= chrome_service,
        options= chrome_options,
    )

    return browser



if __name__ == '__main__':
    TIME_TO_WAIT = 10
    # Example
    # options = ('--disable-gpu', '--no-sandbox', '--headless')
    options = ()
    browser = make_chrome_browser(*options)

    # Como antes
    browser.get('https://www.google.com.br/')

    # Espere para encontrar o input
    search_input = WebDriverWait(browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located(
            (By.NAME, 'q')
        )
    )
    search_input.send_keys('Hello World')
    search_input.send_keys(Keys.ENTER)

    results = browser.find_element(By.ID, 'search')
    links = results.find_elements(By.TAG_NAME, 'a')
    links[0].click()


    # sleep 10'seconds
    sleep(TIME_TO_WAIT)

    # Selecionando




# chrome_browser.get('https://www.google.com.br/')
# time.sleep(30)

