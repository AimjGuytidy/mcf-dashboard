import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

app = dash.Dash(__name__)
app.layout = dbc.Row([
    dbc.Col("column 1",lg=2),
    dbc.Col("column 2",lg={"size":5,"offset":2}),
    dbc.Col("column 3",lg={"size":4,"offset":7})
])

if __name__ == "__main__":
    app.run_server(debug=True,port=1224)