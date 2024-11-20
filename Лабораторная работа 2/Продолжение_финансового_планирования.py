salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
final = [spend - salary]
current_spend = spend
mon = months
for mon in range(months - 1):
    current_spend *= (1 + increase)
    final.append(current_spend - salary)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(sum(final)))
