from datetime import datetime

tasks = []


class Task:
    def __init__(self, name, deadline):
        self.name = name
        self.deadline = deadline


def add_task():
    name = input("Введите название задачи: ")
    deadline = input("Введите крайний срок выполнения (гггг-мм-дд): ")
    task = Task(name, datetime.strptime(deadline, '%Y-%m-%d'))
    tasks.append(task)
    print("Задача успешно добавлена!")


def display_tasks():
    if tasks:
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task.name} - Крайний срок: {task.deadline}")
    else:
        print("Нет добавленных задач")


def main():
    while True:
        print("\nМеню:")
        print("1. Добавить задачу")
        print("2. Показать задачи")
        print("3. Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            display_tasks()
        elif choice == '3':
            print("Программа завершена.")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
