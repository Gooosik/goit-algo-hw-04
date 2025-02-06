def total_salary(path):
    try:
        with open(path, 'r') as file:
            lines = [line.strip() for line in file]
    except FileNotFoundError:
        print("Файл не знайдено. Перевірте шлях до файлу.")
        return 0, 0 

    salary_list = []

    for line in lines:
        try:
            name, salary = line.split(",")
            salary_list.append(float(salary))
        except ValueError:
            print(f"Пропущено некоректний рядок: {line}")

    if not salary_list:
        return 0, 0 

    total = sum(salary_list)
    salary_number = len(salary_list)
    average = total / salary_number

    return total, average 

total, avg = total_salary("D:/Documents/Homework GoIT/Two__work/two_work/salary_file.txt")
print(f"Загальна сума: {total}, Середня зарплата: {avg}")
