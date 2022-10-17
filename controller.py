from imp import impo
from exp import expp
from logg import log_info

def find():
    second_name = input('1. Введите фамилию человека: ')
    return second_name

def inpp():
    str_person = input('4. Введите данные нового сотрудника: ')
    return str_person

def start():
    print("\n" + "=" * 20)
    print("Выберите необходимое действие")
    print("1. Найти сотрудника")
    print("2. Сделать выборку сотрудников по должности")
    print("3. Сделать выборку сотрудников по зарплате")
    print("4. Добавить сотрудника")
    print("5. Удалить сотрудника")
    print("6. Обновить данные сотрудника")
    print("7. Экспортировать данные в формате json")
    print("8. Экспортировать данные в формате cmv")
    print("9. Закончить работу")
    menu_number = int(input("Введите номер необходимого действия: "))
    while (menu_number  != 9):
        if menu_number  == 1:
            info = find()
            expp(info)
            log_info(info)
        elif menu_number  == 4:
            info = inpp()
            impo(info)
            log_info(info)
        print("\n" + "=" * 20)
        print("Выберите необходимое действие")
        print("1. Найти сотрудника")
        print("2. Сделать выборку сотрудников по должности")
        print("3. Сделать выборку сотрудников по зарплате")
        print("4. Добавить сотрудника")
        print("5. Удалить сотрудника")
        print("6. Обновить данные сотрудника")
        print("7. Экспортировать данные в формате json")
        print("8. Экспортировать данные в формате cmv")
        print("9. Закончить работу")
        menu_number = int(input("Введите номер необходимого действия: "))

# def run_work():
#     employees  = read_csv()
#     employee = {}
#     while True:
#         choice = show_menu()
#         if choice == 1:             # find employee
#             employee = find_employee(employees)
#             if employee is None:
#                 no_employee_error()
#             else:
#                 show_employee_info(employee)
# #CSV
# def write_csv(employees: list):
#     with open(Path.cwd() / 'database.csv', 'w', encoding='utf-8') as fout:
#         csv_writer = csv.writer(fout)
#         for employee in employees:
#             csv_writer.writerow(employee.values())
# # з/п
# def find_employees_by_salary_range(employees: list) -> list:
#     result = []
#     lo, hi = get_salary_range()
#     for employee in employees:
#         if lo <= employee["salary"] <= hi:
#             result.append(employee)
#     return result

# fields = ["id", "last_name", "first_name", "position", "phone_number", "salary"]