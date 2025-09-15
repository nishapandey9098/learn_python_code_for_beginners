from student import Student

student1 = Student("Jim", "Business", 3.1, False)
print(student1.name)
print(student1.gpa)

from student import Student
student2 = Student("Pam", "Art", 2.5, True)
student3 = Student("Oscar", "Accounting", 3.8, False)    
print(student2.name)
print(student2.is_on_probation)
print(student3.name)
print(student3.gpa)
print(student3.major)
print(student3.on_honor_roll())

