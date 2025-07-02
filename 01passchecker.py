'''
Password Validity Rules:
    1. At least 12 characters
    2. Atleast one lower case
    3. Atleast one upper case
    4. Atleast one digit
    5. Atleast one special character (@,#,$,%,&,*,!,-,=,+,(,),[,],^) 

'''
'''
Notes: 
 1. First we checked for just the length of the password.
 2. Initialized all the requirements as flags and all the special character we want to allow in password.
 3. Then we check and validate every character in string password for upper,lower,digit,special character and set the flags to true for every match.
 4. We then check and validate for all the requirements again using if conditions and return a message with whatever the requirement is missing.
 5. We have a main function which reads input from user and passes it to the passcheck() function which does everything above.
 6. If all the conditions are satisfied the passcheck() function return a message saying the password is valid.

'''


def passcheck(password):
    if len(password) < 12:
        return("Your password needs to be atleast 12 characters.")
    
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_chars = "!@#%^&*()[]-+="

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True
   
    if not has_digit:
        return("NO digit.")
    if not has_lower:
        return("No Lower.")
    if not has_upper:
        return("No Upper.")
    if not has_special:
        return("No Special Character.")
    return("Passsword is Valid.")


def main():
    password=input("Please Enter Your Password: ")
    print(passcheck(password))

if __name__ == "__main__":
    main()