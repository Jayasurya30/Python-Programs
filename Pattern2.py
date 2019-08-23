a="ABCDE"
b=len(a)
ch=""
for i in range(b):
    
    ch=ch+a[i]
    ch=a[:b-i]
    print("\n",ch[::-1],end="")
    print("\n",ch,end="")
  
    
    
    
