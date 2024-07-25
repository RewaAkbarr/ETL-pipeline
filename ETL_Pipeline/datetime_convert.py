from datetime import datetime
import csv
import re

input_file_path = 'data/Data-orders.csv'
output_file_path = 'data/data_baru.csv'

def fix_date_format(date_str):
    # Coba perbaiki format tanggal yang menggunakan titik sebagai pemisah
    if re.match(r'\d{2}/\d{2}\.\d{4}', date_str):
        return datetime.strptime(date_str, '%d/%m.%Y').strftime('%d/%m/%Y')
    return date_str

with open(input_file_path, mode='r', encoding='utf-8') as infile, \
     open(output_file_path, mode='w', encoding='utf-8', newline='') as outfile:
    
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    for row in reader:
        row[0] = fix_date_format(row[0])  # Asumsikan tanggal adalah kolom pertama
        writer.writerow(row)