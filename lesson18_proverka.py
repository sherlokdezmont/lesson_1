def grade_students():
    students_data = {}

    students = int(input("Сколько студентов в группе? "))

    for i in range(students):
        name = input(f"Имя студента #{i+1}: ")
        grades = list(map(int, input(f"Введите оценки {name} через пробел: ").split()))
        avg = sum(grades) / len(grades)
        students_data[name] = {
            "grades": grades,
            "average": avg
        }

    # Выводим информацию по каждому студенту
    print("\nРезультаты:")
    for name, data in students_data.items():
        print(f"{name}: оценки {data['grades']}, средний балл: {data['average']:.2f}")

    # Определяем лучшего и худшего студента
    best = max(students_data.items(), key=lambda x: x[1]['average'])
    worst = min(students_data.items(), key=lambda x: x[1]['average'])

    print(f"\nЛучший студент: {best[0]} ({best[1]['average']:.2f})")
    print(f"Худший студент: {worst[0]} ({worst[1]['average']:.2f})")

# Запуск
try:
    grade_students()
except ValueError as e:
    print("Ошибка ввода:", e)





