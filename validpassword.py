def check(password):
    if len(password)<4:
        return 0
    has_digit=False
    has_capital=False
    if ' ' in password or '/' in password:
        return 0
    if password[0].isdigit():
        return 0
    for char in password:
        if(char.isdigit()):
            has_digit=True
        if(char.isupper()):
            has_capital=True
    if has_digit and has_capital:
        return 1
    else:
        return 0
        
password=input()
print(check(password))