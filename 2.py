'''
x = 1

if x == 2:
      print("x is 2")
print("end of loop")
name = input("enter your name: ")
if name == "alaa":
    print("good!")
else:
    print("no good")

int1 = input("enter int1: ")
int2 = input("enter int2: ")
if int1<int2:
       print("int2 is bigger")
else:
    print("int1 is bigger")
 '''
fname = "alaa "
lname = "daoud"
full_name = "alaa " + "daoud"
full_name2 = "%s %s" % (fname, lname)
full_name3 = f"{fname} {lname}"
full_name4 = "{} {}".format(fname, lname)

print(full_name)
print(full_name2)
print(full_name3)
print(full_name4)

full_desc = "name: " + fname  + "\nlast nane: "+ lname +"\nage= 30"
print(full_desc)