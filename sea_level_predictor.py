import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"]) 
    


    # Create first line of best fit
    slope, intercept, r, p, std_err = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])

    def myfunc(df):
        return slope * (df) + intercept

    mymodel = list(map(myfunc, df["Year"]))


    plt.plot(df["Year"], mymodel)
    plt.show()



    # Create second line of best fit


    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()