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

    def myfunc(year):
        return slope * (year) + intercept
    years = range(1880, 2051)
    predicted_sea_levels = [myfunc(year) for year in years]


    plt.plot(years, predicted_sea_levels, color='red')
    plt.show()
    


    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    slope2, intercept2, r2, p2, std_err2 = linregress(df_recent['Year'] , df_recent["CSIRO Adjusted Sea Level"])
    
    def myfunc1(years1):
        return slope2 * (years1) + intercept2
    
    years2 = range(2000, 2051)
    predicted_sea_levels1 = [myfunc1(years1) for years1 in years2]
    plt.plot(years2, predicted_sea_levels1, color='blue')
    plt.show()


    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()