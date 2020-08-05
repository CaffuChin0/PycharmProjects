import re

password = str(input())

def lenOK(pwd):
    if(len(pwd)>=8):
        return True
    else:
        print("WARNING: The password should be at least 8 characters.")
        return False

def numberOK(pwd):
    pattern = re.compile('[0-9]+')
    match = pattern.findall(pwd)
    if match:
        return True
    else:
        print("WARNING: The password should include at least 1 number.")
        return False

def upperOK(pwd):
    pattern = re.compile('[A-Z]+')
    match = pattern.findall(pwd)
    if match:
        return True
    else:
        print("WARNING: The password should include at least 1 upper character.")
        return False

def lowerOK(pwd):
    pattern = re.compile('[a-z]+')
    match = pattern.findall(pwd)
    if match:
        return True
    else:
        print("WARNING: The password should include at least 1 lower character.")
        return False

def symbolOK(pwd):
    pattern = re.compile('^[a-z0-9A-Z]+')
    match = pattern.findall(pwd)
    if match:
        return True
    else:
        print("WARNING: The password should start with numbers or characters.")
        return False

def checkpwd(pwd):
    check = lenOK(pwd) and numberOK(pwd) and upperOK(pwd) and lowerOK(pwd) and symbolOK(pwd)
    if (check):
        print("The password is legal.")
    else:
        print(check)

checkpwd(password)