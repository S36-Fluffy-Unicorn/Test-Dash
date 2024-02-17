import dash_bootstrap_components as dbc


navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="/")),
        dbc.NavItem(dbc.NavLink("Robot Controls", href="users")),
        dbc.NavItem(dbc.NavLink("Staff Management", href="dashboard")),
    ],
    brand="Workflow Management App",
    brand_style={"text_align":"left"},
    brand_href="/",
    color="primary",
    dark=True,
)