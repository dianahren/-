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