n=int(input())
sum=0
dig=0
while(n>0):
    d=n%10
    n=n//10
    sum=sum+d
while(sum>0):
    b=sum%10
    sum=sum//10
    dig=dig+b
print(dig)

    
