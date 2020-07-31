'''We have diffrent types of employess '''

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

class Developer(Emp):
    raise_amount =  1.10
    def __init__(self,first,last,pay, prog_lang):
        super().__init__(first,last,pay)
        #Emp.__init__(self,first,last,pay) Alternative of first
        self.prog_lang = prog_lang

class Manager(Emp):
    def __init__(self, first, last, pay, employees= None):#None because , never pass mutable datatype as arguments
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp  in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('--->', emp.fullname())






Dev1=Developer('David','Singh',50000,'Python')
Dev2=Developer('Neou','Stark',60000,'Java')


#print(help(Developer))
#print(Dev1.email, Dev1.prog_lang)

mgr_1 = Manager('sue', 'Smith', 90000, [Dev1])

#isinstance() #prints if object is instance of class
print(isinstance(1,int))
print(isinstance(mgr_1,Manager))
print(isinstance(Developer,Manager))
print(issubclass(Developer,Emp))
print(issubclass(Manager,Emp))
