
''' Regular methods take self/Instance as input variable,
 We will learn how to make class method that takes class as input
 as easy as adding @class method decorator'''

 #Static method are that doesn't pass class,or instance of calss in it automatically.They posses logical connection with calsse

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

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, string):#using class method as alternative constructor
        first, last, salary = string.split('-')
        return cls(first, last, salary)

    @staticmethod
    def is_workday(day):
        if day.weekday() ==5 or  day.weekday()==6:
            return False
        return True


add_3='sammy-singh-30000'


Emp1=Emp('Iqbal','Singh',50000)
Emp2=Emp('Tonny','Stark',60000)
Emp3=Emp.from_string(add_3)#using class method as alternative constructor

Emp.set_raise_amt(1.044)#Class Method

print(Emp.raise_amount)
print(Emp1.raise_amount)
print(Emp2.raise_amount)
print(Emp3.first_name)

import datetime
my_date = datetime.date(2016, 7, 10)
print(Emp.is_workday(my_date))
