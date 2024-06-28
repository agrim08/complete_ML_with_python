import re

pattern = r'\d+' #d means digits
text = "there are 123 apples and 456 mangoes" #it stops after 1st match and does not print 456
match = re.search(pattern,text)
print(match.group())
