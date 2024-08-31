#Handle missing values in the "total_bedrooms" column by filling them with the median value of that column.

import csv 
import statistics

#Specify the path of the CSV file
file_root = r'C:\\Users\\eim95\\Documents\\Trabajo\\Papeleo_de_empresas\\Pepsico\\Business_Case\\BusinessCaseJrDataEngineerHousing-EUGENIA-IBARRA.csv' 

#List to store CSV file data
data = []
#List to store the values in the total_bedrooms column
column_bed = []
#Index of the modified rows
mod_rows = []

#Open the CSV file in read mode ('r')
with open(file_root, 'r', newline='', encoding='UTF-8') as file_csv:
    #Create a CSV reader
    csv_reader = csv.reader(file_csv)
    #Read all rows from the CSV and store them in a list
    data = list(csv_reader)

#Find the index in the 'total_bedrooms' column
header_row = data[0]

try:
    total_bedrooms_index = header_row.index('total_bedrooms')
except ValueError:
    print("Error: 'total_bedrooms' was not found.")
    exit()

#Iterates over the data to calculate the median and replace the values
for i, row in enumerate(data[1:], start=1):
    try:
        if len(row) > total_bedrooms_index:
            val = float(row[total_bedrooms_index])
            if val == 0 or val == '':
                #Stores the row index and value of 'total_bedrooms'
                column_bed.append((i, 0))
            else:
                #Stores the row index and value of 'total_bedrooms'
                column_bed.append((i, val)) 
        else:
            print(f"Error: Row {i+1} has fewer items than expected.")
    except ValueError:
        #Handles invalid (non-numeric) values
        print(f"Error: Non-numeric value in a row {i+1}. Replacing with the median")
        # Add the index of the row with a dummy value (0) to ensure that it is replaced
        column_bed.append((i, 0))

#Extracts only the values of 'total_bedrooms' to calculate the median
valores = [valor for indice, valor in column_bed if valor != 0] 

#Calculate the median of the values in columna_bed   
median = statistics.median(valores)

#Check for empty or zero-equal values and replace with the median
val_replaced = False

for i, valor in column_bed:
    if valor == 0 or valor == '':
        try:
            #Converts median to chain before replacing
            data[i][total_bedrooms_index] = str(median) 
            #Stores the index of the modified rows
            mod_rows.append(i)  
            val_replaced = True
        except IndexError:
            print(f"Error: Index out of rank in row {i+1}.")

#When values were overridden, print a message
if val_replaced:
    print(f"Empty values or values equal to 0 were replaced by the median: {median}")
else:
    print(f"No empty values or values equal to 0 were found. The median is: {median}")

#Write the changed data back to the CSV file
with open(file_root, 'w', newline='', encoding='UTF-8') as file_csv:
    csv_writer = csv.writer(file_csv)
    csv_writer.writerows(data)


