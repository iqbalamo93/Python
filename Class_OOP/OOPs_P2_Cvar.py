print('Opject Oriented Programming!!: Class Variables')


class Emp:
    number_of_employee = 0 #Example of class Variable
    raise_amount = 1.04    #Another  class Variable

    def __init__(self,first,last,pay): #Special Init Method
        self.first_name = first
        self.last_name  = last
        self.email      = first+'.'+last+'@company.com'
        self.pay        = pay

        Emp.number_of_employee +=1
    
    def fullname(self): #Clearing Method
        return '{} {}'.format(self.first_name,self.last_name)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        #Emp.raise_amount can also be used, 
        #both has huge difference, self checks if object has attribute , if not then class

#Emp.raise_amount = 2 #This impacts class and all it's instances 

Emp1=Emp('Iqbal','Singh',50000)
Emp2=Emp('Tonny','Stark',60000)

print('Default pay {} and'.format(Emp1.pay))
print('Deafult raise amount for Emp1 is:  {}'.format(Emp1.raise_amount))
print('\n {}'.format(Emp1.__dict__)) # To show it EMP doesn't have Raise as explicit attribute
print('Deafult raise amount for all is:  {}'.format(Emp.raise_amount))
print('\n Dict for class {}'.format(Emp.__dict__)) # To show it EMP doesn't have Raise as explicit attribute
#Class variable can be accessed via both Class and object of class
Emp1.apply_raise()
print(Emp1.pay)
print('\n  Attributes post apply {}'.format(Emp1.__dict__)) 
Emp1.raise_amount= 1.05
print('New  raise amount for Emp1 is:  {}'.format(Emp1.raise_amount))
Emp1.apply_raise()
print(Emp1.pay, sep='\n')


print(Emp1.__dict__,sep='\n') #This prins all the attributes as a dictionary
Emp1.raise_amount =1.05
print('\n New attribtes : {}'.format(Emp1.__dict__) )#This print all the attributes as a Class
Emp.raise_amount = 2 
print(Emp.__dict__) #New raise amount is 2
print('\n \t New Deafult raise amount for Emp1 is:  {}'.format(Emp1.raise_amount))# It's same old value 
#Because it's checking for variable and that exists, Uncommect and check it's same
Emp2.apply_raise()
print('Emp2 New pay is {} V/s of old Pay of :{}'.format(Emp2.pay,60000), sep='\n')
Emp1.apply_raise()

print(Emp1.pay, sep='\n')


print(Emp.number_of_employee)
