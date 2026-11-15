tasks = []

while True:
    print("\n1. Add task")
    print("2. Show tasks")
    print("3. Mark task completed")
    print("4. Change task priority")
    print("5. Remove task")
    print("6. Exit")

    choice = input("Choose: ")

    if choice == "1":
        title = input("Title: ")
        priority = input("Priority: ")
        task = {"title": title, "status": False, "priority": priority}
        tasks.append(task)
        print("Task added.")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            number = 1
            for task in tasks:
                if task["status"]:
                    status_text = "Completed"
                else:
                    status_text = "Pending"
                print(f"{number}. {task['title']} | {task['priority']} | {status_text}")
                number = number + 1


    elif choice == "3":
        title = input("Title: ")
        found = False
        for task in tasks:
            if task["title"] == title:
                task["status"] = True
                found = True
                print("Task marked completed.")
                break
        if not found:
            print("Task not found.")

    elif choice == "4":
        title = input("Title: ")
        new_priority = input("New priority: ")
        found = False
        for task in tasks:
            if task["title"] == title:
                task["priority"] = new_priority
                found = True
                print("Priority updated.")
                break
        if not found:
            print("Task not found.")

    elif choice == "5":
        title = input("Title: ")
        found = False
        for task in tasks:
            if task["title"] == title:
                tasks.remove(task)
                found = True
                print("Task removed.")
                break
        if not found:
            print("Task not found.")

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")