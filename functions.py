# functions

# pass for empty function
def name():
    pass


# docs
def func_with_doc():
    """
    Retuns 'hello'
    :return:
    """
    return 'hello'


# function that deconstruct an iterable
def expand(iterable):
    return [x for x in iterable]


# function that returns a reference to another function
def gimme_function():
    return expand


# just a string
a = 'dabana'

# service pattern
service = {
    'counter': 0,
    'username': a,
    'expand': expand,
    'gimme_function': gimme_function
}

print service['expand'](service['username'])
service['counter'] += 1
print service['gimme_function']()(service['username'])
service['counter'] += 1
print gimme_function()(service['username'])
service['counter'] += 1


# factory/module pattern
def factory():
    counter = 0
    return {
        'counter': counter,
        'username': a,
        'expand': expand,
        'gimme_function': gimme_function
    }


# create 3 new services using the factory, they are independent (copy)
service1 = factory()
service1['counter'] += 1
print service1['counter']
service2 = factory()
print service2['counter']
service3 = factory()
