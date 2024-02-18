def NegativeAgeError():
    print("negative value")



def get_user_age():
    try:
        age = int(input("enter your age "))
        if age <=0:
           NegativeAgeError()
        else:
            return age

    except BaseException as e:
        print("retry")
        print(e.args)

