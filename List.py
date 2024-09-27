class ToDoList:
    def __init__(self):
        self.tasks = []
    def addTask(self, description):
        self.tasks.append({'description': description, 'status': 'Не начата'})
    def removeTask(self, task_id):
        if task_id >= 0 and task_id < len(self.tasks):
            del self.tasks[task_id]
        else:
            print('Задача не найдена')
    def updateStatus(self, task_id, status):
        if task_id >= 0 and task_id < len(self.tasks):
            if status in ['Не начата', 'В процессе', 'Завершена']:
                self.tasks[task_id]['status'] = status
            else:
                print("Некорректный статус")
        else:
            print('Задача не найдена')

    def viewTasks(self):
        for i in range(len(self.tasks)):
            print(f"id: {i}, Описание: {self.tasks[i]['description']}, Статус: {self.tasks[i]['status']}")
