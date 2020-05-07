import itertools
words1 = 'Username'
word2 = 'Password'
with open('staff.txt') as f:
        for line1,line2 in itertools.zip_longest(*[f]*2):
            #print(line1,line2)
            if line1.startswith('Username'):
                #print(line1.strip().split(' ')[1],line2.strip().split(' ')[1])
                username = line1.strip().split(' ')[1]
                password = line2.strip().split(' ')[1]
                if username.lower()=="BuchiCorp".lower() and (password =='234@paga.ng'):
                    print('welcome')
                #print(password)
#             for word in words:
#                 if word in line1 or line2: 
#                     print(line1, line2)

# # words= ['Username', 'Password']
# with open('staff.txt') as f:
#     for line in open('staff.txt'):
#         line1 = 
#         for word in words:
#             if word in line: 
#                 print(line)