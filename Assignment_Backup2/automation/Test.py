
d = {"name": "Vasu", "name": "Suja"}
d = {"name": "Vasu", "sal": "Suja"}
print(d)

List = ['G','E','E','K','S','F',
        'O','R','G','E','E','K','S']
Sliced_List = List[3:8]
print("\nSlicing elements in a range 3-8: ")
print(Sliced_List)


def get_key(val):
    for key, value in my_dict.items():
        if val == value:
            return key

    return "key doesn't exist"


# Driver Code

my_dict = {"java": 100, "python": 112, "c": 11}

print(get_key(100))
print(get_key(11))


import os
print(os.name)

print(os.path.abspath('.'))

print(os.listdir('.'))

a=[1,2,1,23,23,2]
print (set(a))

