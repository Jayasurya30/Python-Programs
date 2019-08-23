a=input("username:")
b=input("password:")
c=input("confirm password:")
d=input("mobile number:")
e=input("email ID:")
if(a==" ", b==" ", c==" ",d ==" ",e ==" "):
    print("please fill all the fields")
elif b!=c:
    print("given pass is not same")
elif len(d)>10 or len(d)<10:
    print("mobile number is invalid")
else:
    print("register success")
 
