import csv

txt_file = r"/c/Users/Emine/Desktop/convertTXTtoCSV/textfile.txt"
csv_file = r"/c/Users/Emine/Desktop/convertTXTtoCSV/csvfile.csv"

with open(txt_file, 'r') as in_file, open(csv_file, 'w', newline='') as out_file:
    writer = csv.writer(out_file)
    for line in in_file:
        writer.writerow(line.strip().split(' '))

