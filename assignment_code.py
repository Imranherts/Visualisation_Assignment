import pandas as pd
import matplotlib.pyplot as plt


def read_file(file_name):
    """
    Reads the file corresponding to the file_name
    """
    data = pd.read_excel(file_name)
    return data

def plot_no_of_users():
    """
    This function plots a line graph for the Users of Microsoft Teams for 
    the years 2017 - 2022
    """
    plt.figure()
    plt.plot(microsoft["Year"], microsoft["Users (mm)"])
    plt.title("Users for Microsoft Teams (2017 - 2022)")
    plt.xlabel("Year")
    plt.ylabel("Users (mm)")
    plt.savefig("Users for Microsoft Teams")
    plt.show()
 
def plot_inflation_rate():
    """
    This function plots a bar graph for the share of respondents for 
    different collaboration tools
    """
    plt.figure()
    plt.bar(collab_tools["Characteristic"], collab_tools["Share of respondents"]*100)
    plt.xlabel("Tools")
    plt.ylabel("Share of respondents")
    plt.title("Collaboration tool used for remote work")
    plt.savefig("Collaboration tool for remote work")
    plt.show()

def plot_southamerican_population():
    """
    This function produces a pie chart for the South American Population contribution 
    for the year 2022 
    """
    plt.figure(figsize = (9 , 9))
    plt.pie(population["pop2022"])
    plt.legend(population['country'], loc = "best")
    plt.title("South American Population Constituents (2022)")
    plt.savefig("Population Constituents")
    plt.show()

#Read the data from the downloaded files using pandas 
collab_tools = read_file("Social_Media.xlsx")
population = read_file("sa_population.xlsx")
microsoft = read_file("Microsoft.xlsx")

#Call the different functions for plotting respective graphs
plot_no_of_users()
plot_inflation_rate()
plot_southamerican_population()