import requests
import json
from selenium import webdriver
from time import sleep

import sys
print(sys.path)

print(sys.executable)

#API 1
response1 = requests.get("https://api.github.com/users/avielb/repos")

toj = response1.json()

#print(json.dumps(toj, indent=2))
l = []
i=0
for r in toj:
   print("url,  ", r["url"])
   l.append(r["url"])


print(len(l))


repo_num = len(response1.json())

expected = 5
assert repo_num >= expected



#API 2
"""
fake = Faker()
expected_max = 120
expected_min = 0
for i in range(0, 3):
    temp_name = fake.first_name()
    url = "https://api.agify.io/?name=%s" % temp_name
    print(url)
    response2 = requests.get(url)
    to_json = response2.json()
    age = to_json["age"]
    assert ((int(age) < expected_max) & (int(age) > expected_min))

#API 3

response3 = requests.get("http://universities.hipolabs.com/search?country=Israel")
uni_num = len(response3.json())
expected_uni_num= 5
assert expected_uni_num <= uni_num

#URL 4


dr1 = webdriver.Chrome()
dr1.get("https://www.ycombinator.com")
title = dr1.find_element(by="xpath",value="//*[@id=\"why-yc-page\"]/div[2]/div[1]/div/div/div[1]/div[1]/div[2]").text
expected_title= "Y Combinator?"
assert expected_title==title


#URL 5    -----<<>>> this does not always work. tried multiple ways (sometimes returns "Docker"
dr2 = webdriver.Chrome()
expected_title_hub = "Docker Hub Container Image Library | App Containerization"
dr2.get("https://hub.docker.com")
sleep(5)
tittle_rtn = dr2.title
print(tittle_rtn)
assert expected_title_hub==tittle_rtn 

"""