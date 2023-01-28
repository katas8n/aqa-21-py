# def run():

#     data_base = []

#     def createQuestion(str):
#         return str + " 'y/Y' if not 'n/N'"

#     def appendToDB(db, obj):
#         db.append(obj)

#     def createUser():
#         return {}

#     def createUserProperties(user):

#         while True:

#             if input(createQuestion("If you wanna continue press")).lower() == "y":
#                 key = input("Enter key name: ")
#                 user[key] = input(f"Enter your {key} : ")

#             else:
#                 appendToDB(data_base, user)
#                 print(data_base)
#                 break

#     print("Hello , user")

#     while True:

#         if input(createQuestion("Do you want to create a user")).lower() == "y":
#             user = createUser()

#             if input(createQuestion("Do you want to add some props")).lower() == "y":
#                 createUserProperties(user)
#         else:
#             print(data_base)
#             break


# run()

# CREATE PROGRAM

# Animals

# 1) Add new animal into animals array []
# 2) Add property to animal
# 3) Append animal into  array []
# 4) Drop (delete) animal from array []
# 5) Edit animals prop

# def constructor(n, s):
#     return {
#         "name": n,
#         "surname": s ,
#     }


# john = constructor("John", "Doe")
# john = constructor("Mike", "Bibby")

# print(john)

# class Dog:
#     legs = 4

#     def __init__(self, name="Jack", age=23):
#         self.name = name
#         self.age = age

#     def desc(self):
#         print(f"{self.name} , {self.age}")


# dog = Dog("John", "Hello")
# dog2 = Dog("John", 13)

# dog.desc()
# dog2.desc()
# dog.show_self()
class Product:

    def __init__(self, label, price):
        self.label = label
        self.price = price


class Human:

    is_alive = True

    def __init__(self, name, age, money, profession):
        self.name = name
        self.age = age
        self.money = money
        self.profession = profession

    def speak(self, sound):
        print(sound)

    def buy(self, goods):
        self.money -= goods
        print(self.money)


class Admin(Human):
    def __init__(self, name, age, money, profession, isAdmin):
        super().__init__(name, age, money, profession)
        self.isAdmin = isAdmin

    def speak(self, sound="Helllooooo , immmmm adminnn"):
        return super().speak(sound)


admin_john = Admin("John", 23, 2323, "admin", True)

admin_john.speak()

# john = Human("John", 23, 2323, "admin")
# snikers = Product("Snikers", 23)

# john.speak("Hello world")

# john.buy(snikers.price)
