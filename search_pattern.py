import re
def search_Pattern():
    print('=' * 10, 'Pattern Matching', '=' * 10)
    s = int(input("if you are searching Case sensitive letter so press 1 \n otherwise press 2 \n"))
#print (s)
    if(s == 1):
        print('=' * 10, 'Sensitive Pattern Matching', '=' * 10)
        a = str(input("Enter any string ..."))
    #print (a)
        b = str(input("enter the search pattern whatever you want \n"))
    #print (b)
    # second Parameter will be left side and first parameter will be right side.
        if re.search (b,a):
            print ("yes, it's present ...")
        else:
            print ("No, it's not present ...")
    if (s == 2):
        print('=' * 10, 'InSensitive Pattern Matching', '=' * 10)
        a = str(input(" enter any string ")).lower()
        print(a)
        b = str(input("enter the search pattern whatever you want")).lower()
        print(b)
        # second Parameter will be left side and first parameter will be right side.
        if re.search(b, a):
            print("yes, it's present")
        else:
            print("No, it's not present")


if __name__ == "__main__":
    search_Pattern()
    v = int(input("press enter 1 for exit"))
    if (v == 1):
        exit
    else:
        search_Pattern()



