import csv

input_file_path = 'data/Data-order.csv'
output_file_path = 'data/data_baru.csv'

# Fungsi untuk mengganti format numerik
def replace_numeric_format(value):
    return value.replace('.', '').replace(',', '.')

with open(input_file_path, mode='r', encoding='utf-8') as infile, \
     open(output_file_path, mode='w', encoding='utf-8', newline='') as outfile:
    
    reader = csv.reader(infile, delimiter=';')
    writer = csv.writer(outfile, delimiter=',')
    
    for row in reader:
        processed_row = []
        for item in row:
            # Cek apakah item adalah numerik dengan format "1.000,00"
            if item.replace('.', '').replace(',', '').isdigit():
                processed_item = replace_numeric_format(item)
            else:
                processed_item = item
            processed_row.append(processed_item)
        writer.writerow(processed_row)