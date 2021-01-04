
from dash.dependencies import Input, Output

import plotly.express as px

from app import app
from pages.gdpr.gdpr_data import dataframe


@app.callback(
    Output('graph-with-slider', 'figure'),
    Input('year-slider', 'value'))
def update_figure(selected_year):
    gdpr_data = dataframe()
    filtered_df = gdpr_data[gdpr_data.year == selected_year]

    fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp",
                     size="pop", color="continent", hover_name="country",
                     log_x=True, size_max=55)

    fig.update_layout(transition_duration=500)

    return fig