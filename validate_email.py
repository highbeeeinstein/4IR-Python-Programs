import re

pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b')

def validate_email(email):
        return re.fullmatch(pattern, email)
        
while True:
        user_input = input('Enter your email address ')
        if validate_email(user_input): 
            print('Your email is valid')
            break
        else:
            print('Your email is invalid')
        