import random

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"


def generate(length, chars):
    _psw = ""
    for i in range(length):
        _psw += random.choice(chars)

    return _psw


if __name__ == "__main__":
    psw_len = int(input("Введите длину пароля: "))
    psw_chars = input(
        "Укажите какие символы должны войти в пароль:\n1) Цифры (0-9)\n2) Нижний регистр (a-z)\n3) Верхий регистр (A-Z)\n4) Спец. символы\n\nПример для цифр и нижнего регистра: 12"
    )
