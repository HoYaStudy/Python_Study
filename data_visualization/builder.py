import dash_html_components as html


def make_table(df):
    return html.Table(
        children=[
            html.Thead(
                style={"display": "block", "marginBottom": 25},
                children=[
                    html.Tr(
                        style={
                            "display": "grid",
                            "gridTemplateColumns": "repeat(4, 1fr)",
                            "fontSize": 16,
                            "fontWeight": "600",
                        },
                        children=[
                            html.Th(column_name.replace("_", " "))
                            for column_name in df.columns
                        ],
                    )
                ],
            ),
            html.Tbody(
                style={
                    "maxHeight": "50vh",
                    "display": "block",
                    "overflow": "scroll",
                },
                children=[
                    html.Tr(
                        style={
                            "display": "grid",
                            "gridTemplateColumns": "repeat(4, 1fr)",
                            "border-top": "1px solid white",
                            "padding": "30px 0px",
                        },
                        children=[
                            html.Td(
                                data,
                                style={"textAlign": "center"},
                            )
                            for data in value
                        ],
                    )
                    for value in df.values
                ],
            ),
        ]
    )
