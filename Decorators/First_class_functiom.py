def square(x):
    return x*x

f= square #F is variable so it's first class function,We assigned function to a variable
#print(f)
#print(f(5))

'''Higher order function'''
#that accepts a function or accepts a function and output the function
#input function//output function
#Example Map,filter

def my_map(func, arg_list):#here () was not used  No execution
    result = []
    for i in arg_list:
        result.append(func(i))
    return result   

squares = my_map(square,[1,2,3,4,5])
#print(squares)

#Output the function
def logger(msg):
    def log_message():
        print('log:',msg)

    return log_message
log_hi = logger('Hiiiii \n')#Log_hit is function as log_message():
log_hi() # beacuse return is without ()
#Above two are closures 

def html_tag(tag):
    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))
    return wrap_text

print_h1 = html_tag('h1')
print(print_h1) #<function html_tag.<locals>.wrap_text at 0x03035070> funcution waiting to get execute 
print(print_h1.__name__)
'''So, if I got it right, closures are when a function 
remembers the environment it was created it, specifically the variables around it.'''
#On in closure lecture
print_h1('Test Headline!')
print_h1('Another Headline!\n \n')

print_p = html_tag('p')
print_p('Test Paragraph')