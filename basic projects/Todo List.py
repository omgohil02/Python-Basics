tasks = []

print("Welcome to your Simple To-Do List Manager!")

while True:
    print("\n---Menu---:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
    
    choice = input("Enter your choice: ").strip()
    
    if choice == "1":
        task_info = input("Enter the task description: ").strip()
        if task_info:
            tasks.append(task_info)
            print(f"Task '{task_info}' added successfully!")
        else:
            print("Task description cannot be empty.")
            
    elif choice == "2":
        if not tasks:
            print("\nYour To-Do list is empty. Time to add some tasks!")
        else:
            print("\nYour To-Do List")
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task}")    
                
    elif choice == "3":
        if not tasks:
            print("\nYour To-Do list is empty. Nothing to remove!")
        else:
            print("\nYour To-Do List")
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task}")
                
            try:
                task_num = int(input("Enter the number of the task you want to remove: "))
                if 1 <= task_num <= len(tasks):
                    removed_task = tasks.pop(task_num - 1)
                    print(f"Task '{removed_task}' removed successfully!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
                
    elif choice == "4":
        print("Exiting To-Do List Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please choose an option from 1 to 4.")