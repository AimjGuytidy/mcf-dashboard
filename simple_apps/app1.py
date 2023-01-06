import dash
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[html.H3("A Blue Header")],
    style={"color":"blue",
           "fontSize":"50px",
           "marginRight":"11%"}
)

if __name__=="__main__":
    app.run_server(debug=True,port=1222)
