from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options

options = Options()
options.page_load_strategy = 'normal'
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
driver.get('https://tracker.gg/valorant/profile/riot/zelly%2310000/overview')