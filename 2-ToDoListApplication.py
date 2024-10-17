def displayMenu():
    print("Check tasks")
    print("Add task")
    print("Remove task")
    print("Complete task")
    print("Exit program")
    print()

taskList = []
completedTask = []

def checkTask():
    print("Task list: " + str(taskList))
    print("Completed Tasks: " + str(completedTask))
    print()
    
def addTask():
    newTask = input("Enter new task: ")
    print()
    taskList.append(newTask)
    
def removeTask():
    removeTask = input("Choose Task to Delete: ")
    print()
    taskList.remove(removeTask)
    
def completeTask():
    completed = input("Choose Task to Complete: ")
    print()
    completedTask.append(completed)
    taskList.remove(completed)
    
def toDoList():
    # you need a loop because you want to do more than 1 thing, like addign multiple items
    # every iteration, take in input and display the menu.
    chooseOption = ""
    while chooseOption != "Exit program":
        displayMenu()
        chooseOption = input("What would you like to do: ")
        
        if chooseOption == "Check tasks":
            checkTask()
        elif chooseOption == "Add task":
            addTask()
        elif chooseOption == "Remove task":
            removeTask()
        elif chooseOption == "Complete task":
            completeTask()

toDoList()