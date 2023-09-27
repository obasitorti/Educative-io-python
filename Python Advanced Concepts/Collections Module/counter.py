# Counter supports convenient and fast tallies

from collections import Counter

# print(Counter("superfluous"))

counter = Counter("superfluous")
counter_2 = Counter("super")

print(counter.subtract(counter_2))
print(counter)
# print(counter["u"])
# print(list(counter.elements()))
# print(counter.most_common(2))