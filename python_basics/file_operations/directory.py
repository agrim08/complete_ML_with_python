import os

new_directory = 'package'
os.mkdir(new_directory)
print(f"Directory '{new_directory}' create")

#listing files and directories:
itmes = os.listdir('.')
print(itmes)