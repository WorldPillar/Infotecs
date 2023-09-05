# Описание
Задание выполнено с помощью фреймворка __FastAPI__  
Запуск осуществляется через __script.py__ или через команду *uvicorn main:app*  
Необходимые зависимости для запуска находятся в __requirements.txt__  
Основные функции находятся в __main.py__  
Опробовать функции можно с помощью Swagger http://127.0.0.1:8000/docs
## Задание 1
Доступ к методу доступен по запросу *http://127.0.0.1:8000/city/{geonameid}*, 
где
+ geonameid - числовое значение.  

В случае успешного выполнения пользователю вернётся найденный город.
Если города с введенным geonameid найденно не было, пользователю вернётся соответствующая ошибка.  

__Пример работы:__  
Запрос: http://127.0.0.1:8000/city/451747  
Ответ: {
	"geonameid": "451747",
	"name": "Zyabrikovo",
	"asciiname": "Zyabrikovo",
	"alternatenames": [
		""
	],
	"latitude": "56.84665",
	"longitude": "34.7048",
	"feature_class": "P",
	"feature_code": "PPL",
	"country_code": "RU",
	"cc2": "",
	"admin1_code": "77",
	"admin2_code": "",
	"admin3_code": "",
	"admin4_code": "",
	"population": "0",
	"elevation": "",
	"dem": "204",
	"timezone": "Europe/Moscow",
	"modification_date": "2011-07-09"
}

__Название метода:__ *first_task(geonameid: int)*
## Задание 2
Доступ к методу доступен по запросу *http://127.0.0.1:8000/page/{page_number}/numbers/{city_numbers}*, 
где  
+ page_number - номер страницы, больше 1;
+ city_numbers - количество городов на одной странице, больше 1.

В случае успешного выполнения пользователю вернётся список городов на выбранной странице.  
Преполагается, что отсчёт страниц начинается с 1. Если значение страницы или количества городов на странице меньше 1,
пользователю выведется соответствующая ошибка.

__Пример работы:__  
Запрос: http://127.0.0.1:8000/page/2/numbers/3  
Ответ: [  
	{
		"geonameid": "451750",
		"name": "Zhitovo",
		"asciiname": "Zhitovo",
		"alternatenames": [
			""
		],
		"latitude": "57.29693",
		"longitude": "34.41848",
		"feature_class": "P",
		"feature_code": "PPL",
		"country_code": "RU",
		"cc2": "",
		"admin1_code": "77",
		"admin2_code": "",
		"admin3_code": "",
		"admin4_code": "",
		"population": "0",
		"elevation": "",
		"dem": "247",
		"timezone": "Europe/Moscow",
		"modification_date": "2011-07-09"
	},  
	{
		"geonameid": "451751",
		"name": "Zhitnikovo",
		"asciiname": "Zhitnikovo",
		"alternatenames": [
			""
		],
		"latitude": "57.20064",
		"longitude": "34.57831",
		"feature_class": "P",
		"feature_code": "PPL",
		"country_code": "RU",
		"cc2": "",
		"admin1_code": "77",
		"admin2_code": "",
		"admin3_code": "",
		"admin4_code": "",
		"population": "0",
		"elevation": "",
		"dem": "198",
		"timezone": "Europe/Moscow",
		"modification_date": "2011-07-09"
	},  
	{
		"geonameid": "451752",
		"name": "Zhelezovo",
		"asciiname": "Zhelezovo",
		"alternatenames": [
			""
		],
		"latitude": "57.02591",
		"longitude": "34.51886",
		"feature_class": "P",
		"feature_code": "PPL",
		"country_code": "RU",
		"cc2": "",
		"admin1_code": "77",
		"admin2_code": "",
		"admin3_code": "",
		"admin4_code": "",
		"population": "0",
		"elevation": "",
		"dem": "192",
		"timezone": "Europe/Moscow",
		"modification_date": "2011-07-09"
	}  
]

__Название метода:__ *second_task(page_number: int, city_numbers: int)*
## Задание 3
Доступ к методу доступен по запросу *http://127.0.0.1:8000/cities/{first_city_name}/{second_city_name}*, 
где  
+ first_city_name - название первого города;
+ second_city_name - название второго города.

В случае успешного выполнения пользователю вернутся сведения о двух введенных городах под ключами *"first_city"*
и *"second_city"*.  
Под ключом *"north"* будет результат того, какой город находится севернее.  
Под ключом *"timezone"* находится результат проверки временных зон с двумя ключами-значениями:
+ *"is_different"* - с двумя результатами: "Временная зона разная" или "Временная зона одинаковая"
+ *"difference"* - разница в часах двух временных зон  

Если хотя бы один город не был найден, пользователю вернётся соответствующая ошибка.  

__Пример работы:__  
Запрос: http://127.0.0.1:8000/cities/Уфа/Москва  
Ответ: {
	__"first_city"__: {
		"geonameid": "479561",
		"name": "Ufa",
		"asciiname": "Ufa",
		"alternatenames": [
			"Ephu",
			"Oefa",
			"Oufa",
			"Ouffa",
			"Owfa",
			"UFA",
			"Uf",
			"Ufa",
			"Uffa",
			"Ufà",
			"Ufá",
			"Ufа",
			"Upo",
			"awfa",
			"ufa",
			"upa",
			"wu fa",
			"Ĕпхӳ",
			"Оуфа",
			"Уфа",
			"Үфі",
			"Өфө",
			"Ӱпӧ",
			"Ուֆա",
			"אופה",
			"أوفا",
			"اوفا",
			"ऊफ़ा",
			"უფა",
			"ウファ",
			"烏法",
			"우파"
		],
		"latitude": "54.74306",
		"longitude": "55.96779",
		"feature_class": "P",
		"feature_code": "PPLA",
		"country_code": "RU",
		"cc2": "",
		"admin1_code": "08",
		"admin2_code": "",
		"admin3_code": "",
		"admin4_code": "",
		"population": "1120547",
		"elevation": "",
		"dem": "158",
		"timezone": "Asia/Yekaterinburg",
		"modification_date": "2022-09-17"
	},  
	__"second_city"__: {
		"geonameid": "524894",
		"name": "Moskva",
		"asciiname": "Moskva",
		"alternatenames": [
			"Maskva",
			"Moscou",
			"Moscow",
			"Moscu",
			"Moscú",
			"Moskau",
			"Moskou",
			"Moskovu",
			"Moskva",
			"Məskeu",
			"Москва",
			"Мәскеу"
		],
		"latitude": "55.76167",
		"longitude": "37.60667",
		"feature_class": "A",
		"feature_code": "ADM1",
		"country_code": "RU",
		"cc2": "",
		"admin1_code": "48",
		"admin2_code": "",
		"admin3_code": "",
		"admin4_code": "",
		"population": "13010112",
		"elevation": "",
		"dem": "161",
		"timezone": "Europe/Moscow",
		"modification_date": "2023-01-12"
	},  
	__"north"__: "Москва севернее",  
	__"timezone"__: {
		"is_different": "Временная зона разная",
		"difference": "Различие часов: 2"
	}
}

__Название метода:__ *third_task(first_city_name: str, second_city_name: str)*
## Дополнительное задание
Доступ к методу доступен по запросу *http://127.0.0.1:8000/hint/{inc_name}*, 
где  
+ inc_name - часть названия города;  

В случае успешного выполнения пользователю под ключом *"hints"* вернется список возможных вариантов продолжения слова, 
то есть при вводе __"Мос"__ программа предложит, например, __"ква"__

__Пример работы:__  
Запрос: http://127.0.0.1:8000/hint/Уф  
Ответ: {
	"hints": [
		"имщина",
		"имский район",
		"имский Каменный Карьер",
		"имка",
		"имский",
		"тюга",
		"имцы",
		"имцево",
		"а-Шигири",
		"имовский",
		"а",
		"алейка"
	]
}

__Название метода:__ *additional_task(inc_name: str)*