INSTRUCTIONS = '''
  To-Do List Application Instructions

1. Display To-Do List:
   - Enter '1' to display your current to-do list. It will show the tasks and their completion status.

2. Add a Task:
   - Enter '2' to add a new task to your to-do list. You'll be prompted to enter the task's name.

3. Mark a Task as Completed:
   - Enter '3' to mark a task as completed. You'll see the current list of tasks, and you'll be asked to enter the task number you want to mark as completed.

4. Remove a Task:
   - Enter '4' to remove a task from your to-do list. You'll see the current list of tasks and will be prompted to enter the task number you want to remove.

5. Quit:
   - Enter '5' to exit the application.
'''


class TodoList:
  def __init__(self) -> None:
    self.todos = []
    self.size = 0
    self.maxLen = 0

  def __str__(self) -> str:
    return "ID \t TASKS \t COMPLETED" + "\n" + "\n".join([f"{task["ID"]} \t {task["Task"]} \t {task["isCompleted"]}" for task in self.todos])

  def addTask(self, task: str) -> None:
    if not self.todos:
      idx = 1
    else:
      idx = self.todos[-1]["ID"] + 1

    todo = {"ID": idx, "Task": task, "isCompleted": False}
    self.todos.append(todo)
    self.size += 1
    self.maxLen = max(self.maxLen,len(task))

  def markComplete(self, taskID: int) -> None:
    for idx in range(self.size):
      if self.todos[idx]["ID"] == taskID:
        self.todos[idx]["isCompleted"] = True
        break
    else:
      print("Entered id does not exists.")

  def deleteTask(self, taskID: int) -> None:
    for idx in range(self.size):
      if self.todos[idx]["ID"] == taskID:
        self.todos.pop(idx)
        self.size -= 1
        break
    else:
      print("Entered id does not exists.")



if __name__ == "__main__":
  isRunning = True
  print(INSTRUCTIONS)
  todoList = TodoList()

  while isRunning:
    try:
      k = int(input("Enter Operation Number (1-5): "))
      match k:
        case 1:
          print(todoList)
        case 2:
          task = input("Please add task: ")
          todoList.addTask(task)
        case 3:
          print(todoList)
          taskID = int(input("Enter the Task id you want to mark as completed: "))
          todoList.markComplete(taskID)
        case 4:
          print(todoList)
          taskID = int(input("Enter the Task id you want to delete: "))
          todoList.deleteTask(taskID)
        case 5:
          isRunning = False
          print("Thank you for using the application.")
          print("Exiting the Application.")
        case _:
          print("Oops! looks like you have selected an incorrect Operation.")
          print("Please reselect the Operation.")
          print(INSTRUCTIONS)

    except:
      print("Oops! it looks like you have selected an Option that does not exist.")
