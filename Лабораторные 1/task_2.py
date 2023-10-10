# TODO Найдите количество книг, которое можно разместить на дискете
# TODO Информация о дискете
# TODO Информационный объем дискеты в МБ
diskette_capacity_mb = 1.44

# TODO Параметры книги
pages_per_book = 100
lines_per_page = 50
characters_per_line = 25
bytes_per_character = 4  # TODO Байтов на символ

# TODO Размер одной книги в байтах
book_size_bytes = pages_per_book * lines_per_page * characters_per_line * bytes_per_character

# TODO Рассчитать количество книг, которые помещаются на дискету
books_per_diskette = diskette_capacity_mb * 1024 * 1024 // book_size_bytes

# TODO Вывести результат (округленный до целого числа)
print("Количество книг, помещающихся на дискету:", round(books_per_diskette))

