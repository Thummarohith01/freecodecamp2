import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import data
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Clean data by removing the top 2.5% and bottom 2.5% of page views
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

def draw_line_plot():
    # Create a copy of the dataframe for plotting
    df_line = df.copy()

    # Initialize the matplotlib figure
    fig, ax = plt.subplots(figsize=(14, 7))

    # Plot the line chart
    ax.plot(df_line.index, df_line['value'], color='red', linewidth=1)

    # Set the title and labels
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Save the plot to a file
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Create a copy of the dataframe for plotting
    df_bar = df.copy()

    # Add 'year' and 'month' columns
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()

    # Group by year and month and calculate the mean page views
    df_bar_grouped = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    # Order the months correctly
    months_order = ['January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November', 'December']
    df_bar_grouped = df_bar_grouped[months_order]

    # Initialize the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 8))

    # Plot the bar chart
    df_bar_grouped.plot(kind='bar', ax=ax)

    # Set the title and labels
    ax.set_title('Average Daily Page Views per Month')
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(title='Months', loc='upper left', bbox_to_anchor=(1, 1))

    # Adjust layout to make room for the legend
    plt.tight_layout()

    # Save the plot to a file
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.month_name()
    
    # Ensure the months are ordered correctly
    df_box['month'] = pd.Categorical(df_box['month'], categories=[
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'], ordered=True)

    # Initialize the matplotlib figure with two subplots
    fig, axes = plt.subplots(1, 2, figsize=(20, 10))

    # Year-wise Box Plot (Trend)
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    # Month-wise Box Plot (Seasonality)
    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    # Adjust layout to prevent overlap
    plt.tight_layout()

    # Save the plot to a file
    fig.savefig('box_plot.png')
    return fig

# If you want to test the functions locally, you can uncomment the following lines:
# if __name__ == "__main__":
#     draw_line_plot()
#     draw_bar_plot()
#     draw_box_plot()
