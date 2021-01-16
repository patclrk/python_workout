from operator import itemgetter

PEOPLE = [{'first':'Reuven', 'last':'Lerner', 'email':'reuven.lerner@email.com'},
{'first':'Joe', 'last':'Biden', 'email':'president@whitehouse.gov'},
{'first':'Bernie', 'last':'Sanders', 'email':'feelin_the_bern@gmail.com'}]

'''
Return sorted list by last name, first name
'''
def alphabetize_names():
    return sorted(PEOPLE, key=itemgetter('last','first'))

if __name__ == '__main__':
    print(alphabetize_names())