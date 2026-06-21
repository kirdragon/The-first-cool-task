from task_manager import TaskManager

manager = TaskManager()

while True:
    print("\n1. Добавить задачу")
    print("2. Удалить задачу")
    print("3. Показать задачи")
    print("4. Переключить статус")
    print("5. Выход")

    choice = input("Выбор: ")

    if choice == "1":
        text = input("Текст задачи: ")
        manager.add_task(text)

    elif choice == "2":
        index = int(input("Номер задачи: ")) - 1
        manager.delete_task(index)

    elif choice == "3":
        for i, task in enumerate(manager.get_tasks(), 1):
            status = "✔" if task.done else "✖"
            print(f"{i}. {task.text} [{status}]")

    elif choice == "4":
        index = int(input("Номер задачи: ")) - 1
        manager.toggle_task(index)

    elif choice == "5":
        break