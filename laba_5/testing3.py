class Name:
    def __init__(self, name, hobby='') -> None:
        if name not in ["Оксана", "Діана", "Петро"]:
            raise ValueError("Дозволені імена: Оксана, Діана")
        if hobby == '':
            raise ValueError("Хобі не може бути пустим")

        self.name = name
        self.hobby = hobby


a = Name("Діана", "Спатки, їсти, лежати в ліжку, читати книзі")
b = Name("Діана")