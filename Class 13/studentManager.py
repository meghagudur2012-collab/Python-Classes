students = []

while True:
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Modify Student Name")
    print("4. Display All Students")
    print("5. Exit")
    
    choice = int(input("Enter a number to select your choice: "))

    if choice == "1":
        name = input("Enter student name: ")
        students.append(name)

    elif choice == "2":
        name = input("Enter student name to remove: ")
        students.remove(name)

    elif choice == "3":
        index = int(input("Enter student index: "))
        new_name = input("Enter new name: ")
        students[index] = new_name

    elif choice == "4":
        print(students)

    elif choice == "5":
        print("Will Exit. Please wait.")

    else:
        print("Invalid choice! Please choose numbers 1 through 5.")