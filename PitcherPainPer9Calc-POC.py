#The One That Actually Calculates It
import csv

def calculate_csv(input_file, output_file):
    with open(input_file, 'r') as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames + ['PPp9_calculated']

        with open(output_file, 'w', newline='') as output:
            writer = csv.DictWriter(output, fieldnames=fieldnames)
            writer.writeheader()

            for row in reader:
                ip = float(row['IP'])
                r = float(row['R'])
                hr = float(row['HR'])
                bb = float(row['BB'])
                hbp = float(row['HBP'])
                bk = float(row['BK'])
                wp = float(row['WP'])

                PPp9_calculated = ((r + hr + (bb*.25) + (hbp*.25) +(bk*.25) + (wp*.25) )/ip)



                row['PPp9_calculated'] = PPp9_calculated

                writer.writerow(row)

print("CSV calculation completed successfully!")

# Usage example
calculate_csv('Yanks2022PROC.csv', 'Yanks2022CALC.csv')