import dash
from dash import html, dcc
from pages import navigation

dash.register_page(__name__, path="/")


layout = html.Div(
    [   
        navigation.navbar,
        html.Br(),
        dcc.Link("Go to Page 1", href="/users"),
        html.Br(),
        # dcc.Link("Go to Page 2", href="/page-2"),
    ]
)