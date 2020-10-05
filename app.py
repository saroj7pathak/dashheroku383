import dash
# import dash_table
# from dash.dependencies import Input, Output
import pandas as pd
import numpy as np
# import scipy as sp
# import chart_studio.plotly as py
# import plotly.figure_factory as ff
import plotly.graph_objects as go
import plotly.express as px
import folium
data = pd.read_csv("C:/Users/saroj/Documents/GitHub/383dash_heroku/choleraDeaths.tsv", sep='\t')
data["Attack_death_total"] = data.apply(lambda row: row.Attack + row.Death, axis=1)
fig = go.Figure(data=[go.Table(
    header=dict(values=list(data.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[data.Date, data.Attack, data.Death, data.Attack_death_total],
               fill_color='lavender',
               align='left'))
])

fig.show()


data["Cum_attack"] = data.Attack.cumsum()
data["Cum_death"] = data.Death.cumsum()


fig = px.line(data, x="Date", y="Death")
fig.show()

fig = go.Figure()
# Create and style traces
fig.add_trace(go.Scatter(x=data["Date"], y=data["Death"], name='Death each day',
                         line=dict(color='firebrick', width=2)))
fig.add_trace(go.Scatter(x=data["Date"], y=data["Attack"], name='Attack each day',
                         line=dict(color='royalblue', width=2)))
fig.add_trace(go.Scatter(x=data["Date"], y=data["Cum_death"], name='Cummulative death',
                         line=dict(color='firebrick', width=3)))
fig.add_trace(go.Scatter(x=data["Date"], y=data["Cum_attack"], name='Cummulative attack',
                         line=dict(color='royalblue', width=3)))

fig.update_layout(title='Cholera Attack and Death distribituion over time ',
                   xaxis_title='Date',
                   yaxis_title='Number of People')


fig.show()
import pandas as pd
data = pd.read_csv("C:/Users/saroj/Documents/GitHub/383dash_heroku/naplesCholeraAgeSexData.tsv",sep='\t')
#print(data)
fig = go.Figure(data=[go.Table(
    header=dict(values=list(data.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[data.age,data.male, data.female],
               fill_color='lavender',
               align='left'))
])

fig.show()

fig = px.bar(data, x="age", y="male",title="Age categories for male fatalities")
fig.show()
fig = px.bar(data, x="age", y="female",title="Age categories for female fatalities")
fig.show()
fig = px.bar(data, y=["male","female"],x="age",title="Age categories for male and female fatalities")
fig.show()
data = pd.read_csv("C:/Users/saroj/Documents/GitHub/383dash_heroku/UKcensus1851.csv",sep=",",skiprows=[0,1,2])
data["Overall_total"]=data.apply(lambda row: row.male + row.female, axis=1)
fig = go.Figure(data=[go.Table(
    header=dict(values=list(data.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[data.age,data.male, data.female, data.Overall_total],
               fill_color='lavender',
               align='left'))
])

fig.show()
fig = px.pie(data, values='male', names='age', title='Distribution of male population')
fig.show()
fig = px.pie(data, values='female', names='age', title='Distribution of female population')
fig = px.bar(data, x="age", y="male",title="Distribution of male population")
fig.show()
fig = px.bar(data, x="age", y="female",title="Distribution of female population")
fig.show()
fig = px.pie(data, values='Overall_total', names='age', title='Distribution of overall population')
fig.show()
data = pd.read_csv("C:/Users/saroj/Documents/GitHub/383dash_heroku/Copy of choleraDeathLocations.csv",sep=",",header=None)
data.columns=["Death","long","lat"]
dataa = pd.read_csv("C:/Users/saroj/Documents/GitHub/383dash_heroku/choleraPumpLocations.csv",sep=",",header=None)
dataa.columns=["long","lat"]


base_map = folium.Map(location=[51.512, -0.137],
                      zoom_start=16)
for i in range(len(data)):
    folium.Circle(
        location=[data.iloc[i]["lat"], data.iloc[i]["long"]],
        fill=True,
        radius=(int((np.log(data.iloc[i, -1] + 1.00001))) + 0.2) * 3,
        fill_color='Green',
        color='Red',
        tooltip="<div style='margin: 0; background-color: black; color: white;'>" +
                "<h5 style='text-align:center;font-weight: bold'>Death_location</h5>"
                "<hr style='margin:0px;color: white;'>" +
                "<ul style='color: white;;list-style-type:square;align-item:center;padding-left:5px;padding-right:-5px'>" +
                "<li>Death: " + str(data.iloc[i, 0]) + "</li>" +
                "<li>Longitude:   " + str(data.iloc[i, 1]) + "</li>" +
                "<li>Latitude: " + str(data.iloc[i, 2]) + "</li>",

    ).add_to(base_map)
for i in range(len(dataa)):
    folium.Circle(
        location=[dataa.iloc[i]["lat"], dataa.iloc[i]["long"]],
        fill=True,
        radius=(int((np.log(dataa.iloc[i, -1] + 1.00001))) + 0.2) * 4,
        fill_color='Blue',
        color='Black',
        tooltip="<div style='margin: 1px; background-color: black; color: white;'>" +
                "<h5 style='text-align:center;font-weight: simple'>Pump_location</h5>"
                "<hr style='margin:1px;color: white;'>" +
                "<ul style='color: white;;list-style-type:square;align-item:center;padding-left:5px;padding-right:-1px'>" +
                "<li>Longitude:   " + str(dataa.iloc[i, 0]) + "</li>" +
                "<li>Latitude: " + str(dataa.iloc[i, 1]) + "</li>",
    ).add_to(base_map)
base_map
app = dash.Dash()
server = app.server
