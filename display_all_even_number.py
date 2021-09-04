# que 9
# display all even numbers that fall between two numbers 
# exclusive both numbers entered by the user

a=int(input("enter the number:"))
b=int(input("enter the number:"))
while a<=b:
    if a%2==0:
        print(a)
    a=a+1