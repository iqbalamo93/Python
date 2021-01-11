#!/usr/bin/env python
# coding: utf-8
# # Python Multiprocessing: Run Code in Parallel Using the Multiprocessing Module
#
#
# We usually have two types of tasks:
# - IO Bound: Waitinng for input and output to be completed
#  - File system operation, file system operation
#
# - CPU Bound:Number crunching

import platform
import time
print('Os Version:', platform.version())
print('Os Version:', platform.python_version())

start = time.perf_counter()


def do_someting(Text=None):
    print('Sleeping 1 second')
    time.sleep(1)
    print('Done sleeping...')

    if Text:
        print(Text, end='\n\n')


do_someting()
do_someting()
do_someting(Text='This was final')

import multiprocessing as mp

p1 = mp.Process(target=do_someting)
p2 = mp.Process(target=do_someting)

finish = time.perf_counter()

p1.start()
p2.start()
finish = time.perf_counter()
print(f'Finished in {round(finish-start,2)} seconds')
'''
while our p1, p2 were sleeping(running in backround) script moved to print statement so you see print
is
'''


def printer():
    time.sleep(1)
    print(f'We done itafter {1} sec')


start_again = time.perf_counter()
p3 = mp.Process(target=printer)
p4 = mp.Process(target=printer)
p3.start()
p4.start()
p3.join()
p4.join()
finish_again = time.perf_counter()
print(f'Finished priter in {round(finish_again-start_again,2)} seconds')

start_ = time.perf_counter()
processess = []
for _ in range(10):
    p = mp.Process(target=do_someting)
    p.start()
    processess.append(p)

for process in processess:
    process.join()

finished_grp = time.perf_counter()
print(f'Finished loop in {round(finished_grp-start_,2)} seconds')
# N_cores working together can do 10 sec jo in 1 sec !!!!

def do_someting(seconds):
    