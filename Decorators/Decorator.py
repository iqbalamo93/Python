'''Decorator is a function that takes a function as input adds some functionality and return it '''

def decorator_function(Orginal_function):
    def wrapper_function(*args, **Kwargs):
        print('Wrapper executed this before {}'.format(Orginal_function.__name__))
        return Orginal_function(*args, **Kwargs)
    return wrapper_function

#def display():
   # print('Display function ran: ')

#decorated_display = decorator_function(display)

#decorated_display()

@decorator_function
def display():
    print('Display function ran: ')
#display = decorator_function(display): Is what above does.
display()

@decorator_function
def display_info(name, age):
    print('display_info ran with arguments {}, {}'.format(name, age))

display_info('Iqbal', 26)

''' Using Class as decorators-----'''
class  decorator_class(object):
    """docstring for  """
    def __init__(self, Original_function):
        self.Original_function = Original_function

    def __call__(self, *args, **kwargs):
        print('Call method  executed this before {}'.format(self.Original_function.__name__))
        return self.Original_function(*args, **kwargs)


@decorator_class
def display():
    print('Display function ran: ')
#display = decorator_function(display): Is what above does.
display()

@decorator_class
def display_info(name, age):
    print('display_info ran with arguments {}, {}'.format(name, age))

display_info('Iqbal', 26)






