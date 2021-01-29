import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

songtype = pd.read_csv('svt_songtype.csv')

app = dash.Dash(__name__)
fig1 = px.scatter(songtype, x="청량", y="신남")

# Variable Declaration

app.layout = html.Div([
    html.Img(src="/assets/svt_wallpaper_1.jpg"),
    html.Div([
        html.Div([html.H1('SVT', className='rosequartz'),
                  html.H1('Songtype', className='serenity'),
                  html.H1('Dashboard', className='rosequartz')],
                 className='service-name'),
        html.Div([html.P("Enter your Name >", className='label'),
                  dcc.Input(id='input-username', value='캐럿', placeholder='Error')],
                 className='row-flex'),
        html.A(html.Button(id='start-button', children='START!'), href="#anchor-1")
    ], className='intro'),
    html.Div([html.P(id='welcome-message', children='WELCOME!'),
              html.A(id="anchor-1"),
              dcc.Graph(id='main-graph', figure=fig1)],
             id='main-section')
])


@app.callback(
    Output(component_id='welcome-message', component_property='children'),
    Input(component_id='input-username', component_property='value')
)

def set_username(input_text):
    return f'반가워요! {input_text}님💎의 세븐틴 노래 취향을 알아보세요!'

# Turn Server On
if __name__ == '__main__':
    app.run_server(debug=True)