class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я родился(ась) {self.birth_date}, работаю {self.occupation}.")


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group_name):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name

    def introduce(self):
        gender = "одноклассник" if not self.name.endswith("а") else "одноклассница"
        print(f"Привет, меня зовут {self.name}, я {gender} Игоря, учил(ся/ась) вместе в {self.group_name}, "
              f"я родил(ся/ась) {self.birth_date}, работаю {self.occupation}.")


class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        gender = "хороший друг" if not self.name.endswith("а") else "хорошая подруга"
        print(f"Привет, меня зовут {self.name}, я {gender} Игоря, родил(ся/ась) {self.birth_date}, "
              f"работаю {self.occupation}, увлекаюсь {self.hobby}.")


classmate_1 = Classmate(name="Жан-Тур", birth_date="01.01.2001", occupation="Инженер", higher_education=True, group_name="11 Б")
classmate_2 = Classmate(name="Нур-Султан", birth_date="12.04.2000", occupation="Маркетолог", higher_education=True, group_name="11 Б")
friend_1 = Friend(name="Алина", birth_date="17.03.2003", occupation="Фотограф", higher_education=False, hobby="рисование")
friend_2 = Friend(name="Айгерим", birth_date="22.09.2002", occupation="Дизайнер", higher_education=True, hobby="чтение")

for prsn in [classmate_1, classmate_2, friend_1, friend_2]:
    prsn.introduce()