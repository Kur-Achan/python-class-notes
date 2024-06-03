class Student:
    name = "Angela"
    school = "AkiraChix"
    code = 22
    age = 22
    
        school ="AkiraChix"
        def __init__(self,firstname,lastname,age,country,code):
             self.firstname=firstname
             self.lastname=lastname
             self.age=age
             self.country=country
             self.code=code 

        def greeting_student(self):
               greeting =f"Hello {self.firstname} welcome to {self.school} your code is{self.code} "  
               return greeting  
        
        def year_of_birth(self):
               return f"Hello {self.firstname} I was born {self.year_of_birth}"
        