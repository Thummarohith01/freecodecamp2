import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Import the data from medical_examination.csv and assign it to the df variable
df = pd.read_csv('medical_examination.csv')

# 2. Create the overweight column in the df variable
# Calculate BMI and determine overweight status
df['BMI'] = df['weight'] / ((df['height'] / 100) ** 2)
df['overweight'] = df['BMI'].apply(lambda x: 1 if x > 25 else 0)
df = df.drop(columns=['BMI'])  # Drop the BMI column as it's no longer needed

# 3. Normalize data by making 0 always good and 1 always bad.
# Normalize cholesterol and gluc
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

# 4. Draw the Categorical Plot in the draw_cat_plot function
def draw_cat_plot():
    # 4.1 Create a DataFrame for the cat plot using pd.melt with specific features
    df_cat = pd.melt(
        df,
        id_vars=['cardio'],
        value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke']
    )
    
    # 4.2 Group and reformat the data to split it by cardio
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    
    # 4.3 Create a categorical plot using seaborn's catplot
    fig = sns.catplot(
        x='variable',
        y='total',
        hue='value',
        col='cardio',
        data=df_cat,
        kind='bar'
    ).fig
    
    # 4.4 Return the figure for the output
    return fig

# 5. Draw the Heat Map in the draw_heat_map function
def draw_heat_map():
    # 5.1 Clean the data by applying the specified filters
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]
    
    # 5.2 Calculate the correlation matrix
    corr = df_heat.corr()
    
    # 5.3 Generate a mask for the upper triangle
    mask = corr.mask(
        (corr) < 0.3
    )
    mask = corr.where(
        (corr >= 0.3) & (corr <= 1)
    )
    
    # 5.4 Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 10))
    
    # 5.5 Draw the heatmap using seaborn
    sns.heatmap(
        corr,
        mask=None,  # To show all correlations
        annot=True,
        fmt=".1f",
        center=0,
        vmin=-0.1,
        vmax=0.25,
        linewidths=0.5,
        cbar_kws={"shrink": 0.5},
        ax=ax
    )
    
    # 5.6 Return the figure for the output
    return fig

# If you want to test the functions locally, you can use the following code.
# However, according to the instructions, you should not modify the next two lines.
if __name__ == "__main__":
    # Test draw_cat_plot function
    cat_plot = draw_cat_plot()
    cat_plot.savefig('catplot.png')
    
    # Test draw_heat_map function
    heat_map = draw_heat_map()
    heat_map.savefig('heatmap.png')
