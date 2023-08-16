# extend() can be used to merge lists
# insert(index, newElement)
# LIST COMPREHENSION : [EXPRESSION forLoop ifCONDITION]
# Use .get() to get the value from a dictionary
# phone_book = {"Batman": 468426,
#               "Cersei": 237734,
#               "Ghostbusters": 44678}
# print(phone_book)

# phone_book["Godzilla"] = 46394  # New entry
# print(phone_book)

# phone_book["Godzilla"] = 9000  # Updating entry
# print(phone_book)

# # For dictionary comprehension
# houses = {1: "Gryffindor", 2: "Slytherin", 3: "Hufflepuff", 4: "Ravenclaw"}
# new_houses = {n**2: house + "!" for (n, house) in houses.items()}
# print(houses)
# print(new_houses)

# star_wars_dict = {1: "Anakin", 2: "Darth Vader", 3: 1000}
# print(star_wars_dict)

# star_wars_list = list(star_wars_dict.items())
# print(star_wars_list)

# my_list = [34, 82.6, "Darth Vader", 17, "Hannibal"]
# # my_tuple = ()
# # for i in my_list:
# #     my_tuple.append(i)
    

# my_tuple = (my_list[0], my_list[len(my_list) - 1], len(my_list))
# print(my_tuple)

number_list = [21, 76, 31, 9, -1, 66]
def count_low_high(num_list):
    high = 0
    low = 0
    if len(num_list) == 0:
        return None
    if len(num_list) == 0:
        return None
    else:
        for n in num_list:
            if n % 3 == 0 or n > 50:
                high+=1
            else:
                low+=1
    
    return([low, high])
