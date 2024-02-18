def get_difficulty():
    return get_int("Enter Difficulty level(number):")

def get_int(msg):
    while True:
        try:
            num = float(input(msg))
            if round(num) > 0:
                return round(num)
                break
            else:
                print("Please enter a Positive Value")
        except ValueError:
            print("Not a Numer please retry")
