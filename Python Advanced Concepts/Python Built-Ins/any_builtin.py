# any accepts an iterable and returns if any element in it
# is true or not

print(any([0,0,0,1]))

widget_one = ''
widget_two = ''
widget_three = 'button'
widgets_exist = any([widget_one, widget_two, widget_three])
print (widgets_exist)

# enumerate acts like a counter
my_string = 'abcdefg'
for pos, letter in enumerate(my_string):
    print(pos, letter)

list1 = ['enumerate', 'method', 'being', 'used', 'with', 'a', 'list']
print(list(enumerate(list1)))

# you can also decide what index you intend to start with
my_string = 'abcdefg'
print (list(enumerate(my_string, -2)))

def less_than_ten(x):
    return x < 10

my_list = [1, 2, 3, 10, 11, 12]
for item in filter(less_than_ten, my_list):
    print(item)

def doubler(x):
    return x * 2

my_list = [1, 2, 3, 4, 5]
for item in map(doubler, my_list):
    print(item)

def doubler(x):
    return x * 2

my_list = [1, 2, 3, 4, 5]
print (list(map(doubler, my_list)))

# using list comprehension 
def doubler(x):
    return x * 2
my_list = [1, 2, 3, 4, 5]
print(doubler(x) for x in my_list)

# zip is used to aggregate two lists together
# commonly used when converting two lists into a dictionary

keys = ['x', 'y', 'z']
values = [5, 6, 7]
my_dict = dict(zip(keys, values))
print(my_dict)