# with open("weather_data.csv") as data_file:
#    data = data_file.readlines()


# import csv
# with open("weather_data.csv") as data_file:
#   data = csv.reader(data_file)
#  temperatures = []
# for row in data:
#    if row[1] != "temp":
#       temperatures.append(int(row[1]))
# print(temperatures)

import pandas
data = pandas.read_csv("weather_data.csv")

data_dict = data.to_dict()

temp_list = data["temp"].to_list()
print(len(temp_list))

