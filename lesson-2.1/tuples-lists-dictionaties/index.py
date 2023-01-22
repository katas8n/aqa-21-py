#  * Tuples
# ! immutable

# group = ("John", "Mike", "Bob")
# group_2 = tuple(["John", "Mike", "Bob"])
# group_3 = "John", "Mike", "Bob"

# print(group_3)
# john = group[0]

# print(john)

# print(type((1, 2, 3)))

# values = (1, 2, 3, 4, 5, 6)

# print(values[2:4])
# values[0] = 13

# arr_of_val = []

# in

# print(13 in values)
# print(1 in values)

# for value in values:
#     if value > 4:
#         arr_of_val.append(value)

# * Lists - are mutable

# print(type([]))
# colors = ["red", "green", "blue"]
# colors_2 = list(("red", "green", "blue"))

# colors.append("black")
# colors_2.append("yellow")

# print(colors)

# print(tuple(colors_2))

# goods = "eggs , milk , cheese"

# goods_list = goods.split(" , ")
# print(goods_list[-1])

# goods_str = ""

# for item in goods_list:
#     if item == goods_list[-1]:
#         goods_str += item
#         continue

#     else:
#         goods_str += item + " , "

# print(item)

# print(goods_str[])

group = ["John", "Mike", "Bob"]


# group[:2] = ["Mike", "John"]


# group[0] = "Jake"


# group.insert(12, "Jake")
# print(group)

# john = group.pop(0)
# john = group.append("Bobby")
# print(john)
# print(group)
# group.extend(["John", "Mike"])

# print(group)

# nums = [2, 3, 23, 10, 13]
# counter = 0

# for num in nums:
#     counter += num

# print(counter)


# group = [["Mike", "John"], [23, 13]]

# print(group[0][0])
# print(group[1][0])

# colors = ["red", "green", "white", "yellow"]
# colors.sort(key=len)


# print(colors)


# practice


students = [
    [
        "John", 2323
    ],
    [
        "Mike", 3232
    ],
    [
        "Mike", 6000
    ],

]

# max payment
# total payment

# Homework
# name of person with min payment

i = 0
prev_person = students[0]
min_payment_person = ""
max_val = 0
total = 0

for student in range(len(students)):
    payment = students[student][1]

    total += payment

    prev_person = students[student]

    if prev_person[1] > students[student][1]:
        max_val = students[student][1]
    else:
        max_val = prev_person[1]

print(max_val)
print(total)

# print(students)
