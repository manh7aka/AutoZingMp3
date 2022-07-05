from autozingmp3.browser.driver_factory import WebDriverFactory, WebDriverConfigs
from autozingmp3.zingmp3.home_page import HomePage
import sys 
import time 

if __name__ == "__main__":

    configs = WebDriverConfigs()
    wdf = WebDriverFactory(configs=configs)
    driver = wdf.getWebDriverInstance()

    # # Send a get request to the url
    # driver.get('https://zingmp3.vn/')

    # # auto home page 
    # homepage = HomePage(driver=driver)
    # # login by cookies
    # homepage.load_cookie()
    # driver.get('https://zingmp3.vn/')
    # # search for song name
    # homepage.search_for_song('Cạn cả nước mắt')

    driver.get('https://mp3.zing.vn/bai-hat/Cho-Toi-Lang-Thang-Ngot-Den/ZW79DF7C.html')

    while True:
        try:
            input()
        except KeyboardInterrupt:
            sys.exit()
