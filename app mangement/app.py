def task():
    
    task=[]
    print("~~~~~~~~~welcome to the task management app~~~~~~~~~")

    total_tasks = int(input("Enter the total number of tasks you want to add: "))
    for i in range(1,total_tasks+1):
        task_name = input(f"Enter the name of task {i}= ")
        task.append(task_name)
    
    print(f"Today task are\n{task}")

    while True:
        operation = int(input("Enter 1-add\n2-update\n3-delete\n4-view\n5-exit/stop/ "))
        if operation == 1:
            add = input("Enter the task you want to add: ")
            task.append(add)
            print(f"Task {add} has added successfully")

        elif operation == 2:
            updated_val = input("Enter the task you want to update: ")
            if updated_val in task:
                up = input("Enter the new task name: ")
                index = task.index(updated_val)
                task[index] = up
                print(f"updated task {updated_val} to {up} successfully")
        
        elif operation == 3:
            delete_val = input("Enter the task you want to delete: ")
            if delete_val in task:
                index = task.index(delete_val)
                del task[index]
                print(f"Task {delete_val} has deleted successfully")
               
        elif operation == 4:
            print(f"Today task are\n{task}")
        
        elif operation == 5:
            print("Thank you for using the task management app\nClosing the app....")
            break

        else:
            print("Invalid input please try again")

task()