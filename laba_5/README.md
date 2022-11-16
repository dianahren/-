# Звіт до роботи Lab5

## Тема: Тестування

---

### Виконання роботи:

### Перевірка assert

- Зроблено програму з тестами assert:

```py
year = input('Введіть свій рік народження -> ')
assert year.isdigit(), f'Ви впевнені що це "{year}" число ?)'
age = 2022 - int(year)

pib = input(
    'Введіть Прізвище Імя по Батькові (через пробіл, з великої літери) -> ')

list = pib.split()
for item in list:
    assert item.istitle(), f'Схоже ви допустились помилки у слові "{item}"'

print(f'Вітаю {pib}, цього року вам буде (або вже є) {age} рочків )))')
```

Ось що буде виводитись, якщо написати все правильно:

```
Введіть свій рік народження -> 2003
Введіть Прізвище Імя по Батькові (через пробіл, з великої літери) -> Грень Діана Василівна
Грень Діана Василівна, в цьому році вам буде (або вже є) 19 років.
```

Якщо ввести не число (типу int) то перша перевірка видасть таку помилку:

```
Введіть свій рік народження -> текст)
AssertionError: Ви впевнені що це "текст)" число ?)
```

Якщо ввести правильно число, але ввести слово з маленької літери:

```
Введіть свій рік народження -> 200-
Введіть Прізвище Імя по Батькові (через пробіл, з великої літери) -> юлія
AssertionError: Схоже ви допустились помилки у слові "юлія"
```

<span style='color: rgba(255, 255, 255, 0.2)'>Юлія пишеться з великої<span>





## Юніт тести

- - Введено і запущено код, але ось що получилось:
```py
class Figure:
    FIGURES = ["квадрат", "прямокутник", "трикутник"]
    COLORS = ["red", "green", "blue"]

    def __init__(self, type, length, color='0') -> None:
        assert length > 0, "Довжина має бути більшою за 0!"
        assert type in self.FIGURES, "Дозволені фігури: квадрат, прямокутник, трикутник"
        assert color in self.COLORS, "Дозволені кольори: red, green, blue"
        self.type = type
        self.length = length
        self.color = color

    @property
    def get_figure_type(self):
        return self.type

    @property
    def get_figure_length(self):
        return self.type  # робимо помилку

    @property
    def get_figure_color(self):
        return self.color
```

Test_app.py

```py
import unittest
from random import choice, randint

from app import Figure  # назва файлу з нашим класом повинна бути app.py


class TestFigure(unittest.TestCase):
    def setUpClass():
        """Виконається лише раз на початку тестів
        """
        pass

    def setUp(self) -> None:
        """Виконується кожного разу коли запускається тест
        """
        self.figure = choice(Figure.FIGURES)
        self.length = randint(1, 10)
        self.color = choice(Figure.COLORS)
        self.obj = Figure(self.figure, self.length, self.color)
        return super().setUp()

    def tearDown(self) -> None:
        del self.obj
        return super().tearDown()

    def test_figure_type(self):
        print(
            f"Тестуємо вивід, має бути: {self.figure} == {self.obj.get_figure_type}")
        self.assertEqual(self.figure, self.obj.get_figure_type,
                         "Властивість get_figure_type повертає непривильну фігуру!")

    def test_figure_lengh(self):
        self.assertEqual(self.length, self.obj.get_figure_length,
                         "Властивість get_figure_length повертає непривильну довжину!")

    def test_figure_color(self):
        self.assertEqual(self.color, self.obj.get_figure_color,
                         "Властивість get_figure_length повертає непривильний колір!")

    def test_obj(self):
        with self.assertRaises(AssertionError):
            # Спробуємо створити обєкт з недозволеними параметрими, в нас має бути помилка AssertionError
            Figure("коло", 1)


if __name__ == '__main__':
    # unittest.main(verbosity=2) щоб був більш детальний вивід
    unittest.main(verbosity=2)

```

І ось що вивелось у консоль при запуску тестів:

```
test_figure_color (__main__.TestFigure) ... ok
test_figure_lengh (__main__.TestFigure) ... FAIL
test_figure_type (__main__.TestFigure) ... Тестуємо вивід, має бути: прямокутник == прямокутник
ok
test_obj (__main__.TestFigure) ... ok

======================================================================
FAIL: test_figure_lengh (__main__.TestFigure)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "D:\Labs\Labs 3.1\ООП\github\OOP\Lab5\Test_app.py", line 33, in test_figure_lengh
    self.assertEqual(self.length, self.obj.get_figure_length,
AssertionError: 5 != 'прямокутник' : Властивість get_figure_length повертає непривильну довжину!

----------------------------------------------------------------------
Ran 4 tests in 0.002s

FAILED (failures=1)
```

## Юніт тести з використання бібліотеки PyTest

- Я створив віртуальне середовище та інсталював туди бібліотеку `PyTest`
  До арр.ру додав таку функцію:

```py
def test_app_triangle():
    """Test if we create triangle figure.
    """
    fig = "трикутник"
    len = 4
    col = 'blue'

    triangle = Figure(fig, len, col)
    assert triangle.type == fig, f"Фігура має бути {fig}"
```

Ось що вивів `PyTest`:

```
================== test session starts ==================
platform win32 -- Python 3.10.6, pytest-7.1.3, pluggy-1.0.0
rootdir: D:\Labs\Labs 3.1\ООП\github\OOP\Lab5
collected 1 item

app.py .              [100%]

================== 1 passed in 0.02s ==================
```

А це вивід вісля запуску `Test_app.py`:

```
================== test session starts ==================
platform win32 -- Python 3.10.6, pytest-7.1.3, pluggy-1.0.0
rootdir: D:\Labs\Labs 3.1\ООП\github\OOP\Lab5
collected 4 items

Test_app.py .F..   [100%]

================== FAILURES ==================
__________________ TestFigure.test_figure_lengh __________________

self = <Test_app.TestFigure testMethod=test_figure_lengh>

    def test_figure_lengh(self):
>       self.assertEqual(self.length, self.obj.get_figure_length,
                         "Властивість get_figure_length повертає непривильну довжину!")
E       AssertionError: 4 != 'квадрат' : Властивість get_figure_length повертає непривильну довжину!

Test_app.py:33: AssertionError
================== short test summary info ==================
FAILED Test_app.py::TestFigure::test_figure_lengh - AssertionError: 4 != 'квадрат' : Властивість get_figure_length повертає непривильну довжину!
================== 1 failed, 3 passed in 0.10s ==================
```

## Візуалізація результатів та покриття коду Coverage (pytest-cov)

- Я встановив плагін `PyTest-Cov` та `Coverage`, щоб потестити який з тестів краще тестить )
  Вивід трошки гарніший. В таблиці гарно виглядає, але щось мало інформації про помилку.

```
Name     Stmts   Miss  Cover
----------------------------
app.py      25      5    80%
----------------------------
TOTAL       25      5    80%
```


### Висновок:

- :question: Що зроблено в роботі; :wavy_dash: тестування
- :question: Чи досягнуто мети роботи; :wavy_dash: так
- :question: Які нові знання отримано; :wavy_dash: отримано знання про тестування
- :question: Чи вдалось відповісти на всі питання задані в ході роботи; :wavy_dash: так
- :question: Чи вдалося виконати всі завдання; :wavy_dash: думаю так
- :question: Чи виникли складності у виконанні завдання; :wavy_dash: ні
- :question: Чи подобається такий формат здачі роботи (Feedback); :wavy_dash: так
- :question: Побажання для покращення (Suggestions); :wavy_dash: все добре