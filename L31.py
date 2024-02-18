from datetime import datetime,timedelta
import requests

print((datetime.now()))
print((datetime.now() + timedelta(minutes=5)))

response  = requests.get("http://github.com")
urls = ["https://github.com","https://google.com",
        "https://facebook.com"]
for url in urls:
     if requests.get(url).status_code== 200:
         print(url + " is up")


print(response.headers)



