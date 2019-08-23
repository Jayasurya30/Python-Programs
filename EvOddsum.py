


def rev(n):
    rev=0
    while(n!=0):
        rev=(rev*10)+(n%10)
        n=n//10
    return rev
def sum(n):
    n= rev(n)
    sumodd=0
    sumeven=0
    c=1
    while(n!=0):
        if(c%2==0):
            sumeven += n%10
        else:
            sumodd += n%10
        n=n//10
        c=c+1
    print(sumodd)
    print(sumeven)
n=int(input())
sum(n)
