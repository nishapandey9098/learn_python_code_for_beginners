

employee_file = open("employees.txt", "r") 

print(employee_file.readlines()[1])
employee_file.close() 

employee_file = open("employees.txt", "r") 

print(employee_file.read())
employee_file.close() 
 
employee_file = open("employees.txt", "r") 
for employee in employee_file.readlines():
    print(employee)
employee_file.close() 



employee_file = open("employees1.txt", "w") 
employee_file.write("\nKelly - Customer Service") 
employee_file.write("\nbob - IT")
employee_file.close()        

employee_file = open("employees.txt", "a") 
employee_file.write("\nbob - IT")
employee_file.close() 

employee_file = open("index.html", "w") 
employee_file.write("<p>This is a HTML</p>") 
employee_file.close()        