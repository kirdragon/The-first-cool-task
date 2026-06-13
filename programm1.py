import json
tasks=[]
try:
    with open("tasks.json","r",encoding="utf-8") as f:
        tasks=json.load(f)
except(FileNotFoundError, json.JSONDecodeError):
    with open("tasks.json",'w',encoding="utf-8") as f:
        json.dump(tasks,f, ensure_ascii=False, indent=4)
    print("\nСоздан новый файл!")
def add_cmd():
    with open("tasks.json","w",encoding="utf-8") as f:
        tasks.append({'text': input('Впишите задачу: '),
                      'done': False
        })
        json.dump(tasks,f, ensure_ascii=False, indent=4)
        print("\nЗадача успешно записана! \n")
def delete_cmd():
    if tasks:
        try:
            num=int(input("\nУдалить задачу под номером: "))
            tasks.pop(num-1)
            with open("tasks.json","w",encoding="utf-8") as f:
                json.dump(tasks,f, ensure_ascii=False, indent=4)
            print("\nВыбранная задача удалена!")
        except IndexError:
            print("\nЗадачи с таким номером не существует!")
        except ValueError:
            print("Введите число!")
    else:
        print("\nСписок уже пуст")
def show_cmd():
    if not tasks:
        print("\nЗадач пока нет")
    else:
        print("\nВсе записанные ранее задачи: \n")
        for i, task in enumerate(tasks,start=1):
            if task['done']:
                status="Потужно"
            else:
                status="Плохо"
            print(f"{i}. {task['text']} -{status}")
def change_cmd():
    show_cmd()
    try:
        num=int(input("\nВведите номер задачи, статус которой хотите поменять: "))
        if tasks[num-1]["done"]:
            st="выполнена"
        else:
            st="не выполнена"
        try:
            choice=int(input(f"\nЗадача {num} сейчас {st}. Чтобы поменять ее статус нажмите 1, а чтобы вернуться в главное меню- 2: "))
            if choice==1:
                tasks[num-1]["done"]= not tasks[num-1]["done"]
                print("\nСтатус успешно изменен!")
            elif choice==2:
                print("\nВозвращение обратно...")
                return
            else:
                print("\nВведите 1 или 2")
        except ValueError:
            print("\nВведите 1 или 2")
        with open ("tasks.json","w",encoding="utf-8") as f:
            json.dump(tasks,f, ensure_ascii=False, indent=4)
    except IndexError:
        print("\nЗадачи с таким номером не существует!")
    except ValueError:
        print("\nВведите число!")
print("\nДобро пожаловать в этот прекраснейший блокнот\n")
print("=====================================")
while True:
    print("\n1. Вписать новую задачу \n")
    print("2. Удалить задачу n\n")
    print("3. Показать список записанных задач\n")
    print("4. Изменить статус задачи n\n")
    print("5. Выход из программы")
    print("\n=====================================\n")
    try:
        ch=int(input("Выберите действие: "))
        if ch==1:
            add_cmd()
        elif ch==2:
            delete_cmd()
        elif ch==3:
            show_cmd()
        elif ch==4:
            change_cmd()
        elif ch==5:
            print("Выход из программы...")
            break
        else:
            print("\nТы Меленцов64, выбери правильную цифру")
        print("\n=====================================")
    except ValueError:
        print("Введите число!")