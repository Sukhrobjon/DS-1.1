import csv
databank, databank_women, databank_women_survived = list(), list(), list()

# INDEX FOR SEX: 4
# INDEX FOR SURVIVORS: 1
PATH = './titanic.csv'
with open(PATH, "r") as csv_file:
    reader = csv.reader(csv_file, delimiter=",")
    for line in reader:
        databank.append(line)

# FIRST STEP: Filter original data and select for women
for index in range(1, len(databank)):
    if databank[index][4] == "female":
        databank_women.append(databank[index])

# SECOND STEP: Filter women data and select for survivors
for index in range(len(databank_women)):
    if databank_women[index][1] == "1":
        databank_women_survived.append(databank_women[index])

# THIRD STEP: Get length of surviving women data
print("SURVIVING WOMEN: ", len(databank_women_survived))
