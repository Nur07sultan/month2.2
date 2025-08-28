from datetime import datetime


class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.__birth_date = birth_date  # приватный
        self.__occupation = occupation  # приватный
        self.__higher_education = higher_education  # приватный

    @property
    def occupation(self):
        return self.__occupation

    @property
    def higher_education(self):
        return self.__higher_education

    @property
    def age(self):
        birth = datetime.strptime(self.__birth_date, "%d.%m.%Y")
        today = datetime.today()
        return today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))

    def introduce(self):
        education_text = "У меня есть высшее образование." if self.__higher_education else "У меня нет высшего образования."
        print(f"Привет, меня зовут {self.name}. Моя профессия {self.__occupation}. {education_text}")


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, school_class):
        super().__init__(name, birth_date, occupation, higher_education)
        self.school_class = school_class

    def introduce(self):
        super().introduce()
        print(f"Я учился с Амантуром.")


class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        super().introduce()
        print(f"Моё хобби {self.hobby}.")


# Примеры использования
cl1 = Classmate("Иван", "20.02.2000", "студент", True, "11D")
cl1.introduce()

fr1 = Friend("Айбек", "20.02.2000", "студент", True, "футбол")
fr1.introduce()
print(fr1.age)  # пример работы доп. задания