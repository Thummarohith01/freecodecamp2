import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Import data
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data')

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(1880, 2051))
    sea_level_fit = slope * years_extended + intercept
    plt.plot(years_extended, sea_level_fit, color='red', label='Best Fit Line (All Data)')

    # Create second line of best fit for data from year 2000 onward
    df_2000 = df[df['Year'] >= 2000]
    slope_2000, intercept_2000, r_value_2000, p_value_2000, std_err_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    sea_level_fit_2000 = slope_2000 * years_extended + intercept_2000
    plt.plot(years_extended, sea_level_fit_2000, color='green', label='Best Fit Line (2000 Onwards)')

    # Labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save the figure
    plt.savefig('sea_level_plot.png')
    plt.show()

# Call the function to draw the plot
draw_plot()
