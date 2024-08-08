import csv

def getSKUcodes(file):
    file = open(file, "r")
    data = list(csv.reader(file, delimiter="|"))
    file.close()
    return data