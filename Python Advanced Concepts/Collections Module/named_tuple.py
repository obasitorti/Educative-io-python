# namedtuple class is used like a struct
# a struct is a complex data type that groups a list of variables under one name

from collections import namedtuple

Parts = namedtuple("Parts", "id_num desc cost amount")
autoparts = Parts(id_num="1234", desc="Ford Engine", cost=1200.00, amount=10)
print(autoparts.id_num)


# Converting Python dictionary to an object
from collections import namedtuple

Parts = {'id_num':'1234', 'desc':'Ford Engine',
     'cost':1200.00, 'amount':10}
parts = namedtuple('Parts', Parts.keys())(**Parts)
print (parts)
