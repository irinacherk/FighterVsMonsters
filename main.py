from abc import ABC, abstractmethod

# Шаг 1: Абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Шаг 2: Реализация оружия
class Sword(Weapon):
    def attack(self):
        print("Боец наносит удар мечом.")

class Bow(Weapon):
    def attack(self):
        print("Боец наносит удар из лука.")

# Шаг 3: Класс бойца
class Fighter:
    def __init__(self, name, weapon: Weapon):
        self.name = name
        self.weapon = weapon

    def change_weapon(self, new_weapon: Weapon):
        self.weapon = new_weapon
        print(f"{self.name} выбрал новое оружие.")

    def attack(self):
        self.weapon.attack()

# Шаг 4: Реализация боя с монстром
class Monster:
    def __init__(self, name):
        self.name = name

    def take_damage(self):
        print(f"{self.name} побежден!")

# Пример использования
if __name__ == "__main__":
    sword = Sword()
    bow = Bow()

    fighter = Fighter(name="Игрок", weapon=sword)
    monster = Monster(name="Гоблин")

    print("Боец выбирает меч.")
    fighter.attack()
    monster.take_damage()

    print("\nБоец выбирает лук.")
    fighter.change_weapon(bow)
    fighter.attack()
    monster.take_damage()
