import os
import matplotlib.pyplot as pyplot
print(f'xx')
print(os.getcwd())
path='C:\\Users\\iqbal\\Desktop\\DataScience\\'
os.chdir(path)
#print(os.getcwd())

def new_path(Folder_name):
	base=os.getcwd()
	Targrt=os.path.join(path,Folder_name)
	print('New path is {a}'.format(a=os.getcwd()))

print(os.getcwd())

new_path('ML_AndrewNG')
