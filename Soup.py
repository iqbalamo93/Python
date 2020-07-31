import shutil
import zipfile
import os

print(os.getcwd())
fiename='Online PF transfer-IN guideline.zip'
From='C:\\Users\\iqbal\\Downloads\\Compressed\\Online PF transfer-IN guideline.zip'
to='C:\\Users\\iqbal\\Desktop'
shutil.move(From,to)

os.chdir(to)
print(os.getcwd())
zi=os.path.join(to,fiename)
print(zi)
with zipfile.ZipFile(zi) as file:
	file.extractall(to)