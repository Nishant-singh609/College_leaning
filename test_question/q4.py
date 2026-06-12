
# Q4. Create class AgeVerification: (4 Marks) • Method set_age(age):
# → If age < 0 : raise ValueError
# → If age < 18 : raise custom UnderAgeError → If age > 100 : raise custom InvalidAgeError → Else : print 'Valid age!'
# • Handle all exceptions with finally block.

class AgeVerification:
     def set_age(self,age):
        try:
            self.age=age
            if self.age < 0:
                print("raise ValueError")
            elif self.age < 100 and self.age >=18:
                print('Valid age')
            else:
                print("its ok")
        except:
            print("the age the not possible")
       
A1=AgeVerification()
age=int(input("Enter the age = "))
A1.set_age(age)
                