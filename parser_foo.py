from flask import Flask, render_template, url_for, request, redirect
from bs4 import BeautifulSoup
import requests

''' Достаточно кривая функция, но рабочая в подготовленной среде venv. Особое внимание на установку всех используемых
библиотек. Переменные на скорую руку, весь парсер написан с целью опробовать библиотеку BeautifulSoup'''

print("Введите марку авто:")
marka = input()
print("Введите модель авто:")
model = input()
print("Введите год выпуска авто:")
year = input()



def parser_foo(marka, model, year):
    url = 'https://auto.ru/cars/'+str(marka)+'/'+str(model)+'/'+str(year)+'-year/all/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('div', {'class': 'ListingItemPrice-module__content'})
    long_str = []

    for quote in quotes:	#здесь выводим строку с элементами цен вида: ['735Â\xa0000Â\xa0â\x82½', '721Â\xa0000Â\xa0â\x82½', '780Â\xa0000Â\xa0â\x82½'...]
	    long_str.append(quote.text)
	    kol = len(quote)

    price_one = str()
    lst_price_one = []
    sum_price = 0
    result_price = 0

    for i in long_str:
        #print(i) 
        #выводим строки в столбик вида:  735Â 000Â â½  / 721Â 000Â â½  /  780Â 000Â â½ 
        for j in i:
            if j.isdigit():
                price_one = price_one + j              #собираем цены за одну вида 000
                #print(a, end  ='')
            else:
                lst_price_one.append(price_one)                  #формируем лист из преобразованных цен вида 000
                price_one = str()        
                break
    for e in lst_price_one:
        sum_price = sum_price + int(e)
    result_price = sum_price / len(long_str)                    # получение среднеарифметических значений цены автомобиля
    return result_price


print(parser_foo(marka, model, year))


