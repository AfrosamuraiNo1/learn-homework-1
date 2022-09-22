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
    sales_all = sales_sum / len(sales_stock)
    return round(sales_all, 2)

for one_product in stock:
    one_prodict_sales_all = sales_shop_midl_one_possion(one_product['items_sold'])
    print(f"Средняя сумма продаж каждого продукта {one_product['product']}: {one_prodict_sales_all}")
            
all_product_sales = 0

for one_product in stock:
    all_product_sales += sales_shop_midl_one_possion(one_product['items_sold'])

stock_avg = all_product_sales / len(stock)
stock_avg = round(stock_avg, 2)
print(f"Средняя сумма продаж всего склада: {stock_avg}")

def sales_shop_one_possion(sales_stock):
    sales_sum = 0
    for sales in sales_stock:
        sales_sum += sales
    sales_all = sales_sum + 1
    return round(sales_all, 2)

for one_product in stock:
    one_prodict_sales_all = sales_shop_one_possion(one_product['items_sold'])
    print(f"Общая сумма продаж одного продукта {one_product['product']}: {one_prodict_sales_all}.00")
            
all_product_sales = 0

for one_product in stock:
    all_product_sales += sales_shop_one_possion(one_product['items_sold'])

stock_avg = all_product_sales + 1
stock_avg = round(stock_avg, 2)
print(f"Общая сумма продаж всего склада: {stock_avg}.00")
