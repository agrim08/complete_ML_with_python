def pallindraome_checker(string):
    string.lower().replace(" ", "")
    if string == string[::-1]:
        return True
    else:
        return False
    
print(pallindraome_checker("aba"))
print(pallindraome_checker("AbA"))
print(pallindraome_checker("hdgsjwagd"))

