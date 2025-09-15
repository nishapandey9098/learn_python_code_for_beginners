try: #This block will be executed first
    number = int(input("Enter a number: ")) 
    print (number)#Try to convert input to an integer
except:
    print ("Invalid input. Please enter a valid number.") #If conversion fails, this block will be executed

try: #This block will be executed first
    answer = 10 / 0 #Try to divide by zero
    number = int(input("Enter a number: "))
    print (number)
except ZeroDivisionError as err:
    print(err) #If division by zero occurs, this block will be executed 
except ValueError:
    print ("Invalid input. Please enter a valid number.")
    