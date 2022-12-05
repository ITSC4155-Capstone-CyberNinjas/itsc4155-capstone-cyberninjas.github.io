import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("csv/TransitSamplesGreen.csv")

fig = go.Figure(go.Bar(x = df['Stop'], y = df['Count'],
                  hovertext=df['Timestamp'],
                  name='People On/Off bus stop'))

fig.update_layout(title='UNCC CAMPUS GREEN ROUTE TRANSPODRTATION DATA',
                   plot_bgcolor='rgb(230, 230,230)',
                   showlegend=True)

fig.write_html("greenRouteChart.html")