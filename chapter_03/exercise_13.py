from operator import itemgetter, attrgetter
from collections import namedtuple

PEOPLE = [('Angela', 'Merkel', 7.85),
('Vladimir', 'Putin', 3.626),
('Jinping', 'Xi', 10.603)]

'''
Reuturn a sorted, formatted string
Each name is in a 10 char field
Each time is in a 5 char field, rounded to two decimals

Bonus: implement with namedtuple
'''
def create_person_named_tuple(args):
    return namedtuple('Person',['first','last','time'])(*args)

def format_sort_records(people_tuple):
    output = []
    for p in people_tuple:
        Person = create_person_named_tuple(p)
        output.append(f'{Person.first:10} {Person.last:10} {Person.time:5.2f}'.format(Person))

    return sorted(output, key=itemgetter(1, 0))


if __name__ == "__main__":
    print('\n'.join(format_sort_records(PEOPLE)))