class Cal:
    def __init__(self, name_cal, color_cal, consistenscy_cal):
        self.name:str = name_cal
        self.age:int = 4
        self.color:str = color_cal
        self.consistency:str = consistenscy_cal
    def cal_behavior(self):
        print(f'{self.name}, цвет кала, насыщенный: {self.color}')
    def description(self):
        print(f'{self.name}, плотность кала: {self.consistency}')
    def vozrast(self):
        print(f'Возраст кала: {self.age}')

govno = Cal('Kalishe',  'коричневато-зеленый', 'слегка твердый')
govno_v2 = Cal('Дерьмо', 'Черный', 'жидкий')
x = govno.description()
y = govno_v2.description()
z = govno.vozrast()
print(x, y, z)
