"""
@file main.py
@brief Пример модуля для пробного использования некоторых сервисов GitHub и системы документирования кода Doxygen
"""


def fibonacci(n):
    """
    @brief Показательная функция для осуществления некоторой логики. Вычисляет число Фибоначчи
    @param Порядковый номер в последовательности Фибоначчи
    @return Возвращает вычисленное число Фибоначчи
    """
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    print(fibonacci(int(input("Enter number: "))))
