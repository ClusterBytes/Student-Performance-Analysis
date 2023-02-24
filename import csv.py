import csv

with open('students.csv', 'w', newline='') as file:
     writer = csv.writer(file)
     
     writer.writerow(["Reg_No", "Year", "Dept","S1","A1","I1","G1","S2","A2","I2","G2","S3","A3","I3","G3","S4","A4","I4","G4","S5","A5","I5","G5","S6","A6","I6","G6","S7","A7","I7","G7"])
     writer.writerow(["KSD15CS001",2015,"CSE","BE10105",85,62,"F","BE103",93,56,"F","BE110",86.6,46,"F","CS110",89,45,"P","CY100",85.4,76,"F","CY110",100,89,"A+","EC100",75,66,"F"])
     writer.writerow(["KSD15CS002",2015,"CSE","BE10105",90,80,"F","BE103",93,80,"B+","BE110",100,78,"F","CS110",100,69,"B","CY100",89.5,82,"B","CY110",100,97,"S","EC100",89.29,78,"B"])

with open('students.csv', 'r') as infile, open('reordered.csv', 'a') as outfile:
    # output dict needs a list for new column ordering
    fieldnames = ["Reg_No", "Year", "Dept","S1","A1","I1","S2","A2","I2","S3","A3","I3","S4","A4","I4","S5","A5","I5","S6","A6","I6","S7","A7","I7","G1","G2","G3","G4","G5","G6","G7"]
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    # reorder the header first
    writer.writeheader()
    for row in csv.DictReader(infile):
        # writes the reordered rows to the new file
        writer.writerow(row)