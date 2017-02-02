a,b=input().split()
a=int(a)
b=int(b)
if (a,b>=0):
 c=1
 while( c<=b):
        a-=1
        c+=1
        if (a>0):
            print(a)
            print(b)
        else:
            print(b)
            print(a)
elif (a,b<=0):
 c=1
 while (c<= -b):
        a+=1
        c+=1
        if (a>0):
            print(a)
            print(b)
        else:
            print(b)
            print(a)
elif (a>=0 , b<=0):
    print(a)
    print(b)
else:
    print(b)
    print(a)
    
