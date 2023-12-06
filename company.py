"""
В этот раз у нас есть компания, в ней отделы, в отделах люди. У людей есть имя, должность и зарплата.
Ваши задачи такие:
1. Вывести названия всех отделов
2. Вывести имена всех сотрудников компании.
3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.
4. Вывести имена всех сотрудников компании, которые получают больше 100к.
5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями).
6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела
Второй уровень:
7. Вывести названия отделов с указанием минимальной зарплаты в нём.
8. Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём.
9. Вывести среднюю зарплату по всей компании.
10. Вывести названия должностей, которые получают больше 90к без повторений.
11. Посчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин).
12. Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву.
Третий уровень:
Теперь вам пригодится ещё список taxes, в котором хранится информация о налогах на сотрудников из разных департаметов.
Если department None, значит, этот налог применяется ко всем сотрудникам компании.
Иначе он применяется только к сотрудникам департмента, название которого совпадает с тем, что записано по ключу department.
К одному сотруднику может применяться несколько налогов.
13. Вывести список отделов со средним налогом на сотрудников этого отдела.
14. Вывести список всех сотредников с указанием зарплаты "на руки" и зарплаты с учётом налогов.
15. Вывести список отделов, отсортированный по месячной налоговой нагрузки.
16. Вывести всех сотрудников, за которых компания платит больше 100к налогов в год.
17. Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов.
"""

departments = [
    {
        "title": "HR department",
        "employers": [
            {"first_name": "Daniel", "last_name": "Berger", "position": "Junior HR", "salary_rub": 50000},
            {"first_name": "Michelle", "last_name": "Frey", "position": "Middle HR", "salary_rub": 75000},
            {"first_name": "Kevin", "last_name": "Jimenez", "position": "Middle HR", "salary_rub": 70000},
            {"first_name": "Nicole", "last_name": "Riley", "position": "HRD", "salary_rub": 120000},
        ]
    },  
    {
        "title": "IT department",
        "employers": [
            {"first_name": "Christina", "last_name": "Walker", "position": "Python dev", "salary_rub": 80000},
            {"first_name": "Michelle", "last_name": "Gilbert", "position": "JS dev", "salary_rub": 85000},
            {"first_name": "Caitlin", "last_name": "Bradley", "position": "Teamlead", "salary_rub": 950000},
            {"first_name": "Brian", "last_name": "Hartman", "position": "CTO", "salary_rub": 130000},
        ]
    },
]

taxes = [
    {"department": None, "name": "vat", "value_percents": 13},
    {"department": "IT Department", "name": "hiring", "value_percents": 6},
    {"department": "BizDev Department", "name": "sales", "value_percents": 20},
]

print("\n1. Вывести названия всех отделов")
for department in departments:
    print(department['title'])

print("\n2. Вывести имена всех сотрудников компании.")
for department in departments:
    for employer in department['employers']:
        print(f"{employer['first_name']} {employer['last_name']}")

print("\n3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.")
for department in departments:
    for employer in department['employers']:
        print(f"{department['title']}: {employer['first_name']} {employer['last_name']}")

print("\n4. Вывести имена всех сотрудников компании, которые получают больше 100к.")
for department in departments:
    for employer in department['employers']:
        if employer['salary_rub'] > 100000:
            print(f"{employer['first_name']} {employer['last_name']} salary: {employer['salary_rub']}")

print("\n5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями).")
for department in departments:
    for employer in department['employers']:
        if employer['salary_rub'] < 80000:
            print(f"position: {employer['position']} salary: {employer['salary_rub']}")

print("\n6.Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела")
for department in departments:
    sum_salary = sum(employer['salary_rub'] for employer in department['employers'])
    print(f"{department['title']}: {sum_salary}")

print("\n7.Вывести названия отделов с указанием минимальной зарплаты в нём.")
for department in departments:
    min_salary = min(employer['salary_rub'] for employer in department['employers'])
    print(f"{department['title']}: {min_salary}")

print("\n8.Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём.")
for department in departments:
    min_salary = min(employer['salary_rub'] for employer in department['employers'])
    max_salary = max(employer['salary_rub'] for employer in department['employers'])
    employers_count = len(department['employers'])
    avg_salary = 0
    if employers_count != 0:
        avg_salary = sum(employer['salary_rub'] for employer in department['employers'])/len(department['employers'])

    print(f"{department['title']}: min: {min_salary} max: {max_salary} avg: {avg_salary}")

print("\n9.Вывести среднюю зарплату по всей компании.")
sum_salary = 0
employers_count = 0
for department in departments:
    employers_count += len(department['employers'])    
    sum_salary += sum(employer['salary_rub'] for employer in department['employers'])

avg_salary = 0
if employers_count != 0:
    avg_salary = sum_salary/employers_count
print(f"company avg salary: {avg_salary}")

print("\n10. Вывести названия должностей, которые получают больше 90к без повторений.")
unic_positons = []
for department in departments:
    for employer in department['employers']:
        if employer['salary_rub'] > 90000:
            unic_positons.append(employer['position'])
print(unic_positons)

print("\n11. Посчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин).")

girls = ["Michelle", "Nicole", "Christina", "Caitlin"]

for department in departments:    
    sum_girls_salary = sum(employer['salary_rub'] for employer in department['employers'] if employer['first_name'] in girls)
    count_girls = sum(1 for employer in department['employers'] if employer['first_name'] in girls)
    print(f"{sum_girls_salary/count_girls}")


print("\12. Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву.")
unic_names = []
vowels = "aeiouy"
for department in departments:
    for employer in department['employers']:
        if employer['first_name'][-1] in vowels:
            unic_names.append(employer['first_name'])
print(unic_names)
# print("\n")

print("\n13. Вывести список отделов со средним налогом на сотрудников этого отдела.")
for department in departments:
    sum_tax = sum(tax['value_percents'] for tax in taxes if tax['department'] == None or tax['department'].lower() == department['title'].lower())
    sum_salary = sum(employer['salary_rub'] for employer in department['employers'])
    avg_tax = sum_salary * sum_tax / 100 / len(department['employers']) 
    print(f"{department['title']}: {avg_tax}")

print("\n14. Вывести список всех сотрудников с указанием зарплаты 'на руки' и зарплаты с учётом налогов.")
for department in departments:
    sum_tax = sum(tax['value_percents'] for tax in taxes if tax['department'] == None or tax['department'].lower() == department['title'].lower())
    for employer in department['employers']:
        print(f"{employer['first_name']} {employer['last_name']}  на руки: {employer['salary_rub'] * (100 - sum_tax) / 100} с налогами: {employer['salary_rub']}")

print("\n15. Вывести список отделов, отсортированный по месячной налоговой нагрузки.")
department_taxes = {}
for department in departments:
    sum_tax = sum(tax['value_percents'] for tax in taxes if tax['department'] == None or tax['department'].lower() == department['title'].lower())
    sum_salary_tax = sum(employer['salary_rub'] for employer in department['employers']) * sum_tax / 100
    department_taxes[department["title"]] = sum_salary_tax

department_taxes_sorted =  sorted(department_taxes.items(), key=lambda x: x[1]) 

for department_tax in department_taxes_sorted:
    print(f"{department_tax[0]} {department_tax[1]}")

print("\n16. Вывести всех сотрудников, за которых компания платит больше 100к налогов в год.")
for department in departments:
    sum_tax = sum(tax['value_percents'] for tax in taxes if tax['department'] == None or tax['department'].lower() == department['title'].lower())
    for employer in department['employers']:
        if employer['salary_rub'] * 12 * sum_tax / 100 > 100000:
            print(f"{employer['first_name']} {employer['last_name']}")

print("\n17. Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов.")
employers_salary = {}
for department in departments:
    sum_tax = sum(tax['value_percents'] for tax in taxes if tax['department'] == None or tax['department'].lower() == department['title'].lower())
    for employer in department['employers']:
        employers_salary[employer['first_name'] + " " + employer['last_name']] = employer['salary_rub'] * sum_tax / 100
employers_salary_sorted = sorted(employers_salary, key=lambda x: x[1])        
print(employers_salary_sorted[0])
      