from re import findall
from typing import Callable


# scans through the text for all real numbers with a decimal point and returns a generator float value 
def generator_numbers(text_to_scan: str):
    pattern = r"[ ]\d+[,.]\d\d[ ]"
    salaries = findall(pattern, text_to_scan)
    for salary in salaries:
        salary = float(salary.strip())
        yield salary


# adds all the numbers from the generator_numbers() one by one and returns a sum of them
def sum_profit(text_to_scan: str, func: Callable) -> float:
    total_salary = 0
    for salary in func(text_to_scan):
        total_salary += salary
    return total_salary


text = "Employee's total salary consists of several parts: 1000.01 as a base salary with additional incoms of 27.45 and 324.00 USD."
total_income = sum_profit(text, generator_numbers)
print(f"Employee's total salary: {total_income}")
