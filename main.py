import io
from typing_extensions import TypedDict
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pytz
from datetime import datetime
from dateutil.relativedelta import relativedelta


KEY_LIST = ["geonameid", "name", "asciiname", "alternatenames", "latitude", "longitude", "feature_class",
            "feature_code", "country_code", "cc2", "admin1_code", "admin2_code", "admin3_code", "admin4_code",
            "population", "elevation", "dem", "timezone", "modification_date"]


class CityModel(BaseModel):
    geonameid: str
    name: str
    asciiname: str
    alternatenames: list[str]
    latitude: str
    longitude: str
    feature_class: str
    feature_code: str
    country_code: str
    cc2: str
    admin1_code: str
    admin2_code: str
    admin3_code: str
    admin4_code: str
    population: str
    elevation: str
    dem: str
    timezone: str
    modification_date: str


def parse():
    cities = []
    with io.open('RU.txt', encoding='utf-8') as f:
        lines = f.readlines()

        for line in lines:
            city = line[:-1].split('\t')
            city[3] = city[3].split(',')
            cities.append(city)
    return cities


CITIES = parse()

app = FastAPI(
    title="Задание для Infotecs",
    contact={
        "name": "Илья Ежов",
        "email": "ilyaezhov-a@yandex.ru",
    })


def list2dict(orig_list: list):
    """
    Функция преобразует список в словарь с ключами из KEY_LIST
    """
    res_dct = dict(zip(KEY_LIST, orig_list))
    return res_dct


# Задание 1
@app.get("/city/{geonameid}", response_model=CityModel)
async def first_task(geonameid: int):
    """
    Фукнция для решения первого задания
    :param geonameid: параметр geonameid для поиска города
    :return: найденный город
    """
    try:
        # Преобразуем список в словарь
        answer = list2dict(CITIES[geonameid - 451747])
        return answer
    # Если не было найдено города с таким geonameid, пользователю отправляется ошибка
    except IndexError:
        raise HTTPException(status_code=400, detail="Города с таким geonameid нет")


# Задание 2
@app.get("/page/{page_number}/numbers/{city_numbers}", response_model=list[CityModel])
async def second_task(page_number: int, city_numbers: int):
    """
    Функция для решения второго задания
    :param page_number: номер страницы
    :param city_numbers: количество городов на одной странице
    :return: список городов
    """
    if page_number < 1 or city_numbers < 1:
        raise HTTPException(status_code=400, detail="Страница или количество городов на одной странице меньше 1")

    # Находим номер первого города на странице
    first = (page_number - 1) * city_numbers

    list_cities = [list2dict(x) for x in CITIES[first: first + city_numbers]]
    return list_cities

Task3 = TypedDict('Task3', {'first_city': CityModel, 'second_city': CityModel, 'north': str,
                            'timezone': TypedDict('Time', {'is_different': str, 'difference': str})})


# Задание 3
@app.get("/cities/{first_city_name}/{second_city_name}", response_model=Task3)
async def third_task(first_city_name: str, second_city_name: str):
    """
    Функция для решения третьего задания
    :param first_city_name: название первого города
    :param second_city_name: название второго города
    :return: два найденных города; город, находящийся севернее; разность временных зон
    """
    first_city_name = first_city_name.capitalize()
    second_city_name = second_city_name.capitalize()

    first_city = None
    second_city = None
    for city in CITIES:
        for alt_name in city[3]:
            if alt_name == first_city_name:
                if first_city is None or int(city[14]) > int(first_city[14]):
                    first_city = city
            if alt_name == second_city_name:
                if second_city is None or int(city[14]) > int(second_city[14]):
                    second_city = city

    # Если хотя бы один город не был найден, пользователю выведется ошибка
    if first_city is None or second_city is None:
        raise HTTPException(status_code=400, detail="Один или оба города не были найдены")

    # Преобразуем списки в словари
    first_city = list2dict(first_city)
    second_city = list2dict(second_city)

    # Сравниваем широту городов, чтобы найти, какой из них расположен севернее
    if float(first_city['latitude']) > float(second_city['latitude']):
        north = f'{first_city_name} севернее'
    elif first_city['latitude'] < second_city['latitude']:
        north = f'{second_city_name} севернее'
    else:
        north = 'Города одинаковой широты'

    # Сравниваем временную зону
    if first_city['timezone'] != second_city['timezone']:
        # Если временные зоны разные, находим время для каждой зоны
        utcnow = pytz.timezone('utc').localize(datetime.utcnow())
        first = utcnow.astimezone(pytz.timezone(first_city['timezone'])).replace(tzinfo=None)
        second = utcnow.astimezone(pytz.timezone(second_city['timezone'])).replace(tzinfo=None)
        # Получаем разность времени
        offset = relativedelta(first, second)
        timezone = {'is_different': 'Временная зона разная', 'difference': f'Различие часов: {offset.hours}'}
    else:
        timezone = {'is_different': 'Временная зона одинаковая', 'difference': f'Различие часов: 0'}

    answer = {'first_city': first_city, 'second_city': second_city, 'north': north, 'timezone': timezone}
    return answer

Hint = TypedDict('Hint', {'hints': list[str]})


# Дополнительное задание
@app.get("/hint/{inc_name}", response_model=Hint)
async def additional_task(inc_name: str):
    """
    Функция для выполнения дополнительного задания
    :param inc_name: неполное название города
    :return: список возможных продолжений названия города
    """
    inc_name = inc_name.capitalize()

    hints = []
    for city in CITIES:
        for alt_name in city[3]:
            # Проверяем, начинается ли название с переданной строки
            if alt_name.startswith(inc_name):
                # Если начинается, обрезаем совпавшую часть
                hint = alt_name[len(inc_name):]
                if hint != '':
                    hints.append(hint)
                break
    set_hints = set(hints)

    answer = {'hints': set_hints}
    return answer
