import copy

def egg(some_parameter):
    some_parameter.append('hello')

spam = [1,2,3]
print(spam)

egg(copy.copy(spam))
print(spam)