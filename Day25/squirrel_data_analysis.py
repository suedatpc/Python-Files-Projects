import pandas

data = pandas.read_csv("Day25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray = 0
cinnamon = 0
black = 0

squirrel_colors = data["Primary Fur Color"]

for color in squirrel_colors:
    if color == "Gray":
        gray += 1 
    elif color == "Black":
        black += 1
    elif color == "Cinnamon":
        cinnamon += 1 

color_dict = {
    "color": ["Gray", "Black", "Cinnamon"],
    "count": [gray, black, cinnamon]
}

squirrel_dataframe = pandas.DataFrame(color_dict)
squirrel_dataframe.to_csv("squirrel.csv")
