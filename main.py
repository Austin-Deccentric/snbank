import itertools
from datetime import datetime
import time

def login():
    condition = True
    while condition != 'end' :
        print("Please enter your login details")
        username = input("Please enter username: ").strip()
        password = input("Please enter password: ").strip()
        with open('staff.txt') as f:
            for line1,line2 in itertools.zip_longest(*[f]*2):
                #print(line1,line2)
                if line1.startswith('Username'):
                    #print(line1.strip().split(' ')[1],line2.strip().split(' ')[1])
                    name = line1.strip().split(' ')[1]
                    passkey = line2.strip().split(' ')[1]
                    if username.lower()==name.lower() and (password ==passkey):
                        print('Welcome to the Portal')
                        condition = 'end'
                        break
            else:
                print("Invalid username or password")
                    #print("Invalid Username or password")
    return username
    
def session_file(user):
    log = open('log.txt','w')
    log.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S')+ " - %s" %user)
    log.write("\n")
    log.close()



print("Welcome to SN Bank".center(100,'*'))
while True:
    user_input = input('''Please select an option:
1 Staff Login
2 Close App
>''')

    if user_input not in ['1','2']:
        print('Enter a valid option')
        continue
    else:
        user_input = int(user_input)
        break

if user_input == 1:
    username = login()
    session_file(username)
    # print("Welcome")
    