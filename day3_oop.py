class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("My name is", self.name, "and I am", self.age, "years old")

    def is_adult(self):
        if self.age >= 18:
            print(self.name, "is an adult")
        else:
            print(self.name, "is not an adult")


# Create objects
s1 = Student("Anisa", 22)
s2 = Student("Raghu", 17)

# Call methods
s1.introduce()
s1.is_adult()

s2.introduce()
s2.is_adult()