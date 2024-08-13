# Задача "Некорректность":
#
# Создайте 3 класса (2 из которых будут исключениями):
# Класс Car должен обладать следующими свойствами:
# Атрибут объекта model - название автомобиля (строка).
# Атрибут объекта __vin - vin номер автомобиля (целое число). Уровень доступа private.
# Метод __is_valid_vin(vin_number) - принимает vin_number и проверяет его на корректность.
# Возвращает True, если корректный, в других случаях выбрасывает исключение. Уровень доступа private.
# Атрибут __numbers - номера автомобиля (строка).
# Метод __is_valid_numbers(numbers) - принимает numbers и проверяет его на корректность.
# Возвращает True, если корректный, в других случаях выбрасывает исключение. Уровень доступа private.
# Классы исключений IncorrectVinNumber и IncorrectCarNumbers, объекты которые обладают атрибутом
# message - сообщение, которое будет выводиться при выбрасывании исключения.
#
# Работа методов __is_valid_vin и __is_valid_numbers:
# __is_valid_vin
# Выбрасывает исключение IncorrectVinNumber с сообщением 'Некорректный тип vin номер', если передано не
# # целое число. (тип данных можно проверить функцией isinstance).
# Выбрасывает исключение IncorrectVinNumber с сообщением 'Неверный диапазон для vin номера',
# если переданное число находится не в диапазоне от 1000000 до 9999999 включительно.
# Возвращает True, если исключения не были выброшены.
# __is_valid_numbers
# Выбрасывает исключение IncorrectCarNumbers с сообщением 'Некорректный тип данных для номеров',
# если передана не строка. (тип данных можно проверить функцией isinstance).
# Выбрасывает исключение IncorrectCarNumbers с сообщением 'Неверная длина номера', переданная строка
# должна состоять ровно из 6 символов.
# Возвращает True, если исключения не были выброшены.
#
# ВАЖНО!
# Методы __is_valid_vin и __is_valid_numbers должны вызываться и при создании объекта (в __init__ при
# объявлении атрибутов __vin и __numbers).

class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        self.__vin = vin
        self.__numbers = numbers
        # при создании объекта вызываются методы (@staticmethod)
        self.__is_valid_vin(vin)
        self.__is_valid_numbers(numbers)

    @staticmethod
    def __is_valid_vin(vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        elif vin_number not in range(1000000, 9999999):
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        else:
            return True

    @staticmethod
    def __is_valid_numbers(numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        elif len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        else:
            return True

# создаем собственный класс ошибки при наследовании от Exception
class IncorrectVinNumber(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

# создаем собственный класс ошибки при наследовании от Exception
class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


if __name__ == '__main__':
    try:
        first = Car('Model1', 1000000, 'f123dj')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{first.model} успешно создан')

    try:
        second = Car('Model2', 300, 'т001тр')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{second.model} успешно создан')

    # try:
    #     first = Car('Model1', 1000000, 'f123dj')
    # except IncorrectVinNumber as exc:
    #     print(exc.message)
    # except IncorrectCarNumbers as exc:
    #     print(exc.message)
    # else:
    #     print(f'{first.model} успешно создан')
    #
    # try:                                        Почему то здесь Модель1 и Модель2 повторяются?
    #     second = Car('Model2', 300, 'т001тр')
    # except IncorrectVinNumber as exc:
    #     print(exc.message)
    # except IncorrectCarNumbers as exc:
    #     print(exc.message)
    # else:
    #     print(f'{second.model} успешно создан')

    try:
        third = Car('Model3', 2020202, 'нет номера')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{third.model} успешно создан')
