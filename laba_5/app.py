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


def test_app_triangle():
    """Test if we create triangle figure.
    """
    fig = "трикутник"
    len = 4
    col = 'blue'

    triangle = Figure(fig, len, col)
    assert triangle.type == fig, f"Фігура має бути {fig}"