#the user gets lots of options to filter and find out about different rollercoasters
#my data was provided from the public spreadsheets from code.org. you can see mine and more at: https://docs.google.com/spreadsheets/d/1pPFi8LbDhqLAqAs75ayUh6quoBLTEAH0y5aaQSLV9No/edit?gid=0#gid=0
import pandas as pd
data = pd.read_csv("roller.csv")
id = data["id"].tolist()
name = data["Rollercoaster Name"].tolist()
location = data["Amusement Park"].tolist()
city = data["City"].tolist()
country = data["Country"].tolist()
region = data["Region"].tolist()
material = data["Construction Material"].tolist()
height = data["Height"].tolist()
speed = data["Speed"].tolist()
length = data["Length"].tolist()
upsidedown = data["Inversion"].tolist()
upsidedowns_num = data["Number of Inversions"].tolist()
opened = data["Year Opened"].tolist()
filter = []
indexfilter=[]
#set of functions for typical use
def city_finder(x):
    for i in range(len(id)):
        if x in city[i]:
            filter.append(name[i])
            indexfilter.append(i)
    print("here are rollercoasters that met your city requirments")
    print(filter)


def name_finder(x):
    for i in range(len(id)):
        if x in name[i]:
            print(f"data found for search term {x}")
            print(data.loc[i])

def speed_finder(min,max): #x is the slowest y is the fastest
    for i in range(len(id)):
        if speed[i] >= min and speed[i] <= max:
            filter.append(name[i])
            indexfilter.append(i)
    print("here are rollercoasters that met your speed requirments")
    print(filter)


def len_finder(short,long):
    for i in range(len(id)):
        if length[i] >= short and length[i] <= long:
            filter.append(name[i])
            indexfilter.append(i)
    print("here are rollercoasters that met your length requirments")
    print(filter)


def inversion_finder(inversion):
    if inversion == "yes":
        for i in range(len(id)):
            if "Yes" in upsidedown[i]:
                filter.append(name[i])
                indexfilter.append(i)
        print("rollercoasters with inversions")
        print(filter)
    if inversion == "no":
        for i in range(len(id)):
            if "No" in upsidedown[i]:
                filter.append(name[i])
                indexfilter.append(i)
        print("rollercoasters with no inversion")
        print(filter)




def date_finder(younger,older):
    for i in range(len(id)):
        if opened[i] > younger and opened[i] < older:
            filter.append(name[i])
            indexfilter.append(i)
    print("rollercoaster in your range")
    print(filter)
#functions to filter through filtered lists
def city_finderxx(x):
    for i in range(len(filter)):
        y = indexfilter[i]
        if x in city[y]:
            print(name[y])

def speed_finderxx(min,max): #x is the slowest y is the fastest
    for i in range(len(filter)):
        y = indexfilter[i]
        if speed[y] >= min and speed[y] <= max:
            print(name[y])

def len_finderxx(short,long):
    for i in range(len(filter)):
        y = indexfilter[i]
        if length[y] >= short and length[y] <= long:
            print(name[y])

def inversion_finderxx(inversion):
    if inversion == "yes":
        for i in range(len(filter)):
            y = indexfilter[i]
            if "Yes" in upsidedown[y]:
                print(name[y])
    if inversion == "no":
        for i in range(len(filter)):
            y = indexfilter[i]
            if "No" in upsidedown[y]:
                print(name[y])

def date_finderxx(younger,older):
    for i in range(len(filter)):
        y = indexfilter[i]
        if opened[y] > younger and opened[y] < older:
            print(name[y])

while True:
    print("")
    print("detailed search    (1)")
    print("broad serach       (2)")
    print("info               (3)")
    print("quit               (4)")
    print("")
    x = input("")
    if x == "1":
        print("in this mode you can narrow down a rollercoaster through 2 filtering options")
        print("what would you like to filter first")
        print("note: after you use a filter, your next filter will only used items in the previously filterd list")
        print("")
        print("rollercoasters in your city         (1)")
        print("rollercoaters in your speed range   (2)")
        print("rollercoaters in your length range  (3)")
        print("rollercoaters with inversions       (4)")
        print("rollercoaters in you date range     (5)")
        x = input("")
        if x == "1":
            x = input("which cities' rollercoasters do you want to see     ")
            city_finder(x)
            x = 0
        if x == "2":
            min = int(input("how slow are you willing to go?     "))
            max = int(input("how fast do you want to go?     "))
            speed_finder(min,max)
            x = 0

        if x == "3":
            short = int(input("how short do you want it to be?     "))
            long = int(input("how long do you want it to be?     "))
            len_finder(short,long)
            x = 0
            continue

        if x == "4":
            inversion = input("do you want your rollercoaster to have inverions?     ")
            inversion_finder(inversion)
            x = 0

        if x == "5":
            younger = int(input("whats the oldest rollercoaster you want?     "))
            older = int(input("whats the youngest rollercoaster you want?     "))
            date_finder(younger,older)
        x = input("would you like to filter more?     ")
        if x == "no":
            print("")
            print("going back to menu")
            continue
        if x == "yes":
                print("rollercoasters in your city         (1)")
                print("rollercoaters in your speed range   (2)")
                print("rollercoaters in your length range  (3)")
                print("rollercoaters with inversions       (4)")
                print("rollercoaters in you date range     (5)")
                a = input("what else do you want to filter?     ")
                if a == "1":
                    x = input("which cities' rollercoasters do you want to see     ")
                    city_finderxx(x)
                    filter.clear()
                    indexfilter.clear()


                if a == "2":
                    min = int(input("how slow are you willing to go?     "))
                    max = int(input("how fast do you want to go?     "))
                    speed_finderxx(min,max)
                    filter.clear()
                    indexfilter.clear

                if a == "3":
                    short = int(input("how short do you want it to be?     "))
                    long = int(input("how long do you want it to be?     "))
                    len_finderxx(short,long)
                    filter.clear()
                    indexfilter.clear()
                if a == "4":
                    inversion = input("do you want your rollercoaster to have inverions?     ")
                    inversion_finderxx(inversion)
                    filter.clear()
                    indexfilter.clear()
                if a == "5":
                    younger = int(input("whats the oldest rollercoaster you want?     "))
                    older = int(input("whats the youngest rollercoaster you want?     "))
                    date_finderxx(younger,older)
                    filter.clear()
                    indexfilter.clear()

    if x =="2":
        print("rollercoasters in your city         (1)")
        print("rollercoaters in your speed range   (2)")
        print("rollercoaters in your length range  (3)")
        print("rollercoaters with inversions       (4)")
        print("rollercoaters in you date range     (5)")
        print("back to menu                        (6)")
        x = input("")
        if x == "1":
            x = input("which cities' rollercoasters do you want to see     ")
            city_finder(x)
            filter.clear()
            indexfilter.clear()
            x = 0

        if x == "2":
            min = int(input("how slow are you willing to go?     "))
            max = int(input("how fast do you want to go?     "))
            speed_finder(min,max)
            filter.clear()
            indexfilter.clear()
            x = 0

        if x == "3":
            short = int(input("how short do you want it to be?     "))
            long = int(input("how long do you want it to be?     "))
            len_finder(short,long)
            filter.clear()
            indexfilter.clear()
            x = 0

        if x == "4":
            inversion = input("do you want your rollercoaster to have inverions?     ")
            inversion_finder(inversion)
            filter.clear()
            indexfilter.clear()
            x = 0

        if x == "5":
            younger = int(input("whats the oldest rollercoaster you want?     "))
            older = int(input("whats the youngest rollercoaster you want?     "))
            date_finder(younger,older)
            filter.clear()
            indexfilter.clear()
            x = 0
        if x == "6":
            continue

    if x == "3":
        x = input("what rollercoaster do you want to know about?     ")
        name_finder(x)
    if x == "4":
        break




