from List import ToDoList

list = ToDoList()

print("-"*100)

list.addTask("Сходить в магазин за продуктами")
list.updateStatus(0, "В процессе")

list.addTask("Решить задачу по Питону")
list.updateStatus(1,"Завершена")

list.addTask("Решить задачу по React")
list.addTask("Решить задачу по Java")
list.removeTask(3)

list.viewTasks()

print("-"*100)