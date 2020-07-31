
from functools import wraps#it's used when we stack wrappers

def my_logger(original_function):
    import logging
    logging.basicConfig(filename='{}.log'.format(original_function.__name__),level=logging.INFO)

    @wraps(original_function)
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs {}'.format(args,kwargs))
        return original_function(*args, **kwargs)

    return wrapper

def my_timer(orig_func):
    import time
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time()-t1
        print('{} ran in {} sec'.format(orig_func.__name__,t2))

        return result
    return wrapper

#@my_logger
#def display():
#    print('Display function ran: ')

#display()
import time
#stacking two decorators, order matters
@my_logger
@my_timer
def display_info(name, age):
    time.sleep(1)

    print('Display_info ran with arguments {}, {}'.format(name, age))

#Here display_info = my_logger(my_timer(display_info))
display_info('Iqbal', 26)

