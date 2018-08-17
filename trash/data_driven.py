import csv
# #----------------------------------------------------------------------
# def csv_dict_reader(file_obj):
#     """
#     Read a CSV file using csv.DictReader
#     """
#     reader = csv.DictReader(file_obj, delimiter=',')
#     for line in reader:
#         print(line["first_name"]),
#         print(line["last_name"])
# #----------------------------------------------------------------------
# if __name__ == "__main__":
#     with open("data.csv") as f_obj:
#         csv_dict_reader(f_obj)


input_file = csv.DictReader(open("people.csv"))

max_age = None
oldest_person = None
for row in input_file:
    age = int(row["age"])
    if max_age == None or max_age < age:
        max_age = age
        oldest_person = row["name"]

if max_age != None:
    print("The oldest person is %s, who is %d years old." % (oldest_person, max_age))
else:
    print("The file does not contain any people.")

