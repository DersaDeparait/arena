import pandas

class Character:
    regular_characters = []
    params = {
        "сила": 10,
        "виносливість": 10,
        "ловкість": 10,
        "точність": 10,

        "володіння зброєю": 10,
        "ініціативність": 10,
        "сприйняття": 10,
        "удача": 10,
    }
    def __init__(self,id=0,  name="Warrior", image=None, health=1000,
                 params_points = 10, skill_points = 3,
                 weapon_down=10, weapon_up=20,
                 power=10, endurance=10, dexterity=10, precision = 10,
                 initiative=10, weapon_skill=10, perception=10, luck=10,

                 block_chance=1, dodge_chance=1, counterattack_chance=1, counterattack_value=400, critical_chance=1, critical_mod=500,
                 venom_chance=0, venom_value=0, selfheal_chance=0, selfheal_value=0,
                 stun_chance=0,double_attack_chance=0,triple_attack_chance=0,instant_kill_chance=0,
                 fighting_spirit_chance = 1,
                 skills = [], **kwargs):

        if Character.regular_characters == []:
            [Character.regular_characters.append(Character.return_character(i)) for i in range(12)]

        self.id = id
        self.name = name
        self.image = image
        self.health_max = health
        self.health_curent = health

        self.params_points = params_points
        self.skill_points = skill_points

        self.weapon = [weapon_down, weapon_up]

        self.params = dict(Character.params)
        self.params["сила"] = power
        self.params["виносливість"] = endurance
        self.params["ловкість"] = dexterity
        self.params["точність"] = precision
        self.params["володіння зброєю"] = weapon_skill
        self.params["ініціативність"] = initiative
        self.params["сприйняття"] = perception
        self.params["удача"] = luck

        self.params_else = {
            "Блок шанс": block_chance,
            "Уворот шанс": dodge_chance,
            "Контраудар шанс": counterattack_chance,
            "Контраудар мод": counterattack_value,
            "Критичний шанс": critical_chance,
            "Критичний мод":critical_mod,

            "Отрута шанс": venom_chance,
            "Отрута сила": venom_value,

            "Автохіл шанс": selfheal_chance,
            "Автохіл сила": selfheal_value,

            "Оглушаючий удара шанс": stun_chance,
            "Двойний удар шанс": double_attack_chance,
            "Тройний удар шанс": triple_attack_chance,
            "Моментальне вбивство шанс": instant_kill_chance,

            "Бойовий дух шанс": fighting_spirit_chance
        }

        self.skills = []
        if type(skills) == list:
            self.skills = skills
        elif type(skills) == str:
            s = skills.split(" ")
            print(s)
            for i in s:
                if i != '':
                    self.skills.append(int(i))


        self.venoms_on_me = {}
        self.position_on_ruler = 0

    def get_info(self, info=0): #fixme Переробити вивод
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
        s += "\nЗалишилося очок параметрів: {}".format(self.params_points)
        s += "\nЗалишилося очок навиків: {}".format(self.skill_points)
        return s

    def params_up(self, param):
        if self.params_points > 0:
            self.params_points -= 1
            self.params[param] += 3

    def get_picture(self):
        path = "content/images/characters/"
        return open(path+self.image, "rb")

    def add_skill(self, skill_number):
        if self.skill_points > 0:
            self.skills.append(skill_number)
            self.skill_points -= 1

    @staticmethod
    def return_character(number=0):
        c = Character(**Character.get_line_from_csv(number))
        return c
    @staticmethod
    def get_line_from_csv(line_number, file_path="content/data/character_params.csv"):
        p = pandas.read_csv(file_path, sep=";")
        p = p[line_number:line_number + 1].to_dict()
        to_return = {}
        for key in p:
            to_return[key] = p[key][line_number]
        return to_return

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
    18:["Стійкість","",""],
    19:["Стійкість +","",""],
}