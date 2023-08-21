import numpy as np 
import pandas as pd
import matplotlib as mlp
import matplotlib.pyplot as plt



metro_data = pd.read_csv('metro_countries_total.csv')
metro_data.head(10)
metro_data_city = pd.read_csv('metro_countries_cities.csv')
metro_data_process = pd.read_csv('metro_countries_in_progress.csv')



length = metro_data.sort_values('length',ascending=False)
number_st = metro_data.sort_values('stations',ascending=False)
an_ride = metro_data.sort_values('annual_ridership_mill',ascending=False)
system = metro_data.sort_values('systems',ascending=False)
lines = metro_data.sort_values('lines',ascending=False)


import plotly
import plotly.express as px

fig = px.choropleth(length,
                    locations='country',
                    locationmode='country names',
                    color='length', 
                    hover_name='country',
                    hover_data=['length'],
                    title = 'Length of metro per country',
                    color_continuous_scale='greens'
                   )

# Adjusting map, legend, title placement
fig.update_layout(
    autosize=True,
    template='seaborn',
    paper_bgcolor="rgb(255, 255, 255)",
    legend=dict(
        orientation="v",
        yanchor="auto",
        y=1.02,
        xanchor="right",
        x=1
))
 
fig.show()


fig2 = px.choropleth(number_st,
                    locations='country',
                    locationmode='country names',
                    color='annual_ridership_mill', 
                    hover_name='country',
                    hover_data=['annual_ridership_mill'],
                    title = 'Annual Ridership per country',
                    color_continuous_scale='greens'
                   )



# Adjusting map, legend, title placement
fig2.update_layout(
    autosize=True,
    template='seaborn',
    paper_bgcolor="rgb(255, 255, 255)",
    legend=dict(
        orientation="v",
        yanchor="auto",
        y=1.02,
        xanchor="right",
        x=1
))
 
fig2.show()


fig3 = px.choropleth(number_st,
                    locations='country',
                    locationmode='country names',
                    color='stations', 
                    hover_name='country',
                    hover_data=['stations'],
                    title = 'Number of metro station per country',
                    color_continuous_scale='Greens'
                   )



# Adjusting map, legend, title placement
fig3.update_layout(
    autosize=True,
    template='seaborn',
    paper_bgcolor="rgb(255, 255, 255)",
    legend=dict(
        orientation="v",
        yanchor="auto",
        y=1.02,
        xanchor="right",
        x=1
))
 
fig3.show()



fig4 = px.choropleth(number_st,
                    locations='country',
                    locationmode='country names',
                    color='systems', 
                    hover_name='country',
                    hover_data=['systems'],
                    title = 'Number of metro systems per country',
                    color_continuous_scale='Greens'
                   )



# Adjusting map, legend, title placement
fig4.update_layout(
    autosize=True,
    template='seaborn',
    paper_bgcolor="rgb(255, 255, 255)",
    legend=dict(
        orientation="v",
        yanchor="auto",
        y=1.02,
        xanchor="right",
        x=1
))
 
fig4.show()




fig5 = px.choropleth(number_st,
                    locations='country',
                    locationmode='country names',
                    color='lines', 
                    hover_name='country',
                    hover_data=['lines'],
                    title = 'Number of metro lines per country',
                    color_continuous_scale='Greens'
                   )



# Adjusting map, legend, title placement
fig5.update_layout(
    autosize=True,
    template='seaborn',
    paper_bgcolor="rgb(255, 255, 255)",
    legend=dict(
        orientation="v",
        yanchor="auto",
        y=1.02,
        xanchor="right",
        x=1
))



import matplotlib.pyplot as plt

# Assuming you have the metro_data DataFrame and the 'country' column is the index
metro_data.set_index('country', inplace=True)

# Sorting the data by 'stations'
sorted_data = metro_data.sort_values(by='stations', ascending=False).head(10)

plt.figure(figsize=(12, 8))

# Creating the horizontal bar plot
ax = sorted_data['stations'].plot(kind='barh', color='g')

# Adding country names as ticks
ax.set_yticks(range(len(sorted_data)))  # Set the tick positions
ax.set_yticklabels(sorted_data.index)   # Set the tick labels (country names)

plt.xlabel('Number of Stations')
plt.ylabel('Country')
plt.title('Top 10 Countries by the Highest Number of Metro Stations')

plt.show()




metro_data[['region','stations']].groupby('region').sum().sort_values('stations',ascending = False).plot(kind = 'bar', 
        rot = 45, color = 'g', figsize = (12,8), legend = 0)
plt.title('Amount of metro stations per each region')
plt.xlabel('Region')
plt.ylabel('Amount of stations')
plt.show()




metro_data_city.set_index('name', inplace=True)
metro_data_city[['region','stations']].sort_values('stations',ascending = False).head(10).plot(kind = 'bar', 
        rot = 45, color = 'g', figsize = (12,8), legend = 0)
plt.title('Amount of metro stations per each city(top 10)')
plt.xlabel('City')
plt.ylabel('Amount of stations')
plt.show()




metro_data[['region','annual_ridership_mill']].sort_values('annual_ridership_mill',ascending = False).head(10).plot(kind = 'bar', 
        rot = 45, color = 'g', figsize = (12,8), legend = 0)
plt.title('The most congestion country')
plt.xlabel('Country')
plt.ylabel('Average annual ridership in mill')
plt.show()



metro_data_city[['region','annual_ridership_mill']].sort_values('annual_ridership_mill',ascending = False).head(10).plot(kind = 'bar', 
        rot = 45, color = 'g', figsize = (12,8), legend = 0)
plt.title('The most congestion City')
plt.xlabel('Name')
plt.ylabel('Average annual ridership in mill')
plt.show()



metro_data_process.groupby('region').count()['city'].plot(kind = 'barh', figsize = (12,8), color = 'g')
plt.ylabel('Region')
plt.xlabel('Projects in progress')
plt.title('Current metro project for each region')
plt.show()



metro_data_process.groupby('country').count()['city'].plot(kind = 'barh', figsize = (12,8), color = 'g')
plt.ylabel('Region')
plt.xlabel('Projects in progress')
plt.title('Current metro project for each Country')
plt.show()






