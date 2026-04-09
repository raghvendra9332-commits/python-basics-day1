class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_average(self):
        return sum(self.marks) / len(self.marks)

    def get_grade(self):
        avg = self.calculate_average()

        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 50:
            return "C"
        else:
            return "Fail"

    def display(self):
        avg = self.calculate_average()
        grade = self.get_grade()

        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Average:", avg)
        print("Grade:", grade)
        print("---------------------")


# Create multiple students
students = []
n=int(input("Enter the Number of Studnets you want to have a data of:"))
for i in range(n):
    name = input("Enter student name: ")
    marks = []

    for j in range(3):
        m = int(input(f"Enter marks {j+1}: "))
        marks.append(m)

    student = Student(name, marks)
    students.append(student)


# Display results
for s in students:
    s.display()