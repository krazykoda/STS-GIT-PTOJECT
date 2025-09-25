class Person:

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


    # def __str__(self):
    #     return f"{self.name}::{self.gender}"

chloe = Person("chloe", "female")

print(chloe)


class Person2:
    name = "Chloe"
    gender = "female"

    def __init__(self, name):
        print("init is running")
        self.name = name

  


chloe2 = Person2("chloe")




