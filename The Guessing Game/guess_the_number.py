import random

MIN_VALUE = 1
MAX_VALUE = 100
GUESS_VALUE = random.randint(1, 100)


def is_valid(value):
    if value.isdigit():
        value = int(value)
        if MIN_VALUE <= int(value) <= MAX_VALUE:
            return True

    return False


def quess():
    tries = 0
    while True:
        user_input = input("Введите целое число от 1 до 100: ").strip()

        if not is_valid(user_input):
            print("А может быть все-таки введем целое число от 1 до 100?")
        else:
            user_input = int(user_input)

            if user_input == GUESS_VALUE:
                tries += 1
                print(f"(!) Вы угадали, поздравляем!\nКоличество попыток: {tries}")
                break
            elif user_input > GUESS_VALUE:
                tries += 1
                print(" МНОГО! Попробуйте еще раз.", GUESS_VALUE)
            else:
                tries += 1
                print(" МАЛО! Попробуйте еще раз.", GUESS_VALUE)


if __name__ == "__main__":
    quess()
