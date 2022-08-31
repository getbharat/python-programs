import numbers
from unicodedata import decimal


def is_decimal(num):
    try:
        isinstance(num, numbers.Number)
        return True
    except TypeError:
        raise TypeError("Not a number :" + num)


def multiply(num1, num2):
    if is_decimal(num1) & is_decimal(num2):
        return float(num1) * float(num2)


def add(num1, num2):
    if is_decimal(num1) & is_decimal(num2):
        return float(num1) + float(num2)


def subtraction(num1, num2):
    if is_decimal(num1) & is_decimal(num2):
        if num1 > num2:
            return float(num1) - float(num2)
        else:
            return float(num2) - float(num1)


def division(divisor, dividend):
    if is_decimal(divisor) & is_decimal(dividend):
        return float(dividend) / float(divisor)
