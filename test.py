from selenium import webdriver
from time import sleep

dr = webdriver.Chrome()
#dr = webdriver.Edge()
dr.get("http://localhost:81")


sleep(10)