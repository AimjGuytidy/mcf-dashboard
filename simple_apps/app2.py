import dash
import dash_html_components as html
import dash_bootstrap_components as dbc

#instantiate the app object

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.MINTY])

#design the layout of your dashboard

app.layout=html.Div(children=[
    html.H1("MasterCard Foundation",
            style={"color":"#FF7B54",
                   "fontSize":"40px"}),
    html.H2("Young Africa Works",
            style={"color":"#939B62",
                   "fontSize":"28px"}),
    #html.P("")
    dbc.Tabs([
        dbc.Tab([html.Ul([
        html.Br(),
        html.Li(["Number of Dignified and Fulfilling Work to be created: ",html.B("30,000,000")]),
        html.Li("Number of countries considered: 7"),
        html.Li("Impact Organisation Partner in Rwanda: Vanguard Economics"),
        html.Li(["Source: ",html.A(html.B("Young Africa Works"),href="https://mastercardfdn.org/research/young-africa-works/",style={"color":"navy"})])
    ])],label="Key Information"),
        dbc.Tab([html.Ul([
            html.Br(),
            html.Li("Sample Size: 4061 youth between the age 18-32"),
            html.Li("Number of districts reached: 30"),
            html.Li("Data collection Duration: 2 weeks"),
            html.Li("Project Manager: Vanguard Economics")

        ])],label="Dashboard Info")
    ])

])

if __name__=="__main__":
    app.run_server(debug=True,port=1223)
