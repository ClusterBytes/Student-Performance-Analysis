import pandas as pd

# Define the input CSV file path and column order
input_file_path = "students.csv"

# Read the input CSV file and reorder the columns
df = pd.read_csv(input_file_path)
column_order= df.columns
df = df[column_order]

# Define the output CSV file path and columns to keep
output_file_path = "reordered.csv"
columns_to_keep = ["Year", "Dept", "S1", "S2", "S3", "S4", "S5", "S6", "S7", "A1", "A2", "A3", "A4", "A5", "A6", "A7", "I1", "I2", "I3", "I4", "I5", "I6", "I7", "G1", "G2", "G3", "G4", "G5", "G6", "G7"]

# Write the reordered CSV data to the output file, keeping only the specified columns
df.to_csv(output_file_path, columns=columns_to_keep, index=False)
