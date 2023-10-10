list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]
total_players = len(list_players)  # TODO Разделите участников на две команды и определим общее количество игроков
middle_index = total_players // 2  # TODO Разделите игроков на две равные команды
team1 = list_players[:middle_index]
team2 = list_players[middle_index:]

print(team1)  # TODO Выведите каждую команду на отдельной строке
print(team2)
