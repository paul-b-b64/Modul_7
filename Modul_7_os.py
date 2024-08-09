import os
import time


directory = os.getcwd()
print(directory)
for i in os.walk(directory):
    print(i)

dd = os.path.join(directory)
print(dd)

list_dir = os.listdir(dd) # список содержимого текущей директории
seconds = os.path.getmtime(list_dir[6]) # произвольный файл из этого списка
time_local = time.ctime(seconds)
print(time_local)
print(os.path.getsize(dd))
print(os.path.dirname(dd))
