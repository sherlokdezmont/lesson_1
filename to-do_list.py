todo_list = []

def show_tasks():
    if not todo_list:
        print("Список дел пуст.")
    else:
        print("Список дел:")
        for idx, task in enumerate(todo_list, 1):
            print(f"{idx}. {task}")

def add_task():
    task = input("Введите задачу: ")
    todo_list.append(task)
    print("Задача добавлена.")

def delete_task():
    show_tasks()
    if not todo_list:
        return
    try:
        num = int(input("Введите номер задачи для удаления: "))
        if 1 <= num <= len(todo_list):
            removed = todo_list.pop(num - 1)
            print(f"Задача '{removed}' удалена.")
        else:
            print("Некорректный номер задачи.")
    except ValueError:
        print("Пожалуйста, введите число.")

def main():
    while True:
        print("\nМеню:")
        print("1. Показать список дел")
        print("2. Добавить задачу")
        print("3. Удалить задачу")
        print("4. Выйти")
        choice = input("Выберите пункт меню: ")
        if choice == '1':
            show_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()