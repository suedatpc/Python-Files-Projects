# import csv

# with open("Day25/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(row[1])

#     print(temperatures)

import pandas

data = pandas.read_csv("Day25/weather_data.csv")
temp_list = data["temp"].to_list()

# average = sum(temp_list) / len(temp_list)
# print(average)
print(data["temp"].mean())

print(data["temp"].max())

#get data in columns
print(data.condition)

#get data in rows
print(data[data.day == "Tuesday"])
print(data[data.temp == data.temp.max()])
monday = data[data.day == "Monday"]
print(monday.temp)

#create a dataframe
data_dic = {
    "students": ["Amy", "Joe", "Angela"],
    "scores": ["76", "23", "56"]
}
data = pandas.DataFrame(data_dic)
print(data)
#data.to_csv("new_data.csv")