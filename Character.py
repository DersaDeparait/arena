import pandas
import copy

class Character:
    regular_characters = []
    params = {
        "power":[10, "сила", "Усиляє пряму атаку"],
        "endurance":[10, "виносливість", "Збільшує кількість здоровя"],

        "dexterity":[10, "ловкість", "Збільшує шанси на двойний удар"],
        "speed":[10, "скорость", "Збільшує частоту ходів"],

        "precision": [10, "точність", "Збільшує критичний удар"],
        "intelligence": [10, "інтелект", ""],

        "spirit":[10, "дух", ""],
        "wisdom":[10, "мудрість", ""],

        "perception":[10, "сприйняття", "Збільшує ймовірності реакції на удари"],
        "luck":[10, "удача", "Робить кращим життя взагалі"],
    }
    skills = {
        0: ["Оглушаючий удар", "", ""],
        1: ["Двойний удар", "", ""],
        2: ["Тройний удар", "", ""],
        3: ["Вдачний", "", ""],
        4: ["Народжений в рубашці", "", ""],
        5: ["Отравлена зброя", "", ""],
        6: ["Контраатакуючий", "", ""],
        7: ["Гнучкий", "", ""],
        8: ["Блокуючий", "", ""],
        9: ["Лікар", "", ""],
        10: ["Натхненний", "", ""],
        11: ["Стійкість", "", ""],
        12: ["Володіння збрєю", "", ""],
    }

    addition_points_from_one = 4

    @staticmethod
    def set_default_characters():
        if Character.regular_characters == []:
            [Character.regular_characters.append(Character.return_character(i)) for i in range(20)]
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


    def __init__(self,id=0,  name="Warrior", image=None, health=1000,
                 params_points = 10, skill_points = 3,
                 weapon_down=10, weapon_up=20, armor=10,
                 power=10, endurance=10, dexterity=10, speed=10, precision=10, intelligence=10,
                 spirit=10, wisdom=10, perception=10, luck=10,

                 block_chance=1, dodge_chance=1, counterattack_chance=1, counterattack_value=400, critical_chance=1, critical_mod=500,
                 venom_chance=0, venom_value=0, selfheal_chance=0, selfheal_value=0,
                 stun_chance=0,double_attack_chance=0,triple_attack_chance=0,instant_kill_chance=0,rebuff_chance=50,rebuff_value=500,
                 fighting_spirit_chance = 1,
                 skills = [], **kwargs):

        self.id = id
        self.name = name
        self.image = image
        self.health_base = health

        self.params_points = params_points
        self.skill_points = skill_points

        self.weapon = [weapon_down, weapon_up]
        self.armor = armor

        self.params = copy.deepcopy(Character.params)
        self.params["power"][0] = power
        self.params["endurance"][0] = endurance
        self.params["dexterity"][0] = dexterity
        self.params["speed"][0] = speed
        self.params["precision"][0] = precision
        self.params["intelligence"][0] = intelligence
        self.params["spirit"][0] = spirit
        self.params["wisdom"][0] = wisdom
        self.params["perception"][0] = perception
        self.params["luck"][0] = luck

        self.params_else = {
            "block_chance": block_chance,
            "dodge_chance": dodge_chance,
            "counterattack_chance": counterattack_chance,
            "counterattack_value": counterattack_value,
            "critical_chance": critical_chance,
            "critical_mod":critical_mod,

            "venom_chance": venom_chance,
            "venom_value": venom_value,

            "selfheal_chance": selfheal_chance,
            "selfheal_value": selfheal_value,

            "stun_chance": stun_chance,
            "double_attack_chance": double_attack_chance,
            "triple_attack_chance": triple_attack_chance,
            "instant_kill_chance": instant_kill_chance,
            "rebuff_chance":rebuff_chance,
            "rebuff_value": rebuff_value,

            "fighting_spirit_chance": fighting_spirit_chance
        }

        self.skills = [0] * 50
        if type(skills) == list: self.skills = skills

        self.venoms_on_me = {}
        self.position_on_ruler = 0

        self.calculate_upped_params()

    def calculate_upped_params(self):
        small_div = 4
        big_mult = 20
        upper_mult = 50
        # 0: ["Оглушаючий удар", "", ""],
        # 1: ["Двойний удар", "", ""],
        # 2: ["Тройний удар", "", ""],
        # 3: ["Вдачний", "", ""],
        # 4: ["Народжений в рубашці", "", ""], fixme
        # 5: ["Отравлена зброя", "", ""],
        # 6: ["Контраатакуючий", "", ""],
        # 7: ["Гнучкий", "", ""],
        # 8: ["Блокуючий", "", ""],
        # 9: ["Лікар", "", ""],
        # 10: ["Натхненний", "", ""],
        # 11: ["Стійкість", "", ""],
        # 12: ["Володіння збрєю", "", ""],

        self.upped_params = {
            "health": self.health_base + self.params["endurance"][0] * big_mult,
            "weapon": [self.weapon[0] * (1 + self.params["power"][0] / 100),
                       self.weapon[1] * (1 + self.params["power"][1] / 100)],
            "armor": self.armor,

            "block_chance": self.params_else["block_chance"] + self.params["endurance"][0]//small_div + self.params["perception"][0]//small_div,
            "dodge_chance": self.params_else["dodge_chance"] + self.params["dexterity"][0]//small_div + self.params["perception"][0]//small_div,
            "counterattack_chance": self.params_else["counterattack_chance"] + self.params["intelligence"][0]//small_div + self.params["perception"][0]//small_div,
            "counterattack_value": self.params_else["counterattack_value"] + self.params["intelligence"][0] * big_mult,
            "critical_chance": self.params_else["critical_chance"] + self.params["precision"][0]//small_div + self.params["perception"][0]//small_div,
            "critical_mod":self.params_else["critical_mod"] + self.params["precision"][0]*big_mult,

            "venom_chance": self.params_else["venom_chance"],
            "venom_value": self.params_else["venom_value"],

            "selfheal_chance": self.params_else["selfheal_chance"] + self.params["endurance"][0]//upper_mult,
            "selfheal_value": self.params_else["selfheal_value"] + self.params["endurance"][0]//upper_mult,

            "stun_chance": self.params_else["stun_chance"] + self.skills[0] * 100,
            "double_attack_chance": self.params_else["double_attack_chance"] + self.params["dexterity"][0]//small_div + self.skills[1] * 200,
            "triple_attack_chance": self.params_else["triple_attack_chance"] + self.params["dexterity"][0]//small_div + self.skills[2] * 200,
            "instant_kill_chance": self.params_else["instant_kill_chance"] + self.params["wisdom"][0]//upper_mult,
            "rebuff_chance":self.params_else["rebuff_chance"] + self.params["speed"][0]//small_div,
            "rebuff_value": self.params_else["rebuff_value"] + self.params["speed"][0]*big_mult,

            "fighting_spirit_chance": self.params_else["fighting_spirit_chance"],

            "lack": self.params["luck"] + self.skills[3] * big_mult
        }

        self.health_curent = self.upped_params["health"]


    def get_info(self, info=0): #fixme Переробити вивод
        s = "Герой {},    ❤️{}".format(self.name, self.upped_params["health"])
        s += "\n{0:<25}: {1:>5}-{2:<5}".format("Урон зброї: ", self.upped_params["weapon"][0], self.upped_params["weapon"][1])
        s += "\n{0:<25}: {1:>5}".format("Броня: ", self.upped_params["armor"])
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
            self.params[param] += Character.addition_points_from_one
    def add_skill(self, skill_number):
        if self.skill_points > 0:
            self.skills[skill_number] += self.skills[skill_number]
            self.skill_points -= 1
    def get_picture(self):
        path = "content/images/characters/"
        return open(path + self.image, "rb")
