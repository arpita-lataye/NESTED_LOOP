k=1
i=1
while i<=5:
    b=1
    while b<=5-i:
        print(" ",end="")
        b=b+1
    j=1
    while j<=k:
        print("*",end="")
        j=j+1
    k=k+2
    print()
    i=i+1




    # reverse
n=int(input("enter the number:"))
i=1
while(n>0):
    b=1
    while(b<i):
        print(" ",end="")
        b=b+1
    j=1
    while (j<=(n*2)-1):
        print("*",end="")
        j=j+1
    print()
    n=n-1
    i=i+1