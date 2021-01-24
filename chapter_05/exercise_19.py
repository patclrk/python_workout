'''
Input: filepath ('/etc/passwd')
Ouput: dictionary where keys are usernames and values are UserID from /etc/passwd
'''

def passwd_to_dict(file):
    result = {}
    with open(file) as f:
        for line in f.readlines():
            # skip over comments at top of file on my mac
            if line[0] == '#':
                continue
            user_name = line.split(':')[0]
            user_id = line.split(':')[2]
            if result.get(user_name) == None:
                result[user_name] = user_id
    return result


print(passwd_to_dict('/etc/passwd'))

# book solution

# def passwd_to_dict(filename):
#     users = {}
#     with open(filename) as passwd:
#         for line in passwd:
#             if not line.startswith(('#', '\n')):
#                 user_info = line.split(':')
#                 users[user_info[0]] = int(user_info[2])
#     return users