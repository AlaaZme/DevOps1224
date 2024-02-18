file = open("names.txt")

def readallnames():
    file = open("names.txt","r")
    for name in file.readlines():
        print(f"{name}",end='')


newnames = ["1\n","2\n","3\n","4\n"]
def createnewnames(inlist):
   file2 = open("names.txt","a")
   for name in inlist:
       file2.writelines(name)




createnewnames(newnames)
readallnames()

