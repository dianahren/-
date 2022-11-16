class Figure:
    def __init__(self, type, length) -> None:
        assert length > 0, "Довжина має бути більшою за 0!"
        assert type in ["квадрат", "прямокутник",
                        "трикутник"], "Дозволені фігури: квадрат, прямокутник, трикутник"

        self.type = type
        self.length = length

    def print_figure(self):
        return f'Фігура {self.type} з cтороною {self.length}'


try:
    figure1 = Figure("квадрат", 2)
    print(f'Фігура 1 - {figure1.print_figure()}')
except AssertionError as err:
    print(f'Фігура 1 - {err}')

try:
    figure2 = Figure("прямокутник", 0)
    print(f'Фігура 2 - {figure2.print_figure()}')
except AssertionError as err:
    print(f'Фігура 2 - {err}')

try:
    figure3 = Figure("трикутник", -42)
    print(f'Фігура 3 - {figure3.print_figure()}')
except AssertionError as err:
    print(f'Фігура 3 - {err}')

try:
    figure4 = Figure("трикутник", 15)
    print(f'Фігура 4 - {figure4.print_figure()}')
except AssertionError as err:
    print(f'Фігура 4 - {err}')

try:
    figure5 = Figure("трапеція", 100)
    print(f'Фігура 5 - {figure5.print_figure()}')
except AssertionError as err:
    print(f'Фігура 5 - {err}')