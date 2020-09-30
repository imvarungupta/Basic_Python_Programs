import re
s = int(input("if you are searching Case sensitive letter so press 1 \n otherwise press 2 \n"))
print (s)
if(s == 1):
    a = str(input(" enter any string "))
    print (a)
    b = str(input("enter the search element whatever you want \n"))
    print (b)
# second Parameter will be left side and first parameter will be right side.
    if re.search (b,a):
        print ("yes, it's present")
    else:
        print ("No, it's not present")
if (s == 2):
    a = str(input(" enter any string ")).lower()
    print(a)
    b = str(input("enter the search element whatever you want")).lower()
    print(b)
    # second Parameter will be left side and first parameter will be right side.
    if re.search(b, a):
        print("yes, it's present")
    else:
        print("No, it's not present")



