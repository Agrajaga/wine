# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".


## Установка
- Скачайте код
- Установите необходимые зависимости
```
pip install -r requirements.txt
```
Файл с товарами для сайта `wine.xlsx` расположите в корневой папке (там где лежит `main.py`). Он должен иметь следующие колонки:
- Категория - _название категории напитков_
- Название - _название напитка_
- Сорт - _сорт винограда или пустая строка_
- Цена
- Картинка - _имя файла с картинкой_
- Акция - _если ячейка заполнена, то добавляется ярлык "Выгодное предложение"_

_Например:_

Категория | Название | Сорт | Цена | Картинка | Акция
--- | :--- | --- | ---: | --- | ---
Белые вина | Белая леди | Дамский пальчик | 399 | belaya_ledi.png | Выгодное предложение
Напитки | Коньяк классический |  | 350 | konyak_klassicheskyi.png | 
Белые вина | Ркацители | Ркацители | 499 | rkaciteli.png | 
Красные вина | Черный лекарь | Качич | 399 | chernyi_lekar.png | 

## Запуск

- Запустите сайт 
```
python3 main.py
```
- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
