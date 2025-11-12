TAX_RATE = 0.13

income = float(input("Введите свой годовой доход: "))

def tax_rate(income, tax, sum_na_arm, TAX_RATE):
  '''
  Вычисляет сумму рассчитанного налога и Сумму "На руки" после вычета налога

  Args:
    income (float): Годовой запас пользователя калькулятора

    '''

tax = income * TAX_RATE
sum_na_arm = income -  tax

print(f"""Общая сумма дохода: {f"{round(income, 2):,}".replace(",","")}руб.
Сумма рассчитанного налога: {f"{round(tax, 2):,}".replace(",","")}руб.
Сумма "На руки" после вычета налога: {f"{round(sum_na_arm, 2):,}".replace(",","")}руб. """)
