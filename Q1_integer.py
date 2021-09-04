# n=int(input("enter the number:"))
# i=1
# while (i<=n):
#     if i%2 !=0:
#         print("weird")
#     else:
#         print(i)
#     i=i+1

# n=5
# i=2
# (2-5)
# for i in range (2,5):
#     if (i%2==0):
#         print("not weird")
#     else:
#         print(i)

# i=6
# (6,20)
# for i in range (6,20):
#     if (i%2==0):
#         print("wierd")
#     else:
#         print(i)



# (20,n)
# i=20
# for i in range (20,n):
#     if (i%2==0):
#         print("not wierd")
#     else:
#         print(i)

n=int(input("enter number:"))
i=2
sum=0
count=0
while count<=n:
    if i%2==0:
        sum=sum+i
        count=count+1
    i=i+1
print("sum of even number=",sum)
