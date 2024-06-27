a = int(input("Enter a frist number:"))
b = int(input("Enter a second number:"))
opr = input("Enter the opr:")
c=1
while(c>0):
    
    if opr=="+":
        print(a+b)
    elif opr=="-":
        print(a-b)
    elif opr=="*":
        print(a*b)
    elif opr=="/":
        print(a/b)
    else:
        print("invalid opr")                

