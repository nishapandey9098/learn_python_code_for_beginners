is_male = True
is_tall = True
if is_male and is_tall:
    print("You are a tall male")
else: 
    print("YOu are either not male or not tall or both")

is_male = False
is_tall = True

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male)and is_tall:  #note the use of not
    print("You are not a male but are tall")
else: 
    print("YOu are either not male or not tall or both")


def max_num(num1, num2, num3): #function to find the maximum of three numbers
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(3, 4, 5)) #calling the function and printing the maximum of three numbers
print(max_num(10, 4, 5)) #calling the function and printing the maximum of three numbers