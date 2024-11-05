list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]
all_players = len(list_players)
middle_index = all_players // 2

first_team = list_players[:middle_index]
second_team = list_players[middle_index:]

print("Первая команда", first_team)
print("Вторая команда", second_team)
