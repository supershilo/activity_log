import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
# Load the dataset 
data = pd.read_csv("Alegam_ActivityLog.csv")

# Initialize the Dash app
app = dash.Dash(__name__, title="Activity Log")

top_10_activities = data.sort_values(by='Duration (mins)', ascending=True).head(10)
top_10_feelings = data.sort_values(by='How I feel', ascending=True).head(10)

# Define the layout of the dashboard with custom styling
app.layout = html.Div([
    html.Div([
        html.Div(html.B("My Activity Log Dashboard 📊"), style={
            'color': '#1d1545',
            'padding': '1%',
            'font-size': '1.5em',
            'text-align': 'center',
            'height': '20px',
            
        }),
        html.Div(["By: Cielo C. Alegam ",
        ], style={
            'color': '#1d1545',
            'text-align': 'center',
            'font-size': '1em',
            'margin-bottom': '10px',
        }),
    ], style={'background-color': 'rgb(255,255,255, 0.3)','border-radius': '50px 50px'}), 
   
    #IFRAMES FROM FLOURISH
    #Histogram
    html.Div(html.B("My Sleep Duration Over the Days"), style={
            'color': '#EEEDED',
            'background-color': '#1d1545',
            'font-size': '1.2em',
            'text-align': 'center',  # Center text horizontally
            'height': '20px',   
            'width': '58%',
            'padding': '1%',
            'border-radius': '25px 25px 0px 0px',
            'margin': 'auto',  # Center horizontally
            'display': 'flex',
            'align-items': 'center'  # Center vertically
        }),
    html.Div(
    html.Iframe(src="https://flo.uri.sh/visualisation/15475748/embed", width="60%", height="500", style={'border': 'none'}),
    style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center','margin-bottom': '20px'}
), 
    html.Div(html.B("My Mood Over the Days"), style={
            'color': '#EEEDED',
            'background-color': '#1d1545',
            'font-size': '1.2em',
            'text-align': 'center',
            'height': '20px',
            'width': '58%',
            'padding': '1%',
            'border-radius': '25px 25px 0px 0px',
            'margin': 'auto',  # Center horizontally
            'display': 'flex',
            'align-items': 'center'  # Center vertically
            }),
    html.Div(
    html.Iframe(src="https://flo.uri.sh/visualisation/15476287/embed", width="60%", height="500", style={'border': 'none'}),
    style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center','margin-bottom': '20px'}
),

    
    #Stress Level vs Quality of Sleep
    html.Div(html.B("My Mood Over Time"), style={
            'color': '#EEEDED',
            'background-color': '#1d1545',
            'font-size': '1.2em',
            'text-align': 'center',
            'height': '20px',
            'width': '58%',
            'padding': '1%',
            'border-radius': '25px 25px 0px 0px',
            'margin': 'auto',  # Center horizontally
            'display': 'flex',
            'align-items': 'center'  # Center vertically
        }),
    html.Div(
    html.Iframe(src="https://flo.uri.sh/visualisation/15476636/embed", width="60%", height="500", style={'border': 'none'}),
    style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center','margin-bottom': '20px'}
), 
   
    #Age Vs Quality of Sleep
    html.Div(html.B("Activity Duration vs. Emotions"), style={
            'color': '#EEEDED',
            'background-color': '#1d1545',
            'font-size': '1.2em',
            'text-align': 'center',
            'height': '20px',
            'width': '58%',
            'padding': '1%',
            'border-radius': '25px 25px 0px 0px',
            'margin': 'auto',  # Center horizontally
            'display': 'flex',
            'align-items': 'center'  # Center vertically
        }),
    html.Div(
    html.Iframe(src="https://flo.uri.sh/visualisation/15476179/embed", width="60%", height="500", style={'border': 'none'}),
    style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center','margin-bottom': '20px'}
), 
    #Coefficient barchart
    html.Div(html.B("Activity Duration vs. Value"), style={
            'color': '#EEEDED',
            'background-color': '#1d1545',
            'font-size': '1.2em',
            'text-align': 'center',
            'height': '20px',
            'width': '58%',
            'padding': '1%',
            'border-radius': '25px 25px 0px 0px',
            'margin': 'auto',  # Center horizontally
            'display': 'flex',
            'align-items': 'center'  # Center vertically
        }),
   html.Div(
    html.Iframe(src="https://flo.uri.sh/visualisation/15474231/embed", width="60%", height="500", style={'border': 'none'}),
    style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center','margin-bottom': '20px'}
), 

    
    #Cookbook hyperlink
    #html.P(
    #style={'text-align': 'center','background-color': 'rgb(255,255,255, 0.3)','padding': '1%','color': '#1d1545','font-size': '1em'},  # Center-align the content
    #children=[
    #    "Check out the ",
    #    dcc.Link("Global AI Index Cookbook 👩‍🍳", href="https://supershilo.github.io/AI-Global-Index-Cookbook/Global%20AI%20Index%20Cookbook.html", target="_blank")
    #]
#)



], style={'font-family': 'Arial, sans-serif', 'padding': '20px', 'background': 'linear-gradient(90deg, #c2e59c, #64b3f4)'})

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
