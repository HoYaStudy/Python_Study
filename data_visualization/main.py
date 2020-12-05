import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from data import (
    countries_df,
    totals_df,
    dropdown_options,
    make_global_df,
    make_country_df,
)
from builder import make_table

stylesheets = [
    "https://cdn.jsdelivr.net/npm/reset-css@5.0.1/reset.min.css",
    "https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600&display=swap",
]

app = dash.Dash(__name__, external_stylesheets=stylesheets)

app.title = "hCoronaDash"

map_figure = px.scatter_geo(
    countries_df,
    title="confirmed By Country",
    hover_name="Country_Region",
    color="Confirmed",
    color_continuous_scale=px.colors.sequential.Oryel,
    size="Confirmed",
    size_max=40,
    locations="Country_Region",
    locationmode="country names",
    projection="equirectangular",
    hover_data={
        "Confirmed": ":,",
        "Recovered": ":,",
        "Deaths": ":,",
        "Country_Region": False,
    },
    template="plotly_dark",
)
map_figure.update_layout(
    margin=dict(l=0, r=0, t=50, b=30), coloraxis_colorbar=dict(xanchor="left", x=0)
)

bar_figure = px.bar(
    totals_df,
    x="Condition",
    y="Count",
    title="Total Global Cases",
    labels={"condition": "Condition", "count": "Count", "color": "Condition"},
    hover_data={"Count": ":,"},
    template="plotly_dark",
)
bar_figure.update_traces(marker_color=["#e74c3c", "#8e44ad", "#27ae60"])


app.layout = html.Div(
    style={
        "minHeight": "100vh",
        "color": "white",
        "backgroundColor": "#111111",
        "fontFamily": "Open Sans, sans-serif",
    },
    children=[
        html.Header(
            style={"marginBottom": 100, "paddingTop": "50px", "textAlign": "center"},
            children=[
                html.H1(
                    "Corona Dashboard",
                    style={"fontSize": 50},
                )
            ],
        ),
        html.Div(
            style={
                "display": "grid",
                "gridTemplateColumns": "repeat(4, 1fr)",
                "gap": "50",
            },
            children=[
                html.Div(
                    style={"grid-column": "span 3"},
                    children=[dcc.Graph(figure=map_figure)],
                ),
                html.Div(children=[make_table(countries_df)]),
            ],
        ),
        html.Div(
            style={
                "display": "grid",
                "gridTemplateColumns": "repeat(4, 1fr)",
                "gap": "50",
            },
            children=[
                html.Div(children=[dcc.Graph(figure=bar_figure)]),
                html.Div(
                    style={"grid-column": "span 3"},
                    children=[
                        dcc.Dropdown(
                            style={
                                "width": 320,
                                "margin": "0 auto",
                                "color": "#111111",
                            },
                            id="country",
                            options=[
                                {"label": country, "value": country}
                                for country in dropdown_options
                            ],
                        ),
                        dcc.Graph(id="country_graph"),
                    ],
                ),
            ],
        ),
    ],
)


@app.callback(Output("country_graph", "figure"), [Input("country", "value")])
def update_country(value):
    if value:
        df = make_country_df(value)
    else:
        df = make_global_df()
    fig = px.line(
        df,
        x="date",
        y=["confirmed", "deaths", "recovered"],
        template="plotly_dark",
        labels={"value": "Cases", "variable": "Condition", "date": "Date"},
        hover_data={"value": ":,", "variable": False, "date": False},
    )
    fig.update_xaxes(rangeslider_visible=True)
    fig["data"][0]["line"]["color"] = "#e74c3c"
    fig["data"][1]["line"]["color"] = "#8e44ad"
    fig["data"][2]["line"]["color"] = "#27ae60"
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)