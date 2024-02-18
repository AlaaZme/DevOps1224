from selenium import webdriver
from time import sleep

dr = webdriver.Chrome()
#dr = webdriver.Edge()
dr.get("file:///C:/Users/AlaaZme1/Downloads/tip_calc/tip_calc/index.html")

billamt = dr.find_element(by="id" , value="billamt")
billamt.send_keys("100")

peopleamt = dr.find_element(by="id" , value="peopleamt").send_keys("1")
serviceQual = dr.find_element(by="xpath",value="//*[@id=\"serviceQual\"]/option[4]").click()
music = dr.find_element(by="xpath",value="//*[@id=\"music\"]/option[5]").click()

dr.find_element(by="id",value="calculate").click()

tip = dr.find_element(by="id",value="tip").text
expceted = "19.00"

assert expceted == tip


#if expceted == tip:
#    print("all good")
#else:
#    print("bad test")
#print(tip)
#serviceQual = send_keys("1")
sleep(1)
print("test")