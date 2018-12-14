# importing libraries
from plotly.offline import plot
import plotly.graph_objs as go
import pandas as pd

# reading data from csv file
df = pd.read_csv('./csv/airport-codes.csv')

# storing data into local variables
lt = df.latitude
lg = df.longitude
name = df.name
airport_type = df.type
country = df.iso_country
region = df.iso_region

# plotting data on graph
data = [
    go.Scattermapbox(
        lat=lt,
        lon=lg,
        mode='markers',
        hoverlabel=dict(font=dict(family='Roboto, sans-serif', size=14, color='white')),
        marker=dict(
            size=7,
            color='rgb(255, 0, 0)',
            opacity=0.7
        ),
        text='Name: ' + name + '<br>Type : ' + airport_type + '<br>Country: ' + country + '<br>Region: ' + region,
        hoverinfo='text'
    )
]

# styling layout
layout = go.Layout(
    title='Airports',
    font=dict(family='Roboto, sans-serif', size=18, color='black'),
    images=[dict(
        source="https://raw.githubusercontent.com/arjun-thakor/python-pandas-world-airports/master/logo.png",
        xref="paper", yref="paper",
        x=0.1, y=1.0,
        sizex=0.2, sizey=0.2,
        xanchor="center", yanchor="bottom")],
    autosize=True,
    hovermode='closest',
    mapbox=dict(
        accesstoken='pk.eyJ1IjoiYXJqdW4tdGhha29yIiwiYSI6ImNqcGtucWMzcjA1YXo0NG11dW92ZnhvbGEifQ.3aoFUmAWQn7jP-swCU7rjw',
        style='satellite'
    ),
)

# combining data and layout together
fig = dict(data=data, layout=layout)

# drawing figure and adding file name
plot(fig, filename='World Airports.html')