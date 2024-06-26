def password_checker(password):
    if len(password) < 8:
        return False
    elif not any(char.islower() for char in password):
        return False
    elif not any(char.isdigit() for char in password):
        return False
    elif not any(char.isupper() for char in password):
        return False
    elif not any(char in '!@#$%^&*_+-~' for char in password):
        return False

    return True

result = password_checker("Agrim@123")
if result == True:
    print("Your password is correct")
else:
    print("please choose a different password")