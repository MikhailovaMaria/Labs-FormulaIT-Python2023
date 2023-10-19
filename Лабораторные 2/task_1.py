money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

month = 0  # Количество месяцев, которое можно протянуть без долгов
while True:
    contrast = spend - salary  # Разница между расходом и ЗП
    if contrast <= money_capital:
        month += 1
        money_capital -= contrast
        spend *= 1 + increase
        continue
    break
print("Количество месяцев, которое можно протянуть без долгов:", month)
