all_text = open('dict_user_password.txt').read()
lines = all_text.split('\n')

# sometimes there's empty string in the list from 'split', remove that
# "if x" is same as "if x != '' " ,   checking it's non-empty
lines = [ x for x in lines if x ]

passwd = {}
for l in lines:
    user, pwd = l.split()
    passwd[user] = pwd

print(passwd)

