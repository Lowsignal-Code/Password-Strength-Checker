import time

print("-" * 45)
print("A Simple Code for Checking Password Strength")
print("You password must have least 8 Chracter You Can Use: a-A , 0-9 , $@!")
print("-" * 45)
print("")


while True:
    password = input("Enter your password: ")
    length = len(password)
    print("Password Analysis")
    print("-" * 45)
    has_number = False
    has_upper = False
    has_lower = False
    has_special = False
    special_chars = "$@!#%&*"
    score = 0

    if length >= 8:
        score += 2
        for character in password:
            if character.isdigit():
                has_number = True
            if character.isupper():
                has_upper = True
            if character.islower():
                has_lower = True
            if character in special_chars:
                has_special = True
           


        if has_number:
            print("Number Character: OK")
            score += 2
        else :
            print("Number Character: NOT OK")
        if has_upper:
            print("Uppercase Character: OK")
            score += 2
        else :
            print("Uppercase Character: NOT OK")
        if has_lower:
            print("Lowercase Character: OK")
            score += 2
        else :
            print("Lowercase Character: NOT OK")
        if has_special:
            print("Special Character: OK")
            score += 2
        else :
            print("Special Character: NOT OK")








        if score <= 4:
            print("Strength: WEAK")
        elif score <= 7:
            print("Strength: MEDIUM")
        else:
            print("Strength: STRONG")
        print(f"score: {score}/10")

    else :
        print("Password too short")