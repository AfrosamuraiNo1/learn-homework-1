"""

Домашнее задание №1

Исключения: приведение типов

* Перепишите функцию discounted(price, discount, max_discount=20)
  из урока про функции так, чтобы она перехватывала исключения,
  когда переданы некорректные аргументы.
* Первые два нужно приводить к вещественному числу при помощи float(),
  а третий - к целому при помощи int() и перехватывать исключения
  ValueError и TypeError, если приведение типов не сработало.
    
"""

stock = [
{'name': 'iPhone 12 Plus', 'stock': 24, 'price': 65432.1,'discount': 25},
{'name': 'Samsung Galaxy S21', 'stock': 8, 'price': 50000.0, 'discount': 10},
{'name': 'Xiaomi Mi11', 'stock': 42, 'price': 38000.5,'discount': 10}
]
        

def discounted(price, discount, max_discount=20, phone_name=''):
    try:
        price = abs(int(float(price)))
        discount = abs(int(float(discount)))
        max_discount = abs(int(max_discount))
        if max_discount >= 100:
            raise ValueError('Слишком большая максимальная скидка')
        if int(discount) >= int(max_discount):
            return price
        elif 'iphone' in phone_name.lower() or not phone_name:
            return price

    except ValueError:
        print('Введите число!')
    else:
        return price - (price * discount / 100)
        

for phone in stock:
    phone['price_final'] = discounted(phone['price'], phone['discount'], phone_name=phone['name'])

if __name__ == "__main__":
    print(discounted(100, 2))
    print(discounted(100, "3"))
    print(discounted("100", "4.5"))
    print(discounted("five", 5))
    print(discounted("сто", "десять"))
    print(discounted(100.0, 5, "10"))