from time import sleep
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.remote.webelement import WebElement



ROOT_FOLDER = Path(__file__).parent
CHROMEDRIVER_EXEC = ROOT_FOLDER / 'drivers' / 'chromedriver.exe'


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

    options = ('--headless')
    browser = make_chrome_browser(*options)

    url = 'https://weather.com/pt-BR/clima/10dias/l/dfb390d5d0537ed3c80f13693bce4fb5ab75fb5fa1ddd5c46fb61fc04264005d'

    # Como antes
    browser.get(url)
    sleep(10)
    div = browser.find_element(By.ID, 'WxuDailyCard-main-a43097e1-49d7-4df7-9d1a-334b29628263')
    details = div.find_elements(By.TAG_NAME, 'details')
    
    
    # Apagando o primeiro detail sem utilidade
    # details.pop(0)

    # Teste:
    # print(len(details))
    # day = details[8].find_element(By.CLASS_NAME, 'DetailsSummary--daypartName--kbngc').text
    # print(day)

    weather_data = []
    sleep(10)
    for index in range(len(details)):
        detail = details[index]
        
        day = detail.find_element(By.CLASS_NAME, 'DetailsSummary--daypartName--kbngc').text
        # day = details[10].find_element(By.TAG_NAME, 'h2').text # DetailsSummary--daypartName--kbngc')

        high_temperature = detail.find_element(By.CLASS_NAME, 'DetailsSummary--highTempValue--3PjlX').text
        low_temperature = detail.find_element(By.CLASS_NAME, 'DetailsSummary--lowTempValue--2tesQ').text
        temperature = f'{low_temperature}/{high_temperature}'

        climate = detail.find_element(By.CLASS_NAME, 'DetailsSummary--extendedData--307Ax').text
        
        information_day = {'day': day, 'temperature': temperature, 'climate': climate}

        weather_data.append(information_day)
        

    for day in weather_data:
        print(day['day'],'->',  day['temperature'], day['climate'])
        print()

    print(weather_data[8])
    # Sleep 10'seconds
    sleep(10)