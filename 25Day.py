# with open("weather_data.csv") as data_file:
#     data=data_file.readlines()
#     print(data)

# import csv
# with open("weather_data.csv") as data_file:
#     data= csv.reader(data_file)
#     temperatures=[]
#     for row in data:
#         if row[1]!="temp":
#          temperatures.append(int(row[1]))
        
#     print(temperatures)

# import pandas
# data=pandas.read_csv("weather_data.csv")


# avg=sum(data["temp"])/len(data["temp"])
# print(avg)
# print(data["temp"].mean())
# print(data[data.day=="Monday"])
# print(data[data.temp==data.temp.max()])
# monday=data[data.day=="Monday"]
# print(monday.condition)
# data.to_excel("new_data.xlsx", index=False)
import turtle

screen= turtle.Screen()
screen.title("U.S. States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


screen.exitonclick()
