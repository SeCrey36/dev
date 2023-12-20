import ft
import back as bk


def append_salaried(name, salary):
    employee = bk.SalariedEmployee(name, salary)
    company.hire(employee)

def append_hourly(name, hourly_rate, hours):
    employee = bk.HourlyEmployee(name, hourly_rate, hours)
    company.hire(employee)

def append_manager(name, salary, bonus):
    employee = bk.Manager(name, salary, bonus)
    company.hire(employee)

def append_executive(name, salary, bonus, stock_options):
    employee = bk.Executive(name, salary, bonus, stock_options)
    company.hire(employee)


def take_workers_list():
    employee_list = company.show_employees()
    return[str(i + 1) + ' ' + employee_list[i]
           for i in range(len(employee_list))]

def take_worker_info(ind):
    info_arr = company.info(ind - 1)
    return [info_arr[i] for i in range(len(info_arr))]

def del_worker(ind):
    company.fire(ind - 1)

def main():
    ft.mainwin([])  # Передаем пустой список работников потому что он с джcоном мог бы быть изначально не пуст


company = bk.Company() # если в мейне написать другие функции не видят даже через глобал

if __name__ == '__main__':
    main()
