**01. Реализация простого класса для чтения из файла**

Первое задание на этой неделе — не сложное, для разогрева. Ваша задача: написать python-модуль solution.py, внутрь которого необходимо поместить код класса FileReader. Конструктор этого класса принимает один параметр: путь до файла на диске. В классе FileReader должен быть реализован метод read, возвращающий строку - содержимое файла, путь к которому был указан при создании экземпляра класса. Python модуль должен быть написан таким образом, чтобы импорт класса FileReader из него не вызвал ошибок.

При написании реализации метода read, вам нужно учитывать случай, когда при инициализации был передан путь к несуществующему файлу. Требуется обработать возникающее при этом исключение FileNotFoundError и вернуть из метода read пустую строку.

Пример работы:

```
>>> from solution import FileReader
>>> reader = FileReader('not_exist_file.txt')
>>> text = reader.read()
>>> text
''
>>> with open('some_file.txt', 'w') as file:
...     file.write('some text')
...
9
>>> reader = FileReader('some_file.txt')
>>> text = reader.read()
>>> text
'some text'
>>> type(reader) 
<class 'solution.FileReader'>
>>> 
```

**02. Классы и наследование**

Предположим есть данные о разных автомобилях и спецтехнике. Данные представлены в виде таблицы с характеристиками. Вся техника разделена на три вида: спецтехника, легковые и грузовые автомобили. Обратите внимание на то, что некоторые характеристики присущи только определенному виду техники. Например, у легковых автомобилей есть характеристика «кол-во пассажирских мест», а у грузовых автомобилей — габариты кузова: «длина», «ширина» и «высота».

Вам необходимо создать свою иерархию классов для данных, которые описаны в таблице. Классы должны называться CarBase (базовый класс для всех типов машин), Car (легковые автомобили), Truck (грузовые автомобили) и SpecMachine (спецтехника). Все объекты имеют обязательные атрибуты:

- car_type, значение типа объекта и может принимать одно из значений: «car», «truck», «spec_machine».

- photo_file_name, имя файла с изображением машины, допустимы названия файлов изображений с расширением из списка: «.jpg», «.jpeg», «.png», «.gif»

- brand, марка производителя машины

- carrying, грузоподъемность

В базовом классе CarBase нужно реализовать метод get_photo_file_ext для получения расширения файла изображения. Расширение файла можно получить при помощи os.path.splitext.

Для грузового автомобиля необходимо в конструкторе класса определить атрибуты: body_length, body_width, body_height, отвечающие соответственно за габариты кузова — длину, ширину и высоту. Габариты передаются в параметре body_whl (строка, в которой размеры разделены латинской буквой «x»). Обратите внимание на то, что характеристики кузова должны быть вещественными числами и характеристики кузова могут быть не валидными (например, пустая строка). В таком случае всем атрибутам, отвечающим за габариты кузова, присваивается значение равное нулю.

Также для класса грузового автомобиля необходимо реализовать метод get_body_volume, возвращающий объем кузова.

В классе Car должен быть определен атрибут passenger_seats_count (количество пассажирских мест), а в классе SpecMachine — extra (дополнительное описание машины).

Далее вам необходимо реализовать функцию get_car_list, на вход которой подается имя файла в формате csv. Файл содержит данные, аналогичные строкам из таблицы. Вам необходимо прочитать этот файл построчно при помощи модуля стандартной библиотеки csv. Затем проанализировать строки на валидность и создать список объектов с автомобилями и специальной техникой. Функция должна возвращать список объектов.

Вы можете использовать для отладки работы функции get_car_list следующий csv-файл:

```
coursera_week3_cars.csv
```

Первая строка в исходном файле — это заголовок csv, который содержит имена колонок. Нужно пропустить первую строку из исходного файла. Обратите внимание на то, что в некоторых строках исходного файла , данные могут быть заполнены некорректно, например, отсутствовать обязательные поля или иметь не валидное значение. В таком случае нужно проигнорировать подобные строки и не создавать объекты. Строки с пустым или не валидным значением для body_whl игнорироваться не должны.  Вы можете использовать стандартный механизм обработки исключений в процессе чтения, валидации и создания объектов из строк csv-файла. Проверьте работу вашего кода с входным файлом, прежде чем загружать задание для оценки.

Пример кода, демонстрирующего чтение csv файла:

```python
import csv

with open(csv_filename) as csv_fd:
    reader = csv.reader(csv_fd, delimiter=';')
    next(reader)  # пропускаем заголовок
    for row in reader:
        print(row)
```

Ниже приведен шаблон кода для выполнения задания:

```python
class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        pass


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        pass


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        pass


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        pass


def get_car_list(csv_filename):
    car_list = []
    return car_list
```


Несколько примеров работы:

```
>>> from solution import *
>>> car = Car('Bugatti Veyron', 'bugatti.png', '0.312', '2')
>>> print(car.car_type, car.brand, car.photo_file_name, car.carrying,
... car.passenger_seats_count, sep='\n')
car
Bugatti Veyron
bugatti.png
0.312
2
>>> truck = Truck('Nissan', 'nissan.jpeg', '1.5', '3.92x2.09x1.87')
>>> print(truck.car_type, truck.brand, truck.photo_file_name, truck.body_length,
... truck.body_width, truck.body_height, sep='\n')
truck
Nissan
nissan.jpeg
3.92
2.09
1.87
>>> spec_machine = SpecMachine('Komatsu-D355', 'd355.jpg', '93', 'pipelayer specs')
>>> print(spec_machine.car_type, spec_machine.brand, spec_machine.carrying,
... spec_machine.photo_file_name, spec_machine.extra, sep='\n')
spec_machine
Komatsu-D355
93.0
d355.jpg
pipelayer specs
>>> spec_machine.get_photo_file_ext()
'.jpg'
>>> cars = get_car_list('cars_week3.csv')
>>> len(cars)
4
>>> for car in cars:
...     print(type(car))
... 
<class 'solution.Car'>
<class 'solution.Truck'>
<class 'solution.Truck'>
<class 'solution.Car'>
>>> cars[0].passenger_seats_count
4
>>> cars[1].get_body_volume()
60.0
>>> 
```