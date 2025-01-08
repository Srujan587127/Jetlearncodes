student_details = ("Srujan", 15 )
address = ("3105", "Caney Creek Lane", "USA")
for i in address:
    print(i, end = " ")

House_num, apartment_name, country = address
print("")
print("HNO -", House_num)
print("Apartment Name -", apartment_name)
print("Country -", country)

my_tuple = 1, 2, 3, 4, 5
print(type(my_tuple))

nested_tuple = (("apple", "banana"), ("carrot", "potato"))
print(nested_tuple[0])
print(nested_tuple[0][0])

tuple_1 = ("a", "b", "c", "d", "f", "g", "h", "i", "j")
print(tuple_1[6 : 9])
#tuple_1[0] = "z"
tuple_1 = list(tuple_1)
tuple_1[0] = "z"
print(tuple_1)
tuple_1 = tuple(tuple_1)