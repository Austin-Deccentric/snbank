import itertools
from datetime import datetime
import time
from random import choices, seed
import string
from os import remove
import sys

def login():
    condition = True
    while condition != 'end' :
        print("Please enter your login details")
        username = input("Please enter username: ").strip()
        password = input("Please enter password: ").strip()
        with open('staff.txt') as f:
            for line1,line2 in itertools.zip_longest(*[f]*2):
                if line1.startswith('Username'):
                    name = line1.strip().split(' ')[1]
                    passkey = line2.strip().split(' ')[1]
                    if username.lower()==name.lower() and (password ==passkey):
                        print('Welcome to the Portal')
                        condition = 'end'
                        break
            else:
                print("Invalid username or password")
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
>''').strip()

    if user_input not in ['1','2']:
        print('Enter a valid option')
        continue
    else:
        user_input = int(user_input)
        

    if user_input == 1:
        username = login()
        session_file(username)
        actions = True
        while actions != '3':
            actions = input('''Please select an Option
1. Create a new account
2. Check account details
3. Logout
> ''').strip()
            if actions == '1':
                acc_name = input("Enter account holder's name: ")
                opening_balance = int(input('Enter Opening Balance: '))     
                acc_type = input("Enter account type: ")
                acc_email = input("Enter Account email")
                seed(datetime.now())
                acc_num = ''.join(choices(string.digits,k = 10))
                with open('customer.txt', 'a') as file:
                    file.write('{}: {}, {}, {}, {}'.format(acc_num,acc_name,opening_balance,acc_type,acc_email))
                    file.write('\n')
                print("Your account number is: ",acc_num)
                continue

            if actions == '2':
                acc_num = input("Enter account number: ").strip()
                with open('customer.txt', 'r') as file:
                    for line in file:
                        if line.startswith(acc_num):
                            acc_details = line.strip().split(' ',1)[1].split(',')
                            print(f'''Account Name: {acc_details[0]}
Balance:{acc_details[1]}
Account type:{acc_details[2]}
Email:{acc_details[3]}
''')
            if actions == '3':
                remove('log.txt')

        continue
    if user_input == 2:
        sys.exit()