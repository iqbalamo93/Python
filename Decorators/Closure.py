def outer_func():

    message = 'Hi'

    def inner_function():
        print(message)
    return inner_function # executes innerfunction

my_func = outer_func()

'''So, if I got it right, closures are when a function 
remembers the environment it was created it, specifically the variables around it.'''

my_func()
my_func()
my_func()
""" Creating a log system using closure"""

import logging
logging.basicConfig(filename='example.log', level=logging.INFO)

def logger(func):
    def log_func(*args):
        logging.info(
            'Running "{}" with arguments {}'.format(func.__name__, args)
        )
        print(func(*args))
    return log_func

def add(x, y):
    return x+y

def sub(x, y):
    return x-y

add_logger = logger(add)
sub_logger = logger(sub)

add_logger(3,55)
sub_logger(4,55)