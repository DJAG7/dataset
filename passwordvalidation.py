import re
def check_password_strength(self):
    if (int(len(user_input))>=8):
        if any(char.isupper() for char in user_input) or any(char.islower() for char in user_input):
            if any(char.isdigit() for char in user_input()):
                special_characters = r'[!@#$%^&*(),.?":{}|<>]'
                if re.search(special_characters, user_input):
                    print("Your password is correct")
                    return passwordvalidate
                else:
                    print("Your password does not have the required amount of special characters")
            else:
                print("Your password does not meet the required amount of Digits/Numerical Characters")
        else: 
            print(" Your password does not meet the required amount of Capital and Small Letters")
    else:
        print("Your password is less than 8 Characters in Length")
        
password="not generated"
passwordvalidate="not validated"
while password == "not generated":
    user_input=input("Please enter your password. It must be 8 characters in length")
    passwordvalidate=check_password_strength(user_input)
    user_input2=input("Please re enter your password.")
if (password!="not generated"):
    if(int(len(password))>=12):
        print("Password is strong")
    if(int(len(password))>=12):
        print("Password is medium")




    
