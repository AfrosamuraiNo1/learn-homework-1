"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

def main():
    age = input()
    if int(age) <= 6:
        print('Тебе пора в садик')
    elif int(age) <= 17:
            print('Тебе пора в школу')
    elif int(age) <= 24:
            print('Тебе пора в ВУЗ') 
    else:
        print('Тебе пора на работу')
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """

if __name__ == "__main__":
    main()
