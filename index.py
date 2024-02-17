from dash.dependencies import Input, Output, State
from dash import dcc, html
from flask_login import login_user
from flask import Flask
from flask_login import LoginManager, UserMixin
import dash

# Flask server
server = Flask(__name__)
server.secret_key = 'your-secret-key'

# Flask-Login manager
login_manager = LoginManager()
login_manager.init_app(server)

# User class for Flask-Login
class User(UserMixin):
    def __init__(self, id):
        self.id = id

# For simplicity, we use dictionary to store users in this example
# In a real-world application, you would store your user data in a database
users = {'admin': {'password': 'admin'}}

# Dash app
app = dash.Dash(__name__, server=server, suppress_callback_exceptions=True, url_base_pathname='/dashboard/')

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

login_page = html.Div(className='container', children=[
    html.Div(className='login-form', children=[
        dcc.Input(id='username', type='text', placeholder='Enter your username'),
        dcc.Input(id='password', type='password', placeholder='Enter your password'),
        html.Button('Submit', id='submit-val', n_clicks=0, className='button'),
        html.Div(id='container-button-basic',
                 children='Enter your username and password and press submit')
    ])
])

home_page = html.Div(className='container', children=[
    html.Div(className='login-form', children=[
        dcc.Input(id='username', type='text', placeholder='Enter your username'),
        dcc.Input(id='password', type='password', placeholder='Enter your password'),
        html.Button('Submit', id='submit-val', n_clicks=0, className='button'),
        html.Div(id='container-button-basic',
                 children='Enter your username and password and press submit')
    ])
])

users_page = html.Div(className='container', children=[
    html.Div(className='login-form', children=[
        dcc.Input(id='username', type='text', placeholder='Enter your username'),
        dcc.Input(id='password', type='password', placeholder='Enter your password'),
        html.Button('Submit', id='submit-val', n_clicks=0, className='button'),
        html.Div(id='container-button-basic',
                 children='Enter your username and password and press submit')
    ])
])

@app.callback(
    Output('container-button-basic', 'children'),
    [Input('submit-val', 'n_clicks')],
    [State('username', 'value'), State('password', 'value')]
)
def update_output(n_clicks, input1, input2):
    if n_clicks > 0:
        if input1 in users and users[input1]['password'] == input2:
            user = User(input1)
            login_user(user)
            return 'Logged in successfully.'
        else:
            return 'Invalid username or password.'
    else:
        return 'Enter your username and password and press submit.'
    

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/dashboard/home':
        return home_page
    elif pathname == '/dashboard/users':
        return users_page
    else:
        return login_page  # Default to login page

if __name__ == '__main__':
    app.run_server(debug=True)
