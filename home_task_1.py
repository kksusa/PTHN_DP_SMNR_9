# Напишите следующие функции:
# - Нахождение корней квадратного уравнения
# - Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# - Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# - Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.



import csv
import json
import random


def deco_func_with_csv(func):
    def wrapper(*args, **kwargs):
        equations = {}
        with open('coefficients.csv', 'r') as csv_file:
            reader = csv.reader(csv_file, dialect='excel')
            equation = {}
            count = 0
            for row in reader:
                if count > 0:
                    equation = {count: {'a': row[0], 'b': row[1], 'c': row[2],
                                        'result': func(int(row[0]), int(row[1]), int(row[2]))}}
                equations.update(equation)
                count += 1
        return equations

    return wrapper


def write_json(func):
    def wrapper(*args, **kwargs):
        result = func()
        with open('result.json', 'w', encoding='utf-8') as json_file:
            json.dump(result, json_file, indent=2, ensure_ascii=False)

    return wrapper


@write_json
@deco_func_with_csv
def quadratic_equation(a=1, b=2, c=3):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return None
    elif discriminant == 0:
        return round(-1 * b / (2 * a), 4)
    else:
        return round((-1 * b + discriminant ** 0.5) / (2 * a), 4), round((-1 * b - discriminant ** 0.5) / (2 * a), 4)


def coefficients_to_csv():
    header = ['a', 'b', 'c']
    coefficients = []
    num_of_rows = random.randint(100, 1000)
    for _ in range(num_of_rows):
        coefficients.append([random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)])

    with open('coefficients.csv', 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(header)
        writer.writerows(coefficients)


if __name__ == '__main__':
    coefficients_to_csv()
    quadratic_equation()
