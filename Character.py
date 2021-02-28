class Character:
    params = {
        "сила": 10,
        "виносливість": 10,
        "ловкість": 10,
        "ініціативність": 10,
        "володіння зброєю": 10,
        "сприйняття": 10,
        "удача": 10,
    }
    def __init__(self, name="Warrior", image=None, power=10, endurance=10, dexterity=10, initiative=10, weapon_skill=10,
                 perception=10, luck=10,
                 weapon=[2, 10]):
        self.params = dict(Character.params)
        self.params["сила"] = power
        self.params["виносливість"] = endurance
        self.params["ловкість"] = dexterity
        self.params["ініціативність"] = initiative
        self.params["володіння зброєю"] = weapon_skill
        self.params["сприйняття"] = perception
        self.params["удача"] = luck

        self.params_else = {
            "Блок шанс": 1,
            "Уворот шанс": 1,
            "Контраудар шанс": 1,
            "Сила контраудара": 400,

            "Отрута шанс": 0,
            "Отрута сила": 0,
            "Отрута на собі": 0,

            "Автохіл шанс": 0,
            "Автохіл значення": 0,

            "Оглушаючого удара шанс": 0,
            "Двойний удар шанс": 0,
            "Тройний удар шанс": 0,

            "Бойовий дух шанс": 0
        }
        self.name = name
        self.image = image
        self.params_points = 10
        self.skill_points = 2
        self.position_on_ruler = 0
        self.health_max = 1000
        self.health_curent = 1000
        self.weapon = weapon
        self.skills = []

    def get_info(self, info=0):
        s = "Герой {},    ❤️{}".format(self.name, self.health_max)
        s += "\n{0:<25}: {1:>5}-{2:<5}".format("Урон зброї", self.weapon[0], self.weapon[1])
        s += "\n"
        if info > 0:
            s += "\n{0:<30}: {1:>10}".format("сила", self.params["сила"])
            s += "\n{0:<30}: {1:>10}".format("виносливість", self.params["виносливість"])
            s += "\n{0:<30}: {1:>10}".format("ловкість", self.params["ловкість"])
            s += "\n{0:<30}: {1:>10}".format("ініціативність", self.params["ініціативність"])
            s += "\n{0:<30}: {1:>10}".format("володіння зброєю", self.params["володіння зброєю"])
            s += "\n{0:<30}: {1:>10}".format("сприйняття", self.params["сприйняття"])
            s += "\n{0:<30}: {1:>10}".format("удача", self.params["удача"])
            s += "\n"
        s += "\n{0:<38}: {1:>10.1%}".format("Блок шанс", self.params_else["Блок шанс"] / 1000)
        s += "\n{0:<35}: {1:>10.1%}".format("Уворот шанс", self.params_else["Уворот шанс"] / 1000)
        s += "\n{0:<29}: {1:>10.1%}".format("Контраудар шанс", self.params_else["Контраудар шанс"] / 1000)
        s += "\n"
        s += "\nЗалишилося вкласти очок: {}".format(self.params_points)
        return s

    def params_up(self, param):
        if self.params_points > 0:
            self.params_points -= 1
            self.params[param] += 3

    def get_picture(self):
        return open(self.image, "rb")

    def add_skill(self, skill_number):
        if self.skill_points > 0:
            self.skills.append(skill_number)
            self.skill_points -= 1

    @staticmethod
    def return_character(number=0):
        path = "content/images/characters/"
        if number == 0:
            c = Character(name="No One", image=path+"x0.jpg", power=10, endurance=10, dexterity=10, initiative=10,
                          weapon_skill=10, perception=10, luck=10, weapon=[30, 50])
        elif number == 1:
            c = Character(name="Рицар", image=path+"x1.jpg", power=10, endurance=10, dexterity=10, initiative=10,
                          weapon_skill=10, perception=10, luck=10, weapon=[10, 50])
        elif number == 2:
            c = Character(name="Варвар", image=path+"x2.jpg", power=10, endurance=10, dexterity=10, initiative=10,
                          weapon_skill=10, perception=10, luck=10, weapon=[30, 70])
        elif number == 3:
            c = Character(name="Воїн", image=path+"x3.jpg", power=10, endurance=10, dexterity=10, initiative=10,
                          weapon_skill=10, perception=10, luck=10, weapon=[40, 45])
        elif number == 4:
            c = Character(name="Вор", image=path+"x4.jpg", power=10, endurance=10, dexterity=10, initiative=10,
                          weapon_skill=10, perception=10, luck=10, weapon=[15, 30])
        elif number == 5:
            c = Character(name="Дуелянтка", image=path+"x5.jpg", power=10, endurance=10, dexterity=10, initiative=10,
                          weapon_skill=10, perception=10, luck=10, weapon=[50, 60])
        elif number == 6:
            c = Character(name="Берсеркер", image=path+"x6.jpg", power=10, endurance=10, dexterity=10, initiative=10,
                          weapon_skill=10, perception=10, luck=10, weapon=[10, 65])
        elif number == 7:
            c = Character(name="Мандрівник", image="x7.jpg", power=10, endurance=10, dexterity=10, initiative=10,
                          weapon_skill=10, perception=10, luck=10, weapon=[40, 80])
        elif number == 8:
            c = Character(name="Піратка", image="x8.jpg", power=10, endurance=10, dexterity=10, initiative=10,
                          weapon_skill=10, perception=10, luck=10, weapon=[10, 30])
        elif number == 9:
            c = Character(name="Алебардщик", image="x9.jpg", power=10, endurance=10, dexterity=10, initiative=10,
                          weapon_skill=10, perception=10, luck=10, weapon=[60, 120])
        elif number == 10:
            c = Character(name="Темний воїн", image="x10.jpg", power=10, endurance=10, dexterity=10, initiative=10,
                          weapon_skill=10, perception=10, luck=10, weapon=[40, 60])
        elif number == 11:
            c = Character(name="Лучниця", image="x11.jpg", power=10, endurance=10, dexterity=10, initiative=10,
                          weapon_skill=10, perception=10, luck=10, weapon=[25, 50])
        elif number == 12:
            c = Character(name="Копейщиця", image="x12.jpg", power=10, endurance=10, dexterity=10, initiative=10,
                          weapon_skill=10, perception=10, luck=10, weapon=[20, 40])
        else:
            c = Character(name="000", power=10, endurance=10, dexterity=10, initiative=10, weapon_skill=10,
                          perception=10, luck=10, weapon=[10, 20])
        return c


skills = {
    0:["Оглушаючий удар", "", ""],
    1:["Оглушаючий удар +", "", ""],
    2:["Двойний удар", "", ""],
    3:["Тройний удар", "", ""],
    4:["Вдачний", "", ""],
    5:["Народжений в рубашці", "", ""],
    6:["Отравлена зброя", "", ""],
    7:["Отравлена зброя +", "", ""],
    8:["Контраатакуючий", "", ""],
    9:["Контраатакуючий +", "", ""],
    10:["Гнучкий", "", ""],
    11:["Гнучкий +", "", ""],
    12:["Блокуючий", "", ""],
    13:["Блокуючий +", "", ""],
    14:["Лікар", "", ""],
    15:["Хілер", "", ""],
    16:["Натхненний", "", ""],
    17:["Натхненний +", "", ""],
}