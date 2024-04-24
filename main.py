#3адача: Создай класс Task, который позволяет управлять задачами (делами). У задачи должны быть атрибуты: описание задачи,
#срок выполнения и статус (выполнено/не выполнено). Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка
# текущих (не выполненных) задач.

class Task:
    def __init__(self, description, due_date, status=False):

        self.description = description
        self.due_date = due_date
        self.status = status

    def mark_as_done(self):
        self.status = True

    def __repr__(self):
        return f"{self.description} (Срок: {self.due_date}, {'Выполнено' if self.status else 'Не выполнено'})"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):
        self.tasks.append(Task(description, due_date))

    def mark_task_as_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_as_done()
        else:
            print("Задача с таким индексом не найдена.")

    def show_current_tasks(self):
        current_tasks = [task for task in self.tasks if not task.status]
        for task in current_tasks:
            print(task)

task_manager = TaskManager()
task_manager.add_task("Купить еду коту", "24-04-2024")
task_manager.add_task("Записаться к врачу", "25-04-2024")
task_manager.add_task("Убраться дома", "24-04-2024")

print("Текущие задачи:")
task_manager.show_current_tasks()

task_manager.mark_task_as_done(2)
print("\nТекущие задачи после выполнения одной из них:")
task_manager.show_current_tasks()