import csv
import pandas as pd

data = pd.read_csv("weather_data.csv")

# # data_dict = data.to_dict()
# # print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# # The same method.
# avg_temp = sum(temp_list)/len(temp_list)
# print(avg_temp)
# mean_temp = data["temp"].mean()
# print(mean_temp)
#
# # Maximum value
# max_temp = data["temp"].max()
# print(max_temp)
#
# # The same method
# print(data["condition"])
# print(data.condition, "\n")
#
# # Get data in row
# print(data[data.temp == "Monday"], "\n")
#
# # The day which the temperature was "max"
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
#
# # Converting from celcius to farenheit
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(f"Temperature in Celcius:\t\t{monday_temp}\nTemperature in Farenheit:\t{monday_temp_F}")



