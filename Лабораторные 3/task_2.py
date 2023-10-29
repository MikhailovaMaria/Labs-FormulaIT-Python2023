def find_common_participants(group1, group2, delimiter=','):
    # Разделить строки на списки, используя указанный разделитель
    first_group = group1.split(delimiter)
    second_group = group2.split(delimiter)

    # Найти общих участников
    common_participants = list(set(first_group) & set(second_group))

    # Отсортировать список общих участников в алфавитном порядке
    common_participants.sort()

    return common_participants

# Пример использования функции с вашими данными


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
common_participants_result = find_common_participants(
    participants_first_group, participants_second_group, delimiter='|')
print(common_participants_result)
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
