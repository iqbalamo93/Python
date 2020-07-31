print('Opject Oriented Programming!!')

#Method to create class.
#Method 1
class Employee:
    pass

Emp1 = Employee()
Emp2 = Employee()
print(Emp1)
print(Emp2)

#Creating It's attributes 
Emp1.First_name = 'Iqbal'
Emp1.last_name = 'Singh'
Emp1.Email = 'Iqbal.Singh@Comapny.com'
Emp1.Pay = 50,000

Emp2.First_name = 'Tonny'
Emp2.last_name = 'Stark'
Emp2.Email = 'Tonny.Stark@Comapny.com'
Emp2.Pay = 60,000

print(Emp1.Email)

#Now this is tiring process for 100 Emplee, So method 2
class Emp:
    
    def __init__(self,first,last,pay): #Special Init Method
        self.first_name = first
        self.last_name  = last
        self.email      = first+'.'+last+'@company.com'
        self.pay        = pay
    
    def fullname(self): #Clearing Method
        return '{} {}'.format(self.first_name,self.last_name)

Emp1=Emp('Iqbal','Singh',50000)
Emp2=Emp('Tonny','Stark',60000)

print(Emp1.first_name,Emp2.first_name,sep='\n')
Emp1.interst = 'AL|ML' #You can still add attribures 
print(Emp1.interst)
print(Emp1.fullname)
print(Emp1.fullname())


#you can also , run using class directly
print(Emp.fullname(Emp2))





