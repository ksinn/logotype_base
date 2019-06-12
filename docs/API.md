# logotype_base

Список конечных точек

1. Добавить бренд:					POST /brends
2. Добавить логотип:				POST /logotypes
3. Список брендов:					GET /brends
4. Данные о бренде с id=1:				GET /brends/1
5. Список всех логотипов бренда с id=1:		GET /brends/1/logotypes
6. Список всех логотипов:				GET /logotypes
7. Данные о логотипе с id=1:			GET /logotypes/1
8. Обновить  бренд с id=1:				PUT /brends/1
9. Обновить логотип с id=1:			PUT /brends/1
10. Удалить бренд с id=1:				DELETE /brends/1
11. Удалить логотип с id=1:				DELETE /logotypes/1
12. Поиск по брендам				POST / brends/search
12. Поиск по логотипам				POST / logotype/search


Формат данных

Бренд: {
    "id": 1
    "title": "Sаfia",
    "founded": 2002,
    "industry": "Общественное питание",
    "product": "Кандитерские изделия",
    "site": "safiabakery. uz"    
	}

Логотип: {
       "id": 1
            "brend_id": 6,
	"high": 700,
	"width": 700,	
            "type": "jpeg",
            "img": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAA="
	}
В поле img зашифрованный  base64 файл с изображением.


Поиск

Для поиска на конечный точки нужно отправить JSON массив с параметрами поиска. Между параметрами производиться логическая операция И

Формат параметра поиска: {
		"field":"product",
		"operator":"equel",
    		"value": "'Выпечка'"
				}
где поле  field должно содержать параметр по каторому будет производиться поиск,
operator — один из возможных операторов less, more, equel, between
value — единственное значение с которым будет сравниваться параметр из  field, для оператора between необходимо указать два значения в виде массива.
При этом для строчных параметров допустимы только операция эквивалентности и сроку в поле  value НЕОБХОДИМО заключать в одинарные кавычки (Пример: "'Выпечка'").
Числовые значения так же надо записывать в кавычках.

Пример: 
Обращение на точку POST / brends/search с телом:
[
	{
		"field":"id",
		"operator":"more",
    		"value": "1"
	},
	{
		"field":"product",
		"operator":"equel",
    		"value": "'Выпечка'"
	},
	{
		"field":"founded",
		"operator":"between",
    		"value": ["1999", "2015"]
	}
]

бужет эквевалентно SQL запросу:
 
select * from brend where id>1 and product = 'Выпечка' and founded between 1999 and 2015;
