while True:
    a=int(input("Enter the mark:"))
    if(a>100):
        print("The given mark is invalid")
    elif (a>=90 and a==100):
        print("A Grade")
    elif (a>=70 and a<90):
        print("B grade")
    elif (a>=50 and a<70):
        print("C grade")
    else:
        print("D grade")
else:
    print("e grade")
