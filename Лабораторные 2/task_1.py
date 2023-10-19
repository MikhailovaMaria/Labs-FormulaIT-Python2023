money_capital = 20000  # TODO Подушка безопасности
salary = 5000  # TODO Ежемесячная зарплата
spend = 6000  # TODO Траты за первый месяц
increase = 0.05  # TODO Ежемесячный рост цен

month = 0  # TODO Количество месяцев, которое можно протянуть без долгов
while True:
    contrast = spend - salary  # TODO Разница между расходом и ЗП
    if contrast <= money_capital:
        month += 1
        money_capital -= contrast
        spend *= 1 + increase
        continue
    break
print("Количество месяцев, которое можно протянуть без долгов:", month)
