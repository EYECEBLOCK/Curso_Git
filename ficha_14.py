import matplotlib.pyplot as plt

grades = []
students = []

def addStudent():
    while True:
        student_name = input("\nEnter the student's name: ")
        
        try:
            student_grade = float(input("\nEnter the student's grade (from 0 to 20): "))
            
            if student_grade < 0 or student_grade > 20:
                raise ValueError("\nGrade must be between 0 and 20...")
            
            students.append(student_name)
            grades.append(student_grade)
            
            break
        
        except ValueError as e:
            print("\nInvalid input:", e)
    
    print("\nStudent and grade added successfully.")

def checkGraph():
    plt.bar(students, grades)
    plt.xlabel('Students')
    plt.ylabel('Grades')
    plt.title('Student Grades')
    plt.ylim(0, 20)
    plt.show()

def menu():
    while True:
        print("\nWelcome to the school board's grades graph!\nTo introduce a grade, please select 1.\nTo check the graph, please select 2.\nTo close the program, press 0.")
        menuChoice = input("\nPlease select an option: ")
        
        if menuChoice in {"0", "1", "2"}:
            return menuChoice
        else:
            print("Invalid choice.")

operation = {
    "1": addStudent,
    "2": checkGraph,
}

while True:
    choice = menu()
       
    if choice == '0':
        print("Goodbye...")
        break
    else:
        operation[choice]()