per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input("Введите сумму вклада: "))
deposit = []
deposit.append(money * per_cent.get('ТКБ')/100.0)
deposit.append(money * per_cent.get('СКБ')/100.0)
deposit.append(money * per_cent.get('ВТБ')/100.0)
deposit.append(money * per_cent.get('СБЕР')/100.0)

print('Накопленные за год средства в каждом из банков: ', list(map(int, deposit)))

print('Максимальная сумма, которую вы можете заработать: ', max(deposit))