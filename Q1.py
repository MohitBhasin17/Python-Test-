# Importing the CSV module to handle CSV files
import csv

def read_file(file_name):
    try:
        # Attempting to open the file in read mode
        with open(file_name, 'r') as file:
            csv_reader = csv.reader(file)
             # Iterating over each row in the CSV file
            for row in csv_reader:
                 # Printing each row to the console
                print(row)
    except FileNotFoundError:
          # Handling the case where the file does not exist
        print(f"File '{file_name}' not found.")
    except Exception as e:
          # Handling any other exceptions that may occur
        print(f"An error occurred: {e}")

# Calling the function with the file name 'TEXT.csv'
read_file('TEXT.csv')


#Output
#['1', 'asd']
#['2', 'sdfd']
#['3', 'f']
#['4', 'fdf']
#['5', 'gf']
#['6', 'gg']
#['7', 'h']
#['8', 'hjh']
#['9', 'kj']
#['10', 'fgfg']
