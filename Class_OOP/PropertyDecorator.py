''''Getters, Setters, and Deleters'''

class Emp:
    number_of_employee = 0 #Example of class Variable
    raise_amount = 1.04    #Another  class Variable

    def __init__(self,first,last,pay): #Special Init Method
        self.first_name = first
        self.last_name  = last
        self.pay        = pay
        Emp.number_of_employee +=1

    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first_name, self.last_name)

    @property
    def fullname(self): #Clearing Method
        return '{} {}'.format(self.first_name,self.last_name)

    @fullname.setter
    def fullname(self,name):
        first, last = name.split(' ')
        self.first_name = first
        self.last_name  = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last  = None


    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

Dev1=Emp('David','Singh',50000)
Dev2=Emp('Neou','Stark',60000)

print(Dev1.email)
print(Dev1.fullname)

Dev1.fullname = 'Corey Schafer'

print(Dev1.email)
del Dev1.fullname

print(Dev1.email)

