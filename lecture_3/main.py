import statistics
students = []

def hasName(name): #funcion to indicate is this name in students list or not
    for student in students:
        if name.capitalize() == student["name"]:
            return True
    return False

def maxAvgStudent(f, students): # func to find the best student
    list1 = []
    for student in students:
        try:
            list1.append(f(student))
        except ZeroDivisionError:
            continue
    return max(list1)

def printMenu():
        print("--- Student Grade Analyzer ---")
        print("1. Add a new student")
        print("2. Add grades for a student")
        print("3. Generate a full report")
        print("4. Find the top student")
        print("5. Exit program")

while True:

    printMenu()
    try:
        choice = int(input("Enter your choice: "))
    except:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        name = input("Enter student name: ")

        if hasName(name):
            print("Sorry, but this student already exist.")
        else:
            students.append({"name": name.capitalize(), "grades" : []})

    elif choice == 2:
        name = input("Enter student name: ").capitalize()
        for student in students:
            if name in student["name"]:
                while True:    
                    grade = input(f"Enter a grade (or 'done' to finish): ")
                    if grade.lower()=='done':
                        break

                    else: 
                        try: 
                            intGrade = int(grade)
                            if 0 <= intGrade <= 100:
                                student["grades"].append(intGrade)
                            else:
                                print("Grade must be between 0 and 100")
                        except ValueError:
                            print("Invalid input. Please enter a number.")
                        
                    
            elif students[len(students)-1]["name"] == student["name"]: #to avoid print multiple times
                print("This student doesn't exist.") 

    elif choice == 3:
        if any(student.get("grades") for student in students):
            averageGrades = []
            print("--- Student Report ---")
            for student in students:
                try:
                    averageGrades.append(statistics.fmean(student["grades"])) 
                    print(f"{student["name"]}'s average grade is {statistics.fmean(student["grades"])}.")
                except:
                    print(f"{student["name"]}'s average grade is N/A.")
                        
            print("-------------------------")
            print(f"Max Average: {max(averageGrades)}")
            print(f"Min Average: {min(averageGrades)}")
            print(f"Overall Average: {statistics.fmean(averageGrades)}")
        else:
            print("There are no students or grades")

    elif choice == 4:
        if any(student.get("grades") for student in students):
            max_grade = maxAvgStudent(lambda student: sum(student["grades"])/len(student["grades"]), students)
            max_name = ""
            for student in students:
                try:
                    if statistics.fmean(student["grades"]) == max_grade:
                        max_name = student["name"]
                except:
                    continue
            print(f"The student with the highest average is {max_name} with a grade of {max_grade}")
        else:
            print("There are no students or grades")


    elif choice == 5:
        print("Exiting program.")
        break

    else:
        print("Enter a number (1-5)")
    