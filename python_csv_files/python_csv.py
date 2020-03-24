# import csv
# with open("user_details.csv", newline = '') as csvfile:
#     csvreader = csv.reader(csvfile, delimiter = ",")

    # print(csvreader)

    # for row in csvreader:
    #     for column in csvreader:
    #
    #         print(row)
    #         print(column)
#print last row
    # for row in csvreader:
    #     print(row[-1])

    # iterable_csv = iter(csvreader)
    # next(iterable_csv) # skip to next line
    # for row in iterable_csv:
    #     next(iterable_csv)
    #     print(row[-1])


#append new data
import csv
def transform_user_details(csv_file_name):
    new_user_data = []
    with open(csv_file_name, newline='') as csvfile:
        user_details_csv = csv.reader(csvfile, delimiter=",")
        for user in user_details_csv:
            transformation = []
            transformation.append(user[1])
            transformation.append(user[2])
            transformation.append(user[-1])
            new_user_data.append(transformation)
    return new_user_data

print(transform_user_details("user_details.csv"))


#create a csv file nd copy info for user_details.csv to new_user_details.csv
def create_new_user_data_csv(old_user_data_file="user_details.csv", new_file_name='new_user_data.csv'):
    new_user_data = transform_user_details(create_new_user_data_csv)
    new_file = open(new_file_name, 'w')
    with new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerows(new_user_data)
create_new_user_data_csv()

