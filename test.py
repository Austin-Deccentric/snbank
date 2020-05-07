# # user = "BuchiCorp"
# # pascode='234@pagang'
# with open('staff.txt') as f:
#         for line in f:
#                 #print(line)
#                 username, details= line.strip().split(':',maxsplit=1)
#                 print(username)
#                 print(details.strip())

# from random import seed, choices
# from datetime import datetime
# import string

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