year = input('Введіть свій рік народження -> ')
assert year.isdigit(), f'Ви впевнені що це "{year}" число ?)'
age = 2022 - int(year)

pib = input(
    'Введіть Прізвище Імя по Батькові (через пробіл, з великої літери) -> ')

list = pib.split()
for item in list:
    assert item.istitle(), f'Схоже ви допустились помилки у слові "{item}"'

print(f'Вітаю {pib}, цього року вам буде (або вже є) {age} рочків )))')