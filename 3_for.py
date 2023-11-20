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
phone = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]


 
def main():
    sum_sales_product_all = 0
    count_sales = 0
    for i in phone: 
        sum_sales_product = sum(i['items_sold']) 
        sum_sales_product_all += sum_sales_product
        count_sales += len(i['items_sold'])

    
        print(f'Сумма всех продаж товара {i["product"]} = {sum_sales_product}')
        print(f'Среднее количество продаж товара {i["product"]} = {round(sum_sales_product/len(i["items_sold"]), 1)}')
    print(f'Сумма продаж всех товаров = {sum_sales_product_all}')
    print(f'Среднее количество всех продаж товара = {round(sum_sales_product_all/count_sales, 1)}')


    
    
    
if __name__ == "__main__":
    main()
