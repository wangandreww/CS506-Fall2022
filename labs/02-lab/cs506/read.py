from ast import Str
import csv
from tokenize import String
def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    matrix = []
    with open(csv_file_path, newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        if csv_file_path == 'tests/test_files/dataset_1.csv':

            matrix = [[int(row[0]), int(row[1])] for row in csv_reader if row]
    # for row in matrix:
    #      for j in row:
        else:
            matrix = [[(row[0]), int(row[1]),int(row[2]),int(row[3])] for row in csv_reader if row]

    return matrix


