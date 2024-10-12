class ToDoList:
    def __init__(self):
        self.tasks = {}
        self.task_id_count = 0
    def addTask(self, description):
        self.tasks[self.task_id_count] = {'description': description, 'status': 'Не начата'}
        self.task_id_count += 1
    def removeTask(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]
        else:
            print('Задача не найдена')
    def updateStatus(self, task_id, status):
        if task_id in self.tasks:
            if status in ['Не начата', 'В процессе', 'Завершена']:
                self.tasks[task_id]['status'] = status
            else:
                print("Некорректный статус")
        else:
            print('Задача не найдена')

    def viewTasks(self):
        for task_id, task in self.tasks.items():
            print(f"id: {task_id}, Описание: {task['description']}, Статус: {task['status']}")
