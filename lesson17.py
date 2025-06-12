class Cal:
    def __init__(self, name_cal, color_cal, consistenscy_cal):
        self.name:str = name_cal
        self.age:int = 4
        self.color:str = color_cal
        self.consistency:str = consistenscy_cal

    def cal_behavior(self):
        return f'{self.name}, цвет кала, насыщенный: {self.color}'
        result = cal_behavior(self)
        print("Результат функции:", result)

    def description(self):
        return f'{self.name}, плотность кала: {self.consistency}'
        result2 = description(self)
        print("Результат функции:", result2)

    def vozrast(self):
        return f'Возраст кала: {self.age}'
        result3 = vozrast(self)
        print("Результат функции:", result3)

    def check_color(self):
        if self.color.lower() == 'зеленый':
            return f'вот такой цвет-{self.color}, держи лапирамид'
        else:
            return self.color

govno = Cal('Kalishe',  'коричневато-зеленый', 'слегка твердый')
govno_v2 = Cal('Дерьмо', 'Черный', 'жидкий')
govno_v3 = Cal('Дерьмище', 'Зеленый', 'жидкий', )

x = govno.description()
y = govno_v2.description()
z = govno.vozrast()
c = govno_v3.check_color()

print(x, y, z, c)
