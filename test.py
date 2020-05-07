# user = "BuchiCorp"
# pascode='234@pagang'
with open('staff.txt') as f:
        for line in f:
                #print(line)
                username, details= line.strip().split(':',maxsplit=1)
                print(username)
                print(details.strip())