# Домашнее задание по теме "Доступ к свойствам родителя. Переопределение свойств."
# Задача "Изменять нельзя получать":

class Vehicle:
    def __init__(self, owner, model, engine_power, color):
        # Каждый объект Vehicle должен содержать следующие атрибуты объекта:
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    _COLOR_VARIANTS = ["Blue", "Da", "Budi", "Dabydai", "black"]

    # Каждый объект Vehicle должен содержать следующий методы:

    def get_model(self):
        return (f"Модель: {self.__model}")

    def get_horsepower(self):
        return (f"Модель: {self.__engine_power}")

    def get_color(self):
        return (f"Цвет: {self.__color}")

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print("Владелец:", self.owner)

    # Метод set_color - принимает аргумент new_color(str),меняет цвет color на new_color,
    # если он есть в списке COLOR_VARIANTS,в противном случае выводит на экран надпись:"Нельзя сменить цвет"
    def set_color(self, new_color):
        if new_color.lower() in self._COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    # Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

    # Изначальные свойства
vehicle1.print_info()

    # Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

    # Проверяем что поменялось
vehicle1.print_info()
