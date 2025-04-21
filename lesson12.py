import os

path = r'C:\Program Files (x86)\Steam\dumps'
filename = 'metadata'

for root, dirs, files in os.walk(path):
    print(root)
    if filename in files:
            print(filename)
    else:
            print('такого файла нет')