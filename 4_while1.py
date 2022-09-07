"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def hello_user():  
  say = input()
  while say != 'Хорошо':
    say = input('Как дела?')

    if say == 'Хорошо':
      print('Я рад за тебя, пока!')

    
if __name__ == "__main__":
    hello_user()
