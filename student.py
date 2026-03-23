#PARENT CLASS

class Student:
    def __init__(self, name, age, grade):
        self.name=name
        self.age=age
        self.grade=grade

    def display(self):
        print("The details of the student are: ")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")


#CHILD CLASS

class School(Student):
    def __init__(self, name, age, grade, house, section):
        super().__init__(name, age, grade)
        self.house=house
        self.section=section

    def show_details(self):
        print(f"House: {self.house}")
        print(f"Section: {self.section}")


#CREATE AN OBJECT OF THE CLASS

student1=School("Maznah", 13, 8, "Yellow", "F")
student1.display()
student1.show_details()

student2=School("Ayesha", 12, 7, "Blue", "E")
student2.display()
student2.show_details()