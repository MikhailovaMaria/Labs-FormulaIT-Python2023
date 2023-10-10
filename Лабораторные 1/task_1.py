numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
specify_missing_item = 4

sum_numbers = sum(numbers[:specify_missing_item]) + sum(numbers[specify_missing_item+1:])

count_numbers = len(numbers)
average_value = sum_numbers / count_numbers   # TODO Среднее арифметическое
numbers[specify_missing_item] = average_value
print("Измененный список:", numbers)
