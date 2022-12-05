import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("csv/SampleLocations.csv")

fig = go.Figure(go.Bar(x = df['Name'], y = df['Count'],
                  hovertext=df['Timestamp'],
                  name='Devices connected to WIFI'))

fig.update_layout(title='UNCC CAMPUS WIFI DATA',
                   plot_bgcolor='rgb(230, 230,230)',
                   showlegend=True)

fig.write_html("wifichartinfo.html")