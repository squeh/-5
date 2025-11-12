def convert_usd_to_rub(amount_usd):
  '''
Конвертирует сумму в долларах в рубли по установленному курсу.
Args:
  
  '''
  USD_TO_RUB = 95.5
  amount_rub = amount_usd * USD_TO_RUB
  return amount_rub
amount_usd = float(input("Введите количество долларов: "))
print(convert_usd_to_rub(amount_usd))
