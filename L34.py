import requests
import traceback
try:
    requests.get("https//google.asd")
except BaseException as e:
    print("runtime error")
    print(e.args)


#  traceback.print_exc()


def  calc(res):
    res = 0
    while res == 0:
        try:
            a = int(input("insert first number "))
            b = int(input("insert second number "))
            res = a - b
            return res
        except ValueError:
            print("print a legal number")
        except ZeroDivisionError:
            print("cannot divide by 0")


print(calc(0))
