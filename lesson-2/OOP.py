# class blueprint

class Person:

    surname = "Doe"

    def __init__(self, n, a):
        self.self_skills = ("HTML", "PHP", "SQL")
        self.name = n
        self.age = a

    def describe(self):
        return f"NAME : [{self.name}] , AGE : [{self.age}]"

    def skills(self):
        print(self.self_skills)
        for skill in range(len(self.self_skills)):
            print(self.self_skills[skill])


def calc_sum_of_numbers(elem):
    if elem == []:
        return 0
    else:
        sum = calc_sum_of_numbers(elem[1:])

        sum = sum + elem[0]
        return sum


result = calc_sum_of_numbers([23, 3, 5, 10, 13, 26])
print(result)


john = Person("John", 23)
mike = Person("Mike", 32)

johnsData = john.describe()
mikesData = mike.describe()

john.skills()

# print(johnsData)
# print(mikesData)

# print(john.name)
# print(mike.name)

# print(john.surname)
# print(mike.surname)

# print(john == mike)
