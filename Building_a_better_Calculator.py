num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)

elif op == "max":
    num3 = float(input("Enter third number: "))    
    if num1 >= num2 and num1 >= num3:
        print(num1)
    elif num2 >= num1 and num2 >= num3:
        print(num2)
    else:
        print(num3)     
elif op == "min":   
    num3 = float(input("Enter third number: "))    
    if num1 <= num2 and num1 <= num3:
        print(num1)
    elif num2 <= num1 and num2 <= num3:
        print(num2)
    else:
        print(num3)
elif op == "avg":   
        num3 = float(input("Enter third number: "))    
        print((num1 + num2 + num3) / 3) 
elif op == "med":
        num3 = float(input("Enter third number: "))    
        if (num1 >= num2 and num1 <= num3) or (num1 <= num2 and num1 >= num3):
            print(num1)
        elif (num2 >= num1 and num2 <= num3) or (num2 <= num1 and num2 >= num3):
            print(num2)
        else:
            print(num3)
else:
    print("Invalid operator")   

#This is a simple calculator that can perform addition, subtraction, multiplication, division, maximum, minimum, average, and median of three numbers.
