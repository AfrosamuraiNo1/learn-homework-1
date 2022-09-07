"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

stock = [
{'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
{'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
{'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
]


def sales_shop_midl_one_possion(sales_stock):
    sales_sum = 0
    for sales in sales_stock:
        sales_sum += sales
    sales_avg = sales_sum / len(sales_stock)
    return round(sales_avg)


def sales_shop_all_one_possion(sales_stock):
    sales_sum = 0
    for sales in sales_stock:
        sales_sum += sales
    sales_avg = sales_sum + 1
    return round(sales_avg)



print(f"Средний уровнь продаж {stock[0]['product']} :{sales_shop_midl_one_possion(stock[2]['items_sold'])}.00 руб")
print(f"Общая сумма продаж {stock[0]['product']} :{sales_shop_all_one_possion(stock[2]['items_sold'])}.00 руб")
    
if __name__ == "__main__":
    (sales_shop_midl_one_possion)
