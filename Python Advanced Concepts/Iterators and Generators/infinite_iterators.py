from itertools import count
from itertools import islice
from itertools import cycle
from itertools import repeat
# for i in count():
#     if i > 20:
#         break
#     else:
#         print(i)
# for i in islice(count(10), 5):
#     print(i)
# counter = 0
# for item in cycle('XYZ'):
#     if counter > 7:
#         break
#     print(item)
#     counter += 1
# polys = ['triangle', 'square', 'pentagon', 'rectangle']
# iterator = cycle(polys)

# print (next(iterator))
# print (next(iterator))
# print (next(iterator))
# print (next(iterator))
# print (next(iterator))

# print (next(iterator))
repeat(5, 5)
repeat(5, 5)

iterator = repeat(5, 5)
print (next(iterator))
print (next(iterator))
print (next(iterator))
print (next(iterator))
print (next(iterator))
print (next(iterator))  #<module>
#     print (next(iterator))
#            ^^^^^^^^^^^^^^
# StopIteration