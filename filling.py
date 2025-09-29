import csv

# Читаем данные основной таблицы
dataset = {}
with open('dataset.txt', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        id_ = row[0]
        dataset[id_] = row  # сохраняем всю строку

# Читаем данные суммарей
summaries = {}
with open('summaries.txt', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        doc_id = row[0]  # внешний ключ
        summaries[doc_id] = row[1:]  # сохраняем только текстовые колонки

# Создаем объединённый файл
with open('full_dataset.tsv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f, delimiter='\t')
    # Запишем шапку (названия колонок)
    writer.writerow([
        'id','filename','text_dedoc','content_vector','tag','target_summary',
        'lingvo_summary','mt5_summary','mbart_summary','rut5_summary','t5_summary'
    ])
    for id_, row in dataset.items():
        summary_row = summaries.get(id_, ['']*5)  # если нет суммарей — пустые поля
        writer.writerow(row + summary_row)
# C:\Users\try3l\Downloads\Folder\convert_to_utf8.py

# input_file = "C:/Users/try3l/Downloads/Folder/full_dataset.tsv"
# output_file = "C:/Users/try3l/Downloads/Folder/full_dataset_utf8.tsv"

# with open(input_file, "r", encoding="cp1251", errors="replace") as f_in, \
#      open(output_file, "w", encoding="utf-8") as f_out:
#     for line in f_in:
#         f_out.write(line)

# import codecs

# with codecs.open('full_dataset_utf8.tsv', 'r', 'utf-8-sig') as f:
#     content = f.read()

# with codecs.open('full_dataset_fixed.tsv', 'w', 'utf-8') as f:
#     f.write(content)