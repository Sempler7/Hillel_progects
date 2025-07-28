import csv

# Пути к исходным файлам
file1 = "random.csv"
file2 = "random-michaels.csv"
result_file = "result_erenkov.csv"

# Чтение строк из обоих файлов
def read_csv_rows(filename):
    with open(filename, newline='', encoding='utf-8') as f:
        return [tuple(row) for row in csv.reader(f)]

rows1 = read_csv_rows(file1)
rows2 = read_csv_rows(file2)

# Объединение и удаление дубликатов
unique_rows = list(set(rows1 + rows2))

# Запись результата в новый CSV
with open(result_file, "w", newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(unique_rows)

print(f"✅ Готово! Уникальные строки записаны в: {result_file}")