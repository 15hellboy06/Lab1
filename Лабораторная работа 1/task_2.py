# TODO Найдите количество книг, которое можно разместить на дискете
pages = 100
lines_per_page = 50
symbols_per_row = 25
bytes_per_symbol = 4

disk_size_bytes = 1.44 * 1024 * 1024

book_size_bytes = pages * lines_per_page * symbols_per_row * bytes_per_symbol

books_on_disk = disk_size_bytes // book_size_bytes
books_on_disk = round(books_on_disk)

print("Количество книг, помещающихся на дискету:", books_on_disk)
