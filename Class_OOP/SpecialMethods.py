'''__init__
__repr__Meant to be seen by other
__str__ Readable representation of object

Until now
print(Emp1) #<__main__.Emp object at 0x033E04C0> is output
 '''
print('aa'+'ssss') #This uses dunder __add__
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

    def __repr__(self):
        return "Employee({}, {}, {})".format(self.first_name, self.last_name, self.pay)

    def __str__(self):
        return '{}--{}'.format(self.fullname(),self.email)

    def __add__(self,other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

add_3='sammy-singh-30000'


Emp1=Emp('Iqbal','Singh',50000)
Emp2=Emp('Tonny','Stark',60000)
Emp3=Emp.from_string(add_3)

print(Emp1) #<__main__.Emp object at 0x033E04C0>
print(repr(Emp1),Emp1.__repr__())
print(str(Emp1),Emp1.__str__())

print(int.__add__(1,2))
print(str.__add__(str(1),str(10)))


print(Emp1 + Emp2)

print(Emp.__add__(Emp1,Emp2))

print(Emp1.__len__() , Emp2.__len__())
print(len(Emp3))
