def say_hi(): #This is a function
    print("Hello User") #This is the body of the function
    
print("Top") #This is outside the function   
say_hi() #This calls the function
print("Bottom") #This is outside the function

def sayhi(name): #This function takes a parameter
    print("Hello " + name) #This uses the parameter
    
sayhi("Alice") #This calls the function with an argument
sayhi("Bob")

def say_hi(name, age): #This function takes two parameters
    print("Hello " + name + ", you are " + str(age) + " years old.") #This uses both parameters
say_hi("Charlie", 30) #This calls the function with two arguments
say_hi("Diana", 25)