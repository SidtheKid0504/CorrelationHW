import numpy as np
import csv
    
def setup():
    days_present = []
    student_marks = []

    with open('./hwFiles/data/Student Marks vs Days Present.csv') as csv_file:
        data = csv.DictReader(csv_file)
        for row in data:
            days_present.append(float(row["Days Present"]))
            student_marks.append(float(row["Marks In Percentage"]))

    return  {'x': days_present, 'y': student_marks}

def find_correlation(data_src):
    correlation = np.corrcoef(data_src['x'], data_src['y'])
    print(correlation[0][1])

find_correlation(setup())


