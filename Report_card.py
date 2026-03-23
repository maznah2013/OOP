class Student:
    def __init__(self):
        self.name=""
        self.grade=""
        self.section=""
    
class Result(Student):
    def __init__(self):
        super().__init__()
        self.m1=0
        self.m2=0
        self.m3=0
        self.total=0
        self.avg=0

    def input_details(self):
        self.name=input("Enter your name: ")
        self.grade=int(input("Enter your grade: "))
        self.section=input("Enter your section: ")
        self.m1=int(input("Enter your marks in Maths: "))
        self.m2=int(input("Enter your marks in Science: "))
        self.m3=int(input("Enter your marks in English: "))

    def cal(self):
        self.total= self.m1 + self.m2 + self.m3
        self.avg= self.total//3

    def show_details(self):
        print("The details of the student are: ")
        print(f"Name: {self.name}")
        print(f"Grade: {self.grade}")
        print(f"Section: {self.section}")
        print(f"Average: {self.avg}")
        if self.avg>=90:
            print("You got A+")
        elif self.avg>=80:
            print("You got A")
        elif self.avg>=70:
            print("You got B")
        elif self.avg>=60:
            print("You got C")
        elif self.avg>=50:
            print("You got D")
        elif self.avg>=40:
            print("You got E")
        else:
            print("You have failed")

result1=Result()
result1.input_details()
result1.cal()
result1.show_details()